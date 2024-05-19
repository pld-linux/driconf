Summary:	DRI configuration GUI
Summary(pl.UTF-8):	Graficzny interfejs do konfiguracji DRI
Name:		driconf
Version:	0.9.1
Release:	5
License:	GPL v2+
Group:		X11/Applications
Source0:	https://people.freedesktop.org/~fxkuehl/driconf/%{name}-%{version}.tar.gz
# Source0-md5:	76d610bcd56aa5e8a489debb5081178a
URL:		https://dri.sourceforge.net/wiki/DriConf/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-pygtk-gtk >= 2:2.4
Requires:	xorg-app-xdriinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRIConf is the first configuration GUI for DRI and the new
ConfigurationInfrastructure. It is written in Python with the
python-gtk toolkit bindings.

%description -l pl.UTF-8
DRIConf to pierwszy graficzny interfejs do konfiguracji DRI i nowej
infrastruktury konfiguracji. Jest napisany w Pythonie z użyciem wiązań
python-gtk.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--prefix=%{_prefix} \
	--install-purelib=%{py_sitescriptdir} \
	--root=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/driconf
%{_datadir}/driconf
%{py_sitescriptdir}/dri.py[co]
%{py_sitescriptdir}/driconf*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/driconf-*.egg-info
%endif
