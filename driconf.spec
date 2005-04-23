Summary:	DRI configuration GUI
Summary(pl):	Graficzny interfejs do konfiguracji DRI
Name:		driconf
Version:	0.2.6
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dri.freedesktop.org/~fxkuehl/driconf/%{name}-%{version}.tar.gz
# Source0-md5:	92058855dbf48442d3e3b86f153b40cb
URL:		http://dri.sourceforge.net/cgi-bin/moin.cgi/DriConf
BuildRequires:	python
BuildRequires:	python-modules
# xdriinfo exists only in X.org X11 >= 6.8
Requires:	X11-tools >= 1:6.8.0
Requires:	python-pygtk-gtk >= 2:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRIConf is the first configuration GUI for DRI and the new
ConfigurationInfrastructure. It is written in Python with the
python-gtk toolkit bindings.

%description -l pl
DRIConf to pierwszy graficzny interfejs do konfiguracji DRI i nowej
infrastruktury konfiguracji. Jest napisany w Pythonie z u¿yciem wi±zañ
python-gtk.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/driconf
%{py_sitescriptdir}/*.py[co]
