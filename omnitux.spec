# TODO:
# - find missing requirements
Summary:	Educational game based on multimedia elements
Summary(pl.UTF-8):	Gra edukacyjna oparta na elementach multimedialnych
Name:		omnitux
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/omnitux/v1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	e0c4da272baaa4f09b90cc060f7b605c
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
