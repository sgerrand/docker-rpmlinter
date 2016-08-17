Summary:   Test package
Name:      test
Version:   1.0
Release:   1
License:   Public Domain
Group:     Development/Tools
BuildArch: noarch
%description
Trivial test package
%prep
%build
%install
mkdir -p $RPM_BUILD_ROOT/tmp
touch $RPM_BUILD_ROOT/tmp/test %files /tmp/test
%changelog
