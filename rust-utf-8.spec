# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate utf-8

Name:           rust-%{crate}
Version:        0.7.5
Release:        5%{?dist}
Summary:        Incremental, zero-copy UTF-8 decoding with error handling

# Upstream license specification: MIT OR Apache-2.0
# https://github.com/SimonSapin/rust-utf8/issues/3
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/utf-8
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Incremental, zero-copy UTF-8 decoding with error handling.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 11:33:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.5-3
- Regenerate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.7.5-1
- Update to 0.7.5
- Adapt to new packaging

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.4-1
- Initial package
