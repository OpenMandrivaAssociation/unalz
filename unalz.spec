Summary:	Unpacks ALZip files
Name:		unalz
Version:	0.65
Release:	%mkrel 1
License:	BSD
Group:		Archiving/Compression
URL:		http://www.kipple.pe.kr/win/unalz/
Source0:	http://www.kipple.pe.kr/win/unalz/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: zlib-devel

%description
This is a decompressor for files generated by ALZip (*.alz).

%prep

%setup -q -n %name
chmod 644 *.txt

%build
%make linux-utf8

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D %name %buildroot%_bindir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt
%_bindir/%name


