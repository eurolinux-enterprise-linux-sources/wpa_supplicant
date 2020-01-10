Summary: WPA/WPA2/IEEE 802.1X Supplicant
Name: wpa_supplicant
Epoch: 1
Version: 0.7.3
Release: 9%{?dist}.2
License: BSD
Group: System Environment/Base
Source0: http://w1.fi/releases/%{name}-%{version}.tar.gz
Source1: %{name}.config
Source2: %{name}.conf
Source3: %{name}.init.d
Source4: %{name}.sysconfig
Source6: %{name}.logrotate

Requires(post):     /sbin/chkconfig
Requires(preun):    /usr/bin/killall
Requires(preun):    /sbin/service
Requires(preun):    /sbin/service

%define build_gui 1
%if 0%{?rhel} >= 1
%define build_gui 0
%endif

%if %{build_gui}
%define with_qt4 0
%if 0%{?fedora} >= 14
%define with_qt4 1
%endif
%endif

# distro specific customization and not suitable for upstream,
# works around busted drivers
Patch0: wpa_supplicant-assoc-timeout.patch
# ensures that debug output gets flushed immediately to help diagnose driver
# bugs, not suitable for upstream
Patch1: wpa_supplicant-flush-debug-output.patch
# disto specific customization for log paths, not suitable for upstream
Patch2: wpa_supplicant-dbus-service-file-args.patch
# quiet an annoying and frequent syslog message
Patch3: wpa_supplicant-quiet-scan-results-message.patch
# recover from streams of driver disconnect messages (iwl3945)
Patch4: wpa_supplicant-squelch-driver-disconnect-spam.patch
# allow more private key encryption algorithms
Patch5: wpa_supplicant-openssl-more-algs.patch
# Send PropertyChanged notificationes when the BSS list changes
Patch6: wpa_supplicant-bss-changed-prop-notify.patch
# Don't crash trying to pass NULL to dbus
Patch7: wpa_supplicant-dbus-null-error.patch
# Fix signal quality reporting for some drivers when using nl80211
Patch8: rh752032-0001-nl80211-Fix-UNSPEC-signal-quality-reporting.patch

# Session Management Entity (SME) patches for nl80211 driver
Patch20: rh713280-0001-sme-fix-retry-after-auth-assoc-timeout-failure.patch
Patch21: rh713280-0002-sme-optimize-recovery-from-common-load-balancing-mechanisms.patch
Patch22: rh713280-0003-sme-blacklist-bss-on-first-failure-if-only-a-single-network-is-enabled.patch
Patch23: rh713280-0004-sme-extend-load-balancing-optimization-in-bss-blacklisting.patch
Patch24: rh713280-0005-sme-optimize-recovery-from-association-command-failures.patch
Patch25: rh713280-0006-sme-add-timers-for-authentication-and-association.patch
Patch26: rh713280-0007-sme-nl80211-set-cipher-suites.patch

# Fixes for Opportunistic Key Caching (OKC)
Patch30: rh813579-0001-pmkokc-Set-portValid-TRUE-on-association-for-driver-based-4.patch
Patch31: rh813579-0002-pmkokc-Clear-WPA-and-EAPOL-state-machine-config-pointer-on-.patch
Patch32: rh813579-0003-pmkokc-Clear-driver-PMKSA-cache-entry-on-PMKSA-cache-expira.patch
Patch33: rh813579-0004-pmkokc-Flush-PMKSA-cache-entries-and-invalidate-EAP-state-o.patch
Patch34: rh813579-0005-pmkokc-Fix-proactive_key_caching-configuration-to-WPA-code.patch
Patch35: rh813579-0006-pmkokc-RSN-Add-a-debug-message-when-considing-addition-of-O.patch
Patch36: rh813579-0007-pmkokc-Clear-OKC-based-PMKSA-caching-entries-if-PMK-is-chan.patch
Patch37: rh813579-0008-pmkokc-Move-wpa_sm_remove_pmkid-call-to-PMKSA-cache-entry-f.patch
Patch38: rh813579-0009-pmkokc-Use-PMKSA-cache-entries-with-only-a-single-network-c.patch
Patch39: rh813579-0010-pmkokc-PMKSA-Do-not-evict-active-cache-entry-when-adding-ne.patch
Patch40: rh813579-0011-pmkokc-PMKSA-Set-cur_pmksa-pointer-during-initial-associati.patch
Patch41: rh813579-0012-pmkokc-PMKSA-make-deauthentication-due-to-cache-entry-remov.patch
Patch42: rh813579-0013-pmkokc-PMKSA-update-current-cache-entry-due-to-association-.patch

