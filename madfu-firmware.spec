Summary:	Firmware loader for M-Audio/Midiman usb sound devices
Name:		madfu-firmware
Version:	0.5
Release:	 %mkrel 1
License:	GPL
Group:		System/Kernel and hardware		

Source:		http://prdownloads.sourceforge.net/xbox-linux/%{name}-%{version}.tar.bz2
Url:		http://usb-midi-fw.sourceforge.net/
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

