Summary:	Educational game based on multimedia elements
Summary(pl.UTF-8):	Gra edukacyjna oparta na elementach multimedialnych
Name:		omnitux
Version:	0.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/omnitux/v0.9/%{name}-%{version}.noarch.tar.bz2
# Source0-md5:	3696c33b67549a722550b23ddcd7b0a0
URL:		http://omnitux.sourceforge.net/
Requires:	python-pygame
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Educational activities based on multimedia elements (images, sounds,
and text).

%description -l pl.UTF-8
Ćwiczenia edukacyjne oparte na elementach multimedialnych (obrazki,
dźwięki oraz tekst).

%prep
%setup -q -n %{name}

cat <<'EOF' >omnitux
#!/bin/sh
cd %{_datadir}/%{name}/bin/
python menu.py
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install omnitux $RPM_BUILD_ROOT%{_bindir}
cp -r {bin,data} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# LICENSE.txt contains list of contributors
%doc LICENSE.txt
%attr(755,root,root) %{_bindir}/omnitux
%{_datadir}/%{name}
