# TODO:
# - find missing requirements
Summary:	Educational game based on multimedia elements
Summary(pl.UTF-8):	Gra edukacyjna oparta na elementach multimedialnych
Name:		omnitux
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/omnitux/v0.9/%{name}-%{version}.noarch.tar.bz2
# Source0-md5:	03a307c21cf4d3918ef976b465a5b4fc
URL:		http://omnitux.sourceforge.net/
BuildRequires:	rpm-pythonprov
Requires:	python-pygame
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		datadir	%{_datadir}/games/%{name}

%description
Educational activities based on multimedia elements (images, sounds,
and text).

%description -l pl.UTF-8
Ćwiczenia edukacyjne oparte na elementach multimedialnych (obrazki,
dźwięki oraz tekst).

%prep
%setup -q -n %{name}

cat <<'EOF' > omnitux
#!/bin/sh
cd %{datadir}/bin
exec python menu.py "$@"
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{datadir}}
install -p omnitux $RPM_BUILD_ROOT%{_bindir}
cp -a bin data $RPM_BUILD_ROOT%{datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# LICENSE.txt contains list of contributors
%doc LICENSE.txt
%attr(755,root,root) %{_bindir}/omnitux
%{datadir}