Patch50: rh837402-less-aggressive-roaming.patch

# Fixes for CVE-2015-0210 (wpa_supplicant: broken certificate subject check)
Patch51: rh1186806-0001-dbus_server_cert_info.patch
Patch52: rh1186806-0002-move_calls_to_notify.patch
Patch53: rh1186806-0003-write_server_cert.patch
Patch54: rh1186806-0004-domain_match.patch
Patch55: rh1186806-0005-cert_in_cb.patch

# Fix integer underflow in WMM Action frame parser: rh #1221178
Patch56: 0056-rh1221178-fix-int-unferflow-AP-WMM.patch

# Do not quote values for scan_freq and freq_list: rh #1254486
Patch57: rh1254486-dont-qoute-scan_freq-and-freq_list.patch

# reopen debug log file upon receipt of SIGHUP signal
Patch58: 0057-rh908306-log-rotate.patch

# Deauthenticate on reconfiguration: rh #1359044
Patch59: 0058-rh1359044-Deauthenticate-on-reconfiguration.patch

Patch60: rh1495530-0001-Clear-TK-part-of-PTK-after-driver-key-configuration.patch
Patch61: rh1495530-0002-Fix-TK-configuration-to-the-driver-in-EAPOL-Key-3-4-.patch
Patch62: rh1495530-0003-Reduce-the-amount-of-time-PTK-TPTK-GTK-is-kept-in-me.patch
Patch63: rh1495530-0004-Prevent-reinstallation-of-an-already-in-use-group-ke.patch
Patch64: rh1495530-0005-Prevent-installation-of-an-all-zero-TK.patch
Patch65: rh1495530-0006-Fix-PTK-rekeying-to-generate-a-new-ANonce.patch
Patch66: rh1495530-0007-FT-Do-not-allow-multiple-Reassociation-Response-fram.patch

URL: http://w1.fi/wpa_supplicant/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if %{build_gui}
%if %{with_qt4}
BuildRequires: qt-devel >= 4.0
%else
BuildRequires: qt3-devel
%endif
%endif
BuildRequires: openssl-devel
BuildRequires: readline-devel
BuildRequires: dbus-devel
BuildRequires: libnl-devel

%description
wpa_supplicant is a WPA Supplicant for Linux, BSD and Windows with support
for WPA and WPA2 (IEEE 802.11i / RSN). Supplicant is the IEEE 802.1X/WPA
component that is used in the client stations. It implements key negotiation
with a WPA Authenticator and it controls the roaming and IEEE 802.11
authentication/association of the wlan driver.

%if %{build_gui}

%package gui
Summary: Graphical User Interface for %{name}
Group: Applications/System

%description gui
Graphical User Interface for wpa_supplicant written using QT

%endif

%prep
%setup -q
%patch0 -p1 -b .assoc-timeout
%patch1 -p1 -b .flush-debug-output
%patch2 -p1 -b .dbus-service-file
%patch3 -p1 -b .quiet-scan-results-msg
%patch4 -p1 -b .disconnect-spam
%patch5 -p1 -b .more-openssl-algs
%patch6 -p1 -b .bss-changed-prop-notify
%patch7 -p1 -b .dbus-null
%patch8 -p1 -b .unspec-qual

