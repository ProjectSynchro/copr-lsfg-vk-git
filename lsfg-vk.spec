%global tag 0
%global date 20250719
%global commit 8b63447
%global longcommit 8b63447d4167a603c60d2b3c48f13163d39c5569

Name:           lsfg-vk
Version:        %{tag}
Release:        1.%{date}git%{commit}%{?dist}
Summary:        Lossless Scaling Frame Generation on Linux via DXVK/Vulkan.

# SPDX
License:        MIT
URL:            https://github.com/PancakeTAS/lsfg-vk

Patch0:         0001-Build-system-changes.patch

BuildRequires:       clang
BuildRequires:       llvm
BuildRequires:       cmake
BuildRequires:       cmake-rpm-macros
BuildRequires:       ninja-build
BuildRequires:       git
BuildRequires:       pkgconfig(vulkan)
BuildRequires:       pkgconfig(SPIRV-Headers)
BuildRequires:       vulkan-headers

Recommends:          mesa-dri-drivers
Recommends:          mesa-vulkan-drivers

Requires:            %{name}-libs = %{version}-%{release}

%description
The %{name} package provides Lossless Scaling Frame Generation on Linux via DXVK/Vulkan.

%prep
git clone --single-branch --branch develop https://github.com/PancakeTAS/lsfg-vk
cd lsfg-vk
git checkout %{longcommit}
git submodule update --init --recursive

%autopatch -p1

%build
cd lsfg-vk

CMAKE_OPTIONS=(
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
   -DCMAKE_C_COMPILER=clang \
   -DCMAKE_CXX_COMPILER=clang++ \
   -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON
)
%__cmake "${CMAKE_OPTIONS[@]}" .
%__cmake --build . %{?_smp_mflags} --verbose

%install
cd lsfg-vk
DESTDIR="%{buildroot}" %__cmake --install .

%files
%license lsfg-vk/LICENSE.md
%{_datadir}/vulkan/implicit_layer.d/VkLayer_LS_frame_generation*.json

%package libs
Summary:       lsfg-vk libraries
%description libs
%summary

%files libs
%{_libdir}/liblsfg-vk.so

%changelog
%autochangelog
