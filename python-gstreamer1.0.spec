# gst1 api recall here
%define api 1.0
%define oname gst-python

Name:           python-gstreamer%{api}
Version:        1.2.1
Release:        1
Summary:        Python bindings for GStreamer%{api}

Group:          Development/Python
License:        LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-python/%{oname}-%{version}.tar.bz2

BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig
BuildRequires:  gstreamer%{api}-devel >= 1.2.0
BuildRequires:  pkgconfig(pygobject-3.0)

Requires:       python-gobject3
Requires:       gstreamer >= 1.2.0

Provides:       gstreamer%{api}-python = %{EVRD}

%description
This module contains PyGObject overrides to make it easier to write
applications that use GStreamer 1.0 in Python.


%prep
%setup -qn %{oname}-%{version}

%build
%configure 
%{make}

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{py_platsitedir}/gi/overrides/*