%patch20 -p1 -b .fix-retry
%patch21 -p1 -b .load-balance
%patch22 -p1 -b .blacklist-bss-on-first
%patch23 -p1 -b .extend-load-balance
%patch24 -p1 -b .optimize-recovery
%patch25 -p1 -b .add-timers
%patch26 -p1 -b .set-cipher-suites

%patch30 -p1 -b .set-port-valid
%patch31 -p1 -b .clear-wpa-eapol
%patch32 -p1 -b .clear-driver-pmksa
%patch33 -p1 -b .flush-pmksa
%patch34 -p1 -b .fix-pkc
%patch35 -p1 -b .add-pkc-debug
%patch36 -p1 -b .clear-okc
%patch37 -p1 -b .move-call
%patch38 -p1 -b .pmk-single
%patch39 -p1 -b .never-evict-current
%patch40 -p1 -b .initial-cur-pmksa
%patch41 -p1 -b .granular-deauth
%patch42 -p1 -b .update-current

%patch50 -p1 -b .less-agressive-roaming

%patch51 -p1 -b .dbus-server-cert-info
%patch52 -p1 -b .move-calls-to-notify
%patch53 -p1 -b .write-server-cert
%patch54 -p1 -b .domain-match
%patch55 -p1 -b .cert-in-cb
%patch56 -p1 -b .rh1221178-WMM-fix

%patch57 -p1 -b .rh1254486-dont-qoute-scan_freq-and-freq_list

%patch58 -p1 -b .log-rotate

%patch59 -p1 -b .deauthenticate-on-reconfiguration

%patch60 -p1 -b .rh1495530-0001.patch
%patch61 -p1 -b .rh1495530-0002.patch
%patch62 -p1 -b .rh1495530-0003.patch
%patch63 -p1 -b .rh1495530-0004.patch
%patch64 -p1 -b .rh1495530-0005.patch
%patch65 -p1 -b .rh1495530-0006.patch
%patch66 -p1 -b .rh1495530-0007.patch

%build
pushd wpa_supplicant
  cp %{SOURCE1} .config
  CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
  CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
  make %{_smp_mflags}
%if %{build_gui}
%if %{with_qt4}
  QTDIR=%{_libdir}/qt4 make wpa_gui-qt4 %{_smp_mflags}
%else
  QTDIR=%{_libdir}/qt-3.3 make wpa_gui %{_smp_mflags}
%endif
%endif
popd

%install
rm -rf %{buildroot}

# init scripts
install -D -m 0755 %{SOURCE3} %{buildroot}/%{_sysconfdir}/rc.d/init.d/%{name}
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

# config
install -D -m 0600 %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf

# binary
install -d %{buildroot}/%{_sbindir}
install -m 0755 %{name}/wpa_passphrase %{buildroot}/%{_sbindir}
install -m 0755 %{name}/wpa_cli %{buildroot}/%{_sbindir}
install -m 0755 %{name}/wpa_supplicant %{buildroot}/%{_sbindir}
install -D -m 0644 %{name}/dbus/dbus-wpa_supplicant.conf %{buildroot}/%{_sysconfdir}/dbus-1/system.d/wpa_supplicant.conf
install -D -m 0644 %{name}/dbus/fi.epitest.hostap.WPASupplicant.service %{buildroot}/%{_datadir}/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service

%if %{build_gui}
# gui
install -d %{buildroot}/%{_bindir}
%if %{with_qt4}
install -m 0755 %{name}/wpa_gui-qt4/wpa_gui %{buildroot}/%{_bindir}
%else
install -m 0755 %{name}/wpa_gui/wpa_gui %{buildroot}/%{_bindir}
%endif
%else
rm -f %{name}/doc/docbook/wpa_gui*
%endif

# running
mkdir -p %{buildroot}/%{_localstatedir}/run/%{name}

