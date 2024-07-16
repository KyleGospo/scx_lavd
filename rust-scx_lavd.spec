# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global crate scx_lavd

Name:           rust-scx_lavd
Version:        1.0.1
Release:        %autorelease
Summary:        Latency-criticality Aware Virtual Deadline

License:        GPL-2.0-only
URL:            https://crates.io/crates/scx_lavd
Source:         %{crates_source}
Source:         scx_lavd-1.0.1-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A Latency-criticality Aware Virtual Deadline (LAVD) scheduler based on
sched_ext, which is a Linux kernel feature which enables implementing
kernel thread schedulers in BPF and dynamically loading them.
https://github.com/sched-ext/scx/tree/main.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        # FIXME
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/scx_lavd

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
