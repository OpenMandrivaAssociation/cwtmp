Name:		cwtmp
Version:	3.4
Release:	1
URL:		http://www.armory.com/~spcecdt/
Source0:	ftp://ftp.armory.com/pub/source/%{name}.tar.gz
License:	GPLv2
Group:		Text tools
Summary:	Clean up utmp & wtmp files (discard entries; fix corruption)

%description
cwtmp compresses a wtmp file by discarding the uninteresting utmp entries
that make up a large fraction of the typical wtmp file.  If no filename is
given, /etc/wtmp is read.  utmp entries in the file are written to the
output, except entries of type LOGIN_PROCESS, INIT_PROCESS, and EMPTY,
which are skipped.

%prep
%setup -q -c -n %{name}-%{version}

%build
%make CFLAGS="%{optflags}" LIBS="%{ldflags}"

%install
install -m755 %{name} -D %{buildroot}%{_sbindir}/%{name}
install -m644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%files 
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
