Summary:	Firmware loader for M-Audio/Midiman usb sound devices
Name:		madfu-firmware
Version:	0.5
Release:	 %mkrel 5
License:	GPL
Group:		System/Kernel and hardware		

Source:		http://prdownloads.sourceforge.net/xbox-linux/%{name}-%{version}.tar.bz2
Url:		https://usb-midi-fw.sourceforge.net/
BuildRoot:	%_tmppath/%name-%version-root
Exclusivearch:	%{ix86}

%description
This package allows you to use the USB Audio interfaces from M-Audio/
Midiman with Linux.  It sets up an hotplugging script to load the
firmware from the Windows driver files.

Firmware files are not distributed with this package but can be extracted
from the Windows drivers and placed in %{_datadir}/usb/maudio.

%prep
%setup -q

%build
# (sb) just to trick configure
for firmware in [ ma003101 ma004100 ma004103 ma005101 ma006100 ma008100 ]; do
touch $firmware.bin
done
%configure
%make

%install
rm -fr %buildroot
%makeinstall
# (sb) empty firmware files we created in build stage
rm -f %buildroot/%{_datadir}/usb/maudio/*.bin

%clean
rm -fr %buildroot

%files 
%defattr(-,root,root)
%doc README Changelog
%dir %{_datadir}/usb/maudio
%{_sbindir}/madfuload
%{_sysconfdir}/hotplug/usb/maudio_dfu
%config(noreplace) %{_sysconfdir}/hotplug/usb/maudio_dfu.usermap



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-5mdv2011.0
+ Revision: 620287
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2010.0
+ Revision: 429889
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.5-3mdv2009.0
+ Revision: 251643
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.5-1mdv2008.1
+ Revision: 129594
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import madfu-firmware


* Mon Apr 11 2005 Stew Benedict <sbenedict@mandrakesoft.com>  0.5-1mdk
- first Mandriva release