# man pages
install -d %{buildroot}%{_mandir}/man{5,8}
install -m 0644 %{name}/doc/docbook/*.8 %{buildroot}%{_mandir}/man8
install -m 0644 %{name}/doc/docbook/*.5 %{buildroot}%{_mandir}/man5

# some cleanup in docs and examples
rm -f  %{name}/doc/.cvsignore
rm -rf %{name}/doc/docbook
chmod -R 0644 %{name}/examples/*.py


%clean
rm -rf %{buildroot}

%post
if [ $1 = 1 ]; then
	chkconfig --add %{name}
fi

%preun
if [ $1 = 0 ]; then
	service %{name} stop > /dev/null 2>&1
	killall -TERM wpa_supplicant >/dev/null 2>&1
	/sbin/chkconfig --del %{name}
fi


%files
%defattr(-, root, root)
%doc COPYING %{name}/ChangeLog README %{name}/eap_testing.txt %{name}/todo.txt %{name}/wpa_supplicant.conf %{name}/examples
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/dbus-1/system.d/%{name}.conf
%{_datadir}/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service
%{_sbindir}/wpa_passphrase
%{_sbindir}/wpa_supplicant
%{_sbindir}/wpa_cli
%dir %{_localstatedir}/run/%{name}
%dir %{_sysconfdir}/%{name}
%{_mandir}/man8/*
%{_mandir}/man5/*

%if %{build_gui}
%files gui
%defattr(-, root, root)
%{_bindir}/wpa_gui
%endif

%changelog
* Wed Oct 18 2017 Davide Caratti <dcaratti@redhat.com> - 1:0.7.3-9.2
- Fix backport errors (CVE-2017-13077, CVE-2017-13080)

* Sun Oct 15 2017 Davide Caratti <dcaratti@redhat.com> - 1:0.7.3-9.1
- avoid key reinstallation (CVE-2017-13077, CVE-2017-13078, CVE-2017-13079,
  CVE-2017-13080, CVE-2017-13081, CVE-2017-13082)

* Thu Aug 25 2016 Davide Caratti <dcaratti@redhat.com> - 1:0.7.3-9
- Deauthenticate on reconfiguration (rh #1359044)

* Tue Aug 25 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.7.3-8
- Enable syslog logging support (rh #822128)
- Support run-time rotation the debug log file (rh #908306)
- Fix scriptlet dependencies (rh #712848)
- Enable timestampes in logs (rh #1150004)

* Tue Aug 18 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.7.3-7
- Do not quote value for 'scan_freq' and 'freq_list' (rh #1254486)

* Mon Jun  1 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.7.3-6
- AP WMM: Fix integer underflow in WMM Action frame parser (rh #1221178) (rh #1226396)

* Mon May 18 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.7.3-5
- Add domain_match config option from upstream (rh #1186806) (rh #1178263)
- Include peer certificate in EAP events for use by clients
- Add dbus signal for information about server certification
- eapol_test: Add option for writing server certificate chain to a file

* Thu Sep  6 2012 Dan Williams <dcbw@redhat.com> - 1:0.7.3-4
- Fix issues with Opportunistic/Proactive Key Caching (OKC) (rh #813579)
- Be less aggressive when choosing to roam (rh #837402)
- Don't install manpage for wpa_gui (rh #672976)

* Wed Mar 21 2012 Dan Williams <dcbw@redhat.com> - 1:0.7.3-3
- Fix signal quality reporting via nl80211 for some drivers (rh #752032)

* Tue Nov  1 2011 Dan Williams <dcbw@redhat.com> - 1:0.7.3-2
- Backport upstream SME patches for nl80211 roaming improvements (rh #713280)

* Mon Jul 25 2011 Jiří Klimeš <jklimes@redhat.com> - 1:0.7.3-1
- Update to 0.7.3 - for nl80211 and background scanning (rh #713280)
- Drop upstreamed and backported patches

* Thu May 13 2010 Dan Williams <dcbw@redhat.com> - 1:0.6.8-10
- Remove prereq on chkconfig
- Build GUI with qt4 for rawhide (rh #537105)

* Thu May  6 2010 Dan Williams <dcbw@redhat.com> - 1:0.6.8-9
- Fix crash when interfaces are removed (like suspend/resume) (rh #589507)

* Wed Jan  6 2010 Dan Williams <dcbw@redhat.com> - 1:0.6.8-8
- Fix handling of newer PKCS#12 files (rh #541924)

* Sun Nov 29 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.8-7
- Fix supplicant initscript return value (rh #521807)
- Fix race when connecting to WPA-Enterprise/802.1x-enabled access points (rh #508509)
- Don't double-scan when attempting to associate

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1:0.6.8-6
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.8-4
- Let D-Bus clients know when the supplicant is scanning

* Tue May 12 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.8-3
- Ensure the supplicant starts and ends with clean driver state
- Handle driver disconnect spammage by forcibly clearing SSID
- Don't switch access points unless the current association is dire (rh #493745)

* Tue May 12 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.8-2
- Avoid creating bogus Ad-Hoc networks when forcing the driver to disconnect (rh #497771)

* Mon Mar  9 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.8-1
- Update to latest upstream release

* Wed Feb 25 2009 Colin Walters <walters@verbum.org> - 1:0.6.7-4
- Add patch from upstream to suppress unrequested replies, this
  quiets a dbus warning.

* Fri Feb  6 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.7-3
- Fix scan result retrieval in very dense wifi environments

* Fri Feb  6 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.7-2
- Ensure that drivers don't retry association when they aren't supposed to

* Fri Jan 30 2009 Dan Williams <dcbw@redhat.com> - 1:0.6.7-1
- Fix PEAP connections to Windows Server 2008 authenticators (rh #465022)
- Stop supplicant on uninstall (rh #447843)
- Suppress scan results message in logs (rh #466601)

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 1:0.6.4-3
- rebuild with new openssl

* Wed Oct 15 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.4-2
- Handle encryption keys correctly when switching 802.11 modes (rh #459399)
- Better scanning behavior on resume from suspend/hibernate
- Better interaction with newer kernels and drivers

* Wed Aug 27 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.4-1
- Update to 0.6.4
- Remove 'hostap', 'madwifi', and 'prism54' drivers; use standard 'wext' instead
- Drop upstreamed patches

* Tue Jun 10 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.3-6
- Fix 802.11a frequency bug
- Always schedule specific SSID scans to help find hidden APs
- Properly switch between modes on mac80211 drivers
- Give adhoc connections more time to assocate

* Mon Mar 10 2008 Christopher Aillon <caillon@redhat.com> - 1:0.6.3-5
- BuildRequires qt3-devel

* Sat Mar  8 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.3-4
- Fix log file path in service config file

* Thu Mar  6 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.3-3
- Don't start the supplicant by default when installed (rh #436380)

* Tue Mar  4 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.3-2
- Fix a potential use-after-free in the D-Bus byte array demarshalling code

* Mon Mar  3 2008 Dan Williams <dcbw@redhat.com> - 1:0.6.3-1
- Update to latest development release; remove upstreamed patches

* Fri Feb 22 2008 Dan Williams <dcbw@redhat.com> 1:0.5.7-23
- Fix gcc 4.3 rebuild issues

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.5.7-22
- Autorebuild for GCC 4.3

* Tue Dec 25 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-21
- Backport 'frequency' option for Ad-Hoc network configs

* Mon Dec 24 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-20
- Fix LSB initscript header to ensure 'messagebus' is started first (rh #244029)

* Thu Dec  6 2007 Dan Williams <dcbw@redhat.com> - 1:0.5.7-19
- Fix two leaks when signalling state and scan results (rh #408141)
- Add logrotate config file (rh #404181)
- Add new LSB initscript header to initscript with correct deps (rh #244029)
- Move other runtime arguments to /etc/sysconfig/wpa_supplicant
- Start after messagebus service (rh #385191)
- Fix initscript 'condrestart' command (rh #217281)

* Tue Dec  4 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.5.7-18
- Rebuild against new openssl

* Tue Dec  4 2007 Ville Skyttä <ville.skytta at iki.fi> - 1:0.5.7-17
- Group: Application/System -> Applications/System in -gui.

* Tue Nov 13 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-16
- Add IW_ENCODE_TEMP patch for airo driver and Dynamic WEP
- Fix error in wpa_supplicant-0.5.7-ignore-dup-ca-cert-addition.patch that
    caused the last error to not be printed
- Fix wpa_supplicant-0.5.7-ignore-dup-ca-cert-addition.patch to ignore
    duplicate cert additions for all certs and keys
- Change license to BSD due to linkage against OpenSSL since there is no
    OpenSSL exception in the GPLv2 license text that upstream ships

* Sun Oct 28 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-15
- Fix Dynamic WEP associations with mac80211-based drivers

* Sun Oct 28 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-14
- Don't error an association on duplicate CA cert additions

* Wed Oct 24 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-13
- Correctly set the length of blobs added via the D-Bus interface

* Wed Oct 24 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-12
- Fix conversion of byte arrays to strings by ensuring the buffer is NULL
    terminated after conversion

* Sat Oct 20 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-11
- Add BLOB support to the D-Bus interface
- Fix D-Bus interface permissions so that only root can use the wpa_supplicant
    D-Bus interface

* Tue Oct  9 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-10
- Don't segfault with dbus control interface enabled and invalid network
    interface (rh #310531)

* Tue Sep 25 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-9
- Always allow explicit wireless scans triggered from a control interface

* Thu Sep 20 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-8
- Change system bus activation file name to work around D-Bus bug that fails
    to launch services unless their .service file is named the same as the
    service itself

* Fri Aug 24 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-7
- Make SIGUSR1 change debug level on-the-fly; useful in combination with
    the -f switch to log output to /var/log/wpa_supplicant.log
- Stop stripping binaries on install so we get debuginfo packages
- Remove service start requirement for interfaces & devices from sysconfig file,
    since wpa_supplicant's D-Bus interface is now turned on

* Fri Aug 17 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-6
- Fix compilation with RPM_OPT_FLAGS (rh #249951)
- Make debug output to logfile a runtime option

* Fri Aug 17 2007 Christopher Aillon <caillon@redhat.com> - 0.5.7-5
- Update the license tag

* Tue Jun 19 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-4
- Fix initscripts to use -Dwext by default, be more verbose on startup
    (rh #244511)

* Mon Jun  4 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-3
- Fix buffer overflow by removing syslog patch (#rh242455)

* Mon Apr  9 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-2
- Add patch to send output to syslog

* Thu Mar 15 2007 Dan Williams <dcbw@redhat.com> - 0.5.7-1
- Update to 0.5.7 stable release

* Fri Oct 27 2006 Dan Williams <dcbw@redhat.com> - 0.4.9-1
- Update to 0.4.9 for WE-21 fixes, remove upstreamed patches
- Don't package doc/ because they aren't actually wpa_supplicant user documentation,
    and becuase it pulls in perl

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.4.8-10.1
- rebuild

* Thu Apr 27 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-10
- Add fix for madwifi and WEP (wpa_supplicant/hostap bud #140) (#rh190075#)
- Fix up madwifi-ng private ioctl()s for r1331 and later
- Update madwifi headers to r1475

* Tue Apr 25 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-9
- Enable Wired driver, PKCS12, and Smartcard options (#rh189805#)

* Tue Apr 11 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-8
- Fix control interface key obfuscation a bit

* Sun Apr  2 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-7
- Work around older & incorrect drivers that return null-terminated SSIDs

* Mon Mar 27 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-6
- Add patch to make orinoco happy with WEP keys
- Enable Prism54-specific driver
- Disable ipw-specific driver; ipw2x00 should be using WEXT instead

* Fri Mar  3 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-5
- Increase association timeout, mainly for drivers that don't
	fully support WPA ioctls yet

* Fri Mar  3 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-4
- Add additional BuildRequires #rh181914#
- Add prereq on chkconfig #rh182905# #rh182906#
- Own /var/run/wpa_supplicant and /etc/wpa_supplicant #rh183696#

* Wed Mar  1 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-3
- Install wpa_passphrase too #rh183480#

* Mon Feb 27 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-2
- Don't expose private data on the control interface unless requested

* Fri Feb 24 2006 Dan Williams <dcbw@redhat.com> - 0.4.8-1
- Downgrade to 0.4.8 stable release rather than a dev release

* Sun Feb 12 2006 Dan Williams <dcbw@redhat.com> - 0.5.1-3
- Documentation cleanup (Terje Rosten <terje.rosten@ntnu.no>)

* Sun Feb 12 2006 Dan Williams <dcbw@redhat.com> - 0.5.1-2
- Move initscript to /etc/rc.d/init.d

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb  5 2006 Dan Williams <dcbw@redhat.com> 0.5.1-1
- Update to 0.5.1
- Add WE auth fallback to actually work with older drivers

* Thu Jan 26 2006 Dan Williams <dcbw@redhat.com> 0.4.7-2
- Bring package into Fedora Core
- Add ap_scan control interface patch
- Enable madwifi-ng driver

* Sun Jan 15 2006 Douglas E. Warner <silfreed@silfreed.net> 0.4.7-1
- upgrade to 0.4.7
- added package w/ wpa_gui in it

* Mon Nov 14 2005 Douglas E. Warner <silfreed@silfreed.net> 0.4.6-1
- upgrade to 0.4.6
- adding ctrl interface changes recommended 
  by Hugo Paredes <hugo.paredes@e-know.org>

* Sun Oct  9 2005 Douglas E. Warner <silfreed@silfreed.net> 0.4.5-1
- upgrade to 0.4.5
- updated config file wpa_supplicant is built with
  especially, the ipw2100 driver changed to just ipw
  and enabled a bunch more EAP
- disabled dist tag

* Thu Jun 30 2005 Douglas E. Warner <silfreed@silfreed.net> 0.4.2-3
- fix typo in init script

* Thu Jun 30 2005 Douglas E. Warner <silfreed@silfreed.net> 0.4.2-2
- fixing init script using fedora-extras' template
- removing chkconfig default startup

* Tue Jun 21 2005 Douglas E. Warner <silfreed@silfreed.net> 0.4.2-1
- upgrade to 0.4.2
- new sample conf file that will use any unrestricted AP
- make sysconfig config entry
- new BuildRoot for Fedora Extras
- adding dist tag to Release

* Fri May 06 2005 Douglas E. Warner <silfreed@silfreed.net> 0.3.8-1
- upgrade to 0.3.8

* Thu Feb 10 2005 Douglas E. Warner <silfreed@silfreed.net> 0.3.6-2
- compile ipw driver in

* Wed Feb 09 2005 Douglas E. Warner <silfreed@silfreed.net> 0.3.6-1
- upgrade to 0.3.6

* Thu Dec 23 2004 Douglas E. Warner <silfreed@silfreed.net> 0.2.5-4
- fixing init script

* Mon Dec 20 2004 Douglas E. Warner <silfreed@silfreed.net> 0.2.5-3
- fixing init script
- adding post/preun items to add/remove via chkconfig

* Mon Dec 20 2004 Douglas E. Warner <silfreed@silfreed.net> 0.2.5-2
- adding sysV scripts

* Mon Dec 20 2004 Douglas E. Warner <silfreed@silfreed.net> 0.2.5-1
- Initial RPM release.

