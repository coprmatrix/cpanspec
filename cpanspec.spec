#
# spec file for package cpanspec
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name cpanspec
Name:           cpanspec
Version:        0
Release:        9
Summary:        Generate a SUSE spec file for a CPAN module
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Languages/Perl
URL:            https://github.com/openSUSE/cpanspec
Source0:        cpanspec-%{version}.tar.xz
BuildRequires:  perl
BuildRequires:  rpm_macro(perl_make_install)
BuildRequires:  rpm_macro(perl_process_packlist)
BuildRequires:  rpm_macro(perl_gen_filelist)
BuildRequires:  (perl-generators or rpm-build-perl)
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Parse::CPAN::Packages)
BuildRequires:  perl(Perl::PrereqScanner)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::Simple::TextContent)
BuildRequires:  perl(Text::Autoformat)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::XS)
BuildRequires:  sed
BuildRequires:  perl(Capture::Tiny)
Requires:       perl(Algorithm::Diff)
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(Class::Accessor::Chained)
Requires:       perl(File::ShareDir::Install)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Build::Tiny)
Requires:       perl(Parse::CPAN::Packages)
Requires:       perl(Perl::PrereqScanner)
Requires:       perl(Pod::POM)
Requires:       perl(Pod::Simple::TextContent)
Requires:       perl(Text::Autoformat)
Requires:       perl(Text::Capitalize)
Requires:       perl(FFI::CheckLib)
Requires:       perl(YAML)
Requires:       perl(YAML::XS)
#Recommends:     obs-service-format_spec_file
Recommends:     osc
Recommends:     perl(IO::Uncompress::Bunzip2)
BuildArch:      noarch
Patch0:         disable_prepare_spec.patch
Patch1:         fix_requires.patch
Requires:       perl(:MODULE_COMPAT_%{perl_version})

%description
*cpanspec* will generate a spec file to build a rpm from a CPAN-style Perl
module distribution.

%prep
%autosetup -p1 -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644
sed -i 's/\(our[[:space:]]*$VERSION[[:space:]]*=[[:space:]]*'"'"'\)\(.*\)\('"'"'.*\)/\1%{version}\3/;' cpanspec

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test
perl ./cpanspec -h

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license COPYING
%doc Artistic BUGS Changes TODO cpanspec.yml

%changelog
