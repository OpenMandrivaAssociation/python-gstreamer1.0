# gst1 api recall here
%define api 1.0
%define oname gst-python
%define _disable_ld_no_undefined 1

Summary:	Python bindings for GStreamer%{api}
Name:		python-gstreamer%{api}
Version:	1.4.0
Release:	1
Group:		Development/Python
License:	LGPLv2.1+
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(gstreamer-%{api}) >= 1.4.0
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
Requires:	gstreamer1.0-tools >= 1.4.0
Requires:	python-gobject3
Provides:	gstreamer%{api}-python = %{EVRD}

%description
This module contains PyGObject overrides to make it easier to write
applications that use GStreamer 1.0 in Python.

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{py_platsitedir}/gi/overrides/*
%{_libdir}/gstreamer-1.0/libgstpythonplugin.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

%build
%configure
%make

%install
%makeinstall_std

