%global tag v0.9.0
%global date 20250729
%global commit c7b6e1a
%global longcommit c7b6e1a47c39decf66d1a41a38a9a07472d3fe4d

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
BuildRequires:       pkgconfig(gl)
BuildRequires:       pkgconfig(vulkan)
BuildRequires:       pkgconfig(SPIRV-Headers)
BuildRequires:       vulkan-headers
BuildRequires:       pkgconfig(wayland-client) >= 0.2.7
BuildRequires:       pkgconfig(wayland-cursor) >= 0.2.7
BuildRequires:       pkgconfig(wayland-egl) >= 0.2.7
BuildRequires:       pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:       pkgconfig(x11)
BuildRequires:       pkgconfig(xext)
BuildRequires:       pkgconfig(xrandr)
BuildRequires:       pkgconfig(xinerama)
BuildRequires:       pkgconfig(xcursor)
BuildRequires:       pkgconfig(xi)
BuildRequires:       pkgconfig(wayland-protocols)

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

%build
cd lsfg-vk

CMAKE_OPTIONS=(
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_C_COMPILER=clang \
   -DCMAKE_CXX_COMPILER=clang++ \
   -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON
)
%__cmake "${CMAKE_OPTIONS[@]}" .
%__cmake --build . %{?_smp_mflags} --verbose

%install
cd lsfg-vk

# Install the Vulkan layer JSON file and shared library
install -Dm644 VkLayer_LS_frame_generation.json "%{buildroot}/%{_datadir}/vulkan/implicit_layer.d/VkLayer_LS_frame_generation.json"
install -Dm644 liblsfg-vk.so "%{buildroot}/%{_libdir}/liblsfg-vk.so"

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
