%global tag 0
%global date 20250714
%global commit 83b869b
%global longcommit 83b869b0c4d4cd4da2e760126242c6ed76bafec8

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
   -DCMAKE_INSTALL_LIBDIR=%{_lib} \
   -DCMAKE_C_COMPILER=clang \
   -DCMAKE_CXX_COMPILER=clang++ \
   -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON
)

CC=clang
CXX=clang++

%cmake "${CMAKE_OPTIONS[@]}" .
%cmake_build

%install
cd lsfg-vk
%cmake_install

%check
cd lsfg-vk
%ctest

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
