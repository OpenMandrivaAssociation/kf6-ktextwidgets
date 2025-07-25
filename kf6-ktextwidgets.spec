%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6TextWidgets
%define devname %mklibname KF6TextWidgets -d
#define git 20240217

Name: kf6-ktextwidgets
Version: 6.16.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/ktextwidgets/-/archive/master/ktextwidgets-master.tar.bz2#/ktextwidgets-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/ktextwidgets-%{version}.tar.xz
%endif
Summary: Text editing widgets
URL: https://invent.kde.org/frameworks/ktextwidgets
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Sonnet)
# Just to make sure we don't pull in the KF5 version
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Text editing widgets

%package -n %{libname}
Summary: Text editing widgets
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Text editing widgets

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Text editing widgets

%prep
%autosetup -p1 -n ktextwidgets-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang

%files -n %{devname}
%{_includedir}/KF6/KTextWidgets
%{_libdir}/cmake/KF6TextWidgets

%files -n %{libname}
%{_libdir}/libKF6TextWidgets.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/ktextwidgets6widgets.so
