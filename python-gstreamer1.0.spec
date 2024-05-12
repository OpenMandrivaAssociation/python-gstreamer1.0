# gst1 api recall here
%define api 1.0
%define oname gst-python
%define _disable_ld_no_undefined 1

Summary:	Python bindings for GStreamer%{api}
Name:		python-gstreamer%{api}
Version:	1.24.3
Release:	1
Group:		Development/Python
License:	LGPLv2.1+
Url:		https://gstreamer.freedesktop.org/
Source0:	https://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gstreamer-%{api})
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python3)
Requires:	gstreamer1.0-tools
Requires:	python-gobject3
Provides:	gstreamer%{api}-python = %{EVRD}

%description
This module contains PyGObject overrides to make it easier to write
applications that use GStreamer 1.0 in Python.

%files
%doc COPYING ChangeLog NEWS
%{python_sitearch}/gi/overrides/
%{_libdir}/gstreamer-1.0/libgstpython.so
#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
