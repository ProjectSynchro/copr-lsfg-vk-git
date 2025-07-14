%global tag 0
%global date 20250713
%global commit f998647
%global longcommit f998647d74051467e39de9de2df2ff9a5996db5f

Name:           lsfg-vk
Version:        %{tag}
Release:        1.%{date}git%{commit}%{?dist}
Summary:        Lossless Scaling Frame Generation on Linux via DXVK/Vulkan.

# SPDX
License:        MIT
URL:            https://github.com/PancakeTAS/lsfg-vk

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

%description
The %{name} package provides Lossless Scaling Frame Generation on Linux via DXVK/Vulkan.

%prep
git clone --single-branch --branch develop https://github.com/PancakeTAS/lsfg-vk
cd lsfg-vk
git checkout %{longcommit}
git submodule update --init --recursive

%build
cd lsfg-vk

CMAKE_OPTIONS=(
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON
)

%cmake "${CMAKE_OPTIONS[@]}" .
%make_build

%install
cd lsfg-vk
%make_install

%check
ctest -V %{?_smp_mflags}

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
