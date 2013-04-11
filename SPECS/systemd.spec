%define libdaemon_major 0
%define liblogin_major 0
%define libjournal_major 0
%define libid128_major 0
%define libudev_major 1
%define libgudev_api 1.0
%define libgudev_major 0

%define libdaemon %mklibname systemd-daemon %{libdaemon_major}
%define liblogin %mklibname systemd-login %{liblogin_major}
%define libjournal %mklibname systemd-journal %{libjournal_major}
%define libid128 %mklibname systemd-id 128 %{libid128_major}

%define libudev %mklibname udev %{libudev_major}
%define libudev_devel %mklibname -d udev

%define libgudev %mklibname gudev %{libgudev_api} %{libgudev_major}
%define libgudev_devel %mklibname -d gudev %{libgudev_api}
%define libgudev_gir %mklibname gudev-gir %{libgudev_api}

Summary:	A System and Session Manager
Name:		systemd
Version:	195
Release:	%mkrel 20
License:	GPLv2+
Group:		System/Boot and Init
Url:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz

Source10: 50-udev-mageia.rules
Source11: 69-printeracl.rules
# (hk) udev rules for zte 3g modems with drakx-net
Source12: 61-mobile-zte-drakx-net.rules

# (blino) net rules and helpers
Source20: 76-net.rules
Source21: udev_net_create_ifcfg
Source22: udev_net_action
Source23: udev_net.sysconfig

# (cg) Upstream cherry picks
Patch100: 0100-rules-Remove-HP-iLO-from-USB-HID-PM-rules.patch
Patch101: 0101-job-avoid-recursion-into-transaction-code-from-job-c.patch
Patch102: 0102-sysctl-parse-all-keys-in-a-config-file.patch
Patch103: 0103-journal-fix-parsing-of-monotonic-kernel-timestamps.patch
Patch104: 0104-hwclock-do-not-seal-the-kernel-s-time-warp-call-from.patch
Patch105: 0105-units-agetty-overrides-TERM.patch
Patch106: 0106-shared-libsystemd-daemon-check-for-empty-strings-in-.patch
Patch107: 0107-shared-core-do-not-always-accept-numbers-in-string-l.patch
Patch108: 0108-shared-max-in-the-string-number-conversion-is-meant-.patch
Patch109: 0109-strv-cleanup-error-path-loops.patch
Patch110: 0110-build-sys-store-journald-code-in-a-noinst-library.patch
Patch111: 0111-dbus-manager-fix-a-fatal-dbus-abort-in-bus_manager_m.patch
Patch112: 0112-shutdown-readd-explicit-sync-when-shutting-down.patch
Patch113: 0113-switch-root-try-pivot_root-before-overmounting.patch
Patch114: 0114-umount-always-remount-read-only-before-unmounting-in.patch
Patch115: 0115-shared-utils-systemd-cgls-shows-n-a-when-piping-outp.patch
Patch116: 0116-core-load-fragment-fix-potential-bad-memory-access.patch
Patch117: 0117-journald-fix-bad-memory-access.patch
Patch118: 0118-journal-send-always-send-SYSLOG_IDENTIFIER-if-we-hav.patch
Patch119: 0119-localectl-fix-dbus-call-arguments-in-set_x11_keymap.patch
Patch120: 0120-add-Belarussian-mapping-simple-by-and-by.patch
Patch121: 0121-French-Canadian-xlayout-is-just-ca-not-ca-fr-any-mor.patch
Patch122: 0122-add-Hebrew-Israel-simple-il-il.patch
Patch123: 0123-add-Kazakh-keyboard-mapping-kazakh-kz.patch
Patch124: 0124-add-Lithuanian-keyboard-mapping-lt-lt.patch
Patch125: 0125-correct-Macedonian-keyboard-mapping-X-layout-is-mk-n.patch
Patch126: 0126-configure.ac-fix-FTBFS-with-new-glibc.patch
Patch127: 0127-tmpfiles-allow-Age-to-be-set-to-0.patch
Patch128: 0128-tmpfiles-Fix-file-descriptor-leak-on-error.patch
Patch129: 0129-tmpfiles-introduce-type-X.patch
Patch130: 0130-tmpfiles-exclude-tmp-systemd-private-from-cleanup.patch
Patch131: 0131-tmpfiles-exclude-var-tmp-systemd-private-too.patch
Patch132: 0132-man-mention-that-PrivateTmp-means-var-tmp-too.patch
Patch133: 0133-service-properly-signal-permanent-failure-of-a-servi.patch
Patch134: 0134-pam-properly-handle-SSH-logins-lacking-the-PAM-tty-f.patch
Patch135: 0135-pam_systemd-new-option-for-the-session-class.patch
Patch136: 0136-logind-it-s-OK-if-a-process-on-an-pty-requests-a-ses.patch
Patch137: 0137-systemd-mount-the-EFI-variable-filesystem.patch
Patch138: 0138-shutdown-don-t-consider-umounting-of-and-usr-failed.patch
Patch139: 0139-readahead-properly-detect-btrfs-on-SSD.patch
Patch140: 0140-timedated-do-not-incorrectly-close-non-opened-dbus-c.patch
Patch141: 0141-journalctl-remove-left-over-log-message.patch
Patch142: 0142-journal-properly-determine-cutoff-max-date.patch
Patch143: 0143-units-reword-rescue-mode-hints.patch
Patch144: 0144-util-fix-possible-integer-overflows.patch
Patch145: 0145-swap-fix-swap-behaviour-with-symlinks.patch
Patch146: 0146-hostnamectl-do-not-choke-on-set-hostname-with-no-arg.patch
Patch147: 0147-cryptsetup-hash-plain-means-don-t-use-a-hash.patch
Patch148: 0148-fstab-generator-more-specific-error-messages.patch
Patch149: 0149-delta.c-fix-option-t.patch
Patch150: 0150-systemd-highlight-ordering-cycle-deletions.patch
Patch151: 0151-core-interpret-token-in-ExecStart-as-escaped.patch
Patch152: 0152-hostnamectl-fix-parsing-of-no-ask-password.patch
Patch153: 0153-core-load-fragment-be-more-precise-in-error-messages.patch
Patch154: 0154-socket-improve-error-message-when-we-cannot-spawn-th.patch
Patch155: 0155-cryptsetup-fix-nofail-support.patch
Patch156: 0156-cryptsetup-generator-state-file-name-in-error-messag.patch
Patch157: 0157-fstab-generator-make-error-more-helpful-in-case-of-d.patch
Patch158: 0158-systemctl-verbose-message-on-missing-Install.patch
Patch159: 0159-shutdown-downgrade-a-warning.patch
Patch160: 0160-path-util-set-pointer-to-null-after-calling-free.patch
Patch161: 0161-coredumpctl-check-return-of-strndup.patch
Patch162: 0162-socket-Too-many-incoming-connections.patch
Patch163: 0163-fstab-generator-properly-detect-bind-mounts.patch
Patch164: 0164-localectl-support-systems-without-locale-archive.patch
Patch165: 0165-logind-Capability-of-making-seats-without-framebuffe.patch
Patch166: 0166-service-for-Type-forking-services-ignore-exit-status.patch
Patch167: 0167-logind-ignore-non-tty-non-x11-session-when-checking-.patch
Patch168: 0168-journalctl-quit-on-I-O-error.patch
Patch169: 0169-core-do-not-make-sockets-dependent-on-lo.patch
Patch170: 0170-umount-fix-check-for-DM-changed.patch
Patch171: 0171-shutdown-umount-logging-improvements.patch
Patch172: 0172-shutdown-umount-use-verbs-consistently.patch
Patch173: 0173-shutdown-in-the-final-umount-loop-don-t-use-MNT_FORC.patch
Patch174: 0174-shutdown-ignore-loop-devices-without-a-backing-file.patch
Patch175: 0175-util-fix-bad-memory-access.patch
Patch176: 0176-util-continuation-support-for-load_env_file.patch
Patch177: 0177-tmpfiles-introduce-type-X.patch
Patch178: 0178-job-fix-merging-with-ignore-dependencies.patch
Patch179: 0179-journalctl-require-argument-for-priority.patch
Patch180: 0180-cryptsetup-accept-both-read-only-and-readonly-spelli.patch
Patch181: 0181-shutdown-issue-a-sync-as-soon-as-shutdown.target-is-.patch
Patch182: 0182-systemctl-print-wall-message-only-if-successful.patch
Patch183: 0183-journal-introduce-entry-array-chain-cache.patch
Patch184: 0184-completion-fix-typo-in-accessing-array-index.patch
Patch185: 0185-bash-completion-add-minimal-udevadm-support.patch
Patch186: 0186-bash-completion-avoid-usage-of-ls-for-listing-device.patch
Patch187: 0187-logind-support-for-hybrid-sleep-i.e.-suspend-hiberna.patch
Patch188: 0188-fstab-mount-detect-rbind-as-bind-mount.patch
Patch189: 0189-udev-path_id-handle-Hyper-V-devices.patch
Patch190: 0190-keymap-Update-the-list-of-Samsung-Series-9-models.patch
Patch191: 0191-keymap-Add-Samsung-700T.patch
Patch192: 0192-libudev-avoid-leak-during-realloc-failure.patch
Patch193: 0193-libudev-do-not-resolve-attr-device-symlinks.patch
Patch194: 0194-libudev-validate-udev-argument-to-udev_enumerate_new.patch
Patch195: 0195-udev-fix-whitespace.patch
# (cg) The following patch causes Floating point exceptions... (mga#9689)
#Patch196: 0196-udev-use-usec_t-and-now.patch
# (cg) And this patch depends on the above...
#Patch197: 0197-udev-properly-handle-symlink-removal-by-change-event.patch
Patch198: 0198-keymap-Add-HP-EliteBook-8440p.patch
Patch199: 0199-keymap-Add-HP-HDX-9494NR.patch
Patch200: 0200-keymap-Add-HP-HDX-9494NR-Fix-touchpad-keys.patch
Patch201: 0201-udev-Fix-device-matching-in-the-accelerometer.patch
Patch202: 0202-udev-usb_id-ignore-non-ASCII-serial-numbers.patch
Patch203: 0203-udev-usb_id-parse-only-size-bytes-of-the-descriptors.patch
Patch204: 0204-cdrom_id-add-data-track-count-for-bad-virtual-drive-.patch
Patch205: 0205-udev-expose-new-ISO9660-properties-from-libblkid.patch
Patch206: 0206-shared-add-is_efiboot.patch
Patch207: 0207-kmod-setup-add-conditional-module-loading-callback.patch
Patch208: 0208-kmod-setup-mounting-efivarfs-after-we-tried-to-mount.patch
Patch209: 0209-mount-setup-try-mounting-efivarfs-only-if-the-system.patch
Patch210: 0210-udevd-add-missing-to-getopt_long-e.patch
Patch211: 0211-udev-builtin-do-not-fail-builtin-initialization-if-o.patch
Patch212: 0212-udev-use-unique-names-for-temporary-files-created-in.patch
Patch213: 0213-cryptsetup-fix-inverted-comparison-in-pass_volume_ke.patch
Patch214: 0214-journal-special-case-the-trivial-cache-chain-cache-e.patch

# (cg/bor) clean up directories on boot as done by rc.sysinit
# - Lennart should be poked about this (he couldn't think why he hadn't done it already)
Patch500: 0500-Clean-directories-that-were-cleaned-up-by-rc.sysinit.patch
Patch501: 0501-Some-more-tmpfiles-fixes.patch
Patch502: 0502-main-Add-failsafe-to-the-sysvinit-compat-cmdline-key.patch
Patch503: 0503-mageia-Fallback-message-when-display-manager-fails.patch
Patch504: 0504-Disable-modprobe-pci-devices-on-coldplug-for-storage.patch
Patch505: 0505-Allow-booting-from-live-cd-in-virtualbox.patch
Patch506: 0506-reinstate-TIMEOUT-handling.patch
Patch507: 0507-udev-Allow-the-udevadm-settle-timeout-to-be-set-via-.patch
Patch508: 0508-Mageia-Relax-perms-on-sys-kernel-debug-for-lspcidrak.patch
Patch509: 0509-udev-rules-Apply-SuSE-patch-to-restore-cdrom-cdrw-dv.patch

# (cjw) revert commit 97595710b77aa162ca5e20da57d0a1ed7355eaad that breaks network interface renaming
# (cg) This is done for mga3, but will be removed for mga4 when we will switch
# to a different naming scheme for network interfaces which should prevent the
# need for a racy an confusing (from a user perspective) feature.
# https://wiki.mageia.org/en/Feature:NetworkDeviceNameChange
Patch700: systemd-188-udev-network-interface-renaming.patch
Source50: 75-persistent-net-generator.rules
Source51: rule_generator.functions
Source52: write_net_rules

BuildRequires:	dbus-devel >= 1.4.0
BuildRequires:	libcap-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	pam-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	vala >= 0.9
BuildRequires:	glib2-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	gperf
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	cryptsetup-devel
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	python-devel
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(liblzma)
Requires(pre):	filesystem >= 2.1.9-18
Requires:	systemd-units = %{version}-%{release}
Requires:	dbus >= 1.3.2
Requires:	initscripts >= 9.21-3
Requires:	util-linux-ng >= 2.18
Requires:	nss-myhostname
Requires:	lockdev
Conflicts:	initscripts < 9.25
Provides:	should-restart = system
Provides: udev = %{version}-%{release}
Obsoletes: udev < 185
Provides:  systemd-sysvinit = %{version}-%{release}
Conflicts: systemd-sysvinit < 185
Obsoletes: systemd-sysvinit < 185
Provides:  sysvinit = 2.87-22
Obsoletes: sysvinit < 2.87-22
Conflicts: SysVinit
# Due to halt/poweroff etc. in _bindir
Conflicts: usermode-consoleonly < 1:1.110
Provides:  system-logger
# (blino) consolekit has been replaced by systemd-logind
Obsoletes: consolekit
Obsoletes: consolekit-x11
Obsoletes: libconsolekit0
Obsoletes: lib64consolekit0

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

# (TV) basically split b/c it pulls python in basesystem
%package tools
Summary:	Non essential systemd tools
Group:		System/Boot and Init
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus
Requires:	python-cairo
Conflicts:	%{name} <= 37-15

%description tools
Non essential systemd tools

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		System/Boot and Init
Requires(pre):	filesystem >= 2.1.9-18
Requires:	%{name} = %{version}-%{release}
Conflicts:	initscripts < 9.25
Requires(post): coreutils grep awk

%description units
Basic configuration files, directories and installation tool for the systemd
system and session manager.

%package -n python-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Python

%description -n python-%{name}
Python bindings for %{name}

%package devel
Summary:       Systemd development files
Group:         Development/C
Conflicts:     %{name} <= 35-4
Requires:      %{libdaemon} = %{version}-%{release}
Requires:      %{liblogin} = %{version}-%{release}
Requires:      %{libjournal} = %{version}-%{release}
Requires:      %{libid128} = %{version}-%{release}
# (cg) Obsolete the old, versioned/split devel packages
Provides:      libsystemd-daemon-devel = %{version}-%{release}
Provides:      %{mklibname -d systemd-daemon 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-daemon 0} < 185
Provides:      %{mklibname -d systemd-daemon} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-daemon} < 186
Provides:      libsystemd-login-devel = %{version}-%{release}
Provides:      %{mklibname -d systemd-login 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-login 0} < 185
Provides:      %{mklibname -d systemd-login} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-login} < 186
Provides:      libsystemd-journal-devel = %{version}-%{release}
Provides:      %{mklibname -d systemd-journal 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-journal 0} < 185
Provides:      %{mklibname -d systemd-journal} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-journal} < 186
Provides:      libsystemd-id128-devel = %{version}-%{release}
Provides:      %{mklibname -d systemd-id128 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-id128 0} < 185
Provides:      %{mklibname -d systemd-id128} = %{version}-%{release}
Obsoletes:     %{mklibname -d systemd-id128} < 186

%description devel
This package provides the development files for systemd.

%package -n %{libdaemon}
Summary:       Systemd-daemon library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18
Provides:      libsystemd-daemon = %{version}-%{release}

%description -n %{libdaemon}
This package provides the systemd-daemon shared library.

%package -n %{liblogin}
Summary:       Systemd-login library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18
Provides:      libsystemd-login = %{version}-%{release}

%description -n %{liblogin}
This package provides the systemd-login shared library.

%package -n %{libjournal}
Summary:       Systemd-journal library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18
Provides:      libsystemd-journal = %{version}-%{release}

%description -n %{libjournal}
This package provides the systemd-journal shared library.

%package -n %{libid128}
Summary:       Systemd-id128 library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18
Provides:      libsystemd-id128 = %{version}-%{release}
Obsoletes:     %{_lib}systemd-id1280 < 187-5

%description -n %{libid128}
This package provides the systemd-id128 shared library.

%package -n %{libudev}
Summary:       udev library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18

%description -n %{libudev}
This package provides the udev shared library.

%package -n %{libudev_devel}
Summary:       udev library development files
Group:         Development/C
Requires:      %{libudev} = %{version}-%{release}
Provides:      udev-devel = %{version}-%{release}
Provides:      libudev-devel = %{version}-%{release}
# (cg) Obsolete the old, versioned devel package
Provides:      %{mklibname -d udev 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d udev 0} < 185

%description -n %{libudev_devel}
This package provides the development files for the udev shared library.

%package -n %{libgudev}
Summary:       gudev library package
Group:         System/Libraries
Requires(pre): filesystem >= 2.1.9-18
Provides:      libgudev = %{version}-%{release}

%description -n %{libgudev}
This package provides the gudev shared library.

%package -n %{libgudev_gir}
Summary:       GObject Introspection interface description for GUdev
Group:         System/Libraries
Requires:      %{libgudev} = %{version}-%{release}
Conflicts:     %{_lib}gudev1.0_0 < 187-5

%description -n %{libgudev_gir}
GObject Introspection interface description for GUdev.


%package -n %{libgudev_devel}
Summary:       gudev library development files
Group:         Development/C
Requires:      %{libgudev} = %{version}-%{release}
Provides:      libgudev-devel = %{version}-%{release}
# (cg) Obsolete the old, versioned devel package
Provides:      %{mklibname -d gudev 0} = %{version}-%{release}
Obsoletes:     %{mklibname -d gudev 0} < 185

%description -n %{libgudev_devel}
This package provides the development files for the gudev shared library.


%prep
%setup -q
%apply_patches
find src/ -name "*.vala" -exec touch '{}' \;

%build
autoreconf --force --install --verbose
%configure2_5x \
  --with-distro=mageia \
  --disable-static \
  --disable-selinux \
  --with-firmware-path=%{_prefix}/lib/firmware/updates:%{_prefix}/lib/firmware \
  --with-usb-ids-path=/usr/share/usb.ids \
  --with-pci-ids-path=/usr/share/pci.ids

%make

%install
rm -rf %{buildroot}

%makeinstall_std
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# (cg) Create and ship folder to hold user rules
install -d -m 755 %{buildroot}%{_sysconfdir}/udev/rules.d

install -m 644 %SOURCE10 %{buildroot}%{_prefix}/lib/udev/rules.d/
install -m 644 %SOURCE11 %{buildroot}%{_prefix}/lib/udev/rules.d/
# udev rules for zte 3g modems and drakx-net
install -m 0644 %SOURCE12 %{buildroot}%{_prefix}/lib/udev/rules.d/

# net rules
install -m 0644 %SOURCE20 %{buildroot}%{_prefix}/lib/udev/rules.d/
install -m 0755 %SOURCE21 %{buildroot}%{_prefix}/lib/udev/net_create_ifcfg
install -m 0755 %SOURCE22 %{buildroot}%{_prefix}/lib/udev/net_action
install -m 0755 -d %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %SOURCE23 %{buildroot}%{_sysconfdir}/sysconfig/udev_net


# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}{%{_bindir},%{_sbindir}}
ln -s ../lib/systemd/systemd %{buildroot}%{_bindir}/systemd
ln -s ../lib/systemd/systemd %{buildroot}%{_sbindir}/init
ln -s ../bin/systemctl %{buildroot}%{_bindir}/reboot
ln -s ../bin/systemctl %{buildroot}%{_bindir}/halt
ln -s ../bin/systemctl %{buildroot}%{_bindir}/poweroff
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/shutdown
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/telinit
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/runlevel

# Also add a symlink for udevadm for now as lots of things use an absolute path
ln -s ../bin/udevadm %{buildroot}%{_sbindir}/udevadm

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants

# (cg) To avoid making life hard for developers, don't package the
# kernel.core_pattern setting until systemd-coredump is a part of an actual
# systemd release and it's made clear how to get the core dumps out of the
# journal.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/coredump.conf

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/syslog.target.wants

# And the default symlink we generate automatically based on inittab
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# (bor) make sure we own directory for bluez to install service
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/bluetooth.target.wants

# use consistent naming and permissions for completion scriplets
mv %{buildroot}%{_sysconfdir}/bash_completion.d/systemd-bash-completion.sh \
  %{buildroot}%{_sysconfdir}/bash_completion.d/systemd
chmod 644 %{buildroot}%{_sysconfdir}/bash_completion.d/systemd

# (cg) Set up the pager to make it generally more useful
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/40systemd.sh << EOF
export SYSTEMD_PAGER="/usr/bin/less -FR"
EOF
chmod 644 %{buildroot}%{_sysconfdir}/profile.d/40systemd.sh

# (bor) enable rpcbind.target by default so we have something to plug
# portmapper service into
ln -s ../rpcbind.target %{buildroot}%{_prefix}/lib/systemd/system/multi-user.target.wants

# create modules.conf as a symlink to /etc/
ln -s /etc/modules %{buildroot}%{_sysconfdir}/modules-load.d/modules.conf

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/timezone
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Make sure the NTP units dir exists
mkdir -p %{buildroot}%{_prefix}/lib/systemd/ntp-units.d/

# (cg) Make the journal's persistent in order to provide a real syslog implementation
install -m 0755 -d %{buildroot}%{_logdir}/journal

# automatic systemd release on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
# (cg) I'm not sure if the file list check works against the packaged rpm
#      or what is installed, so I've added both the /lib and /usr/lib paths
#      below, even thought the former is just a symlink to the latter
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.filter << EOF
^./usr/lib/systemd/system/
^./lib/systemd/system/
^./etc/systemd/system/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.script << EOF
#!/bin/sh
if %{_bindir}/mountpoint -q /sys/fs/cgroup/systemd; then
  if [ -x %{_bindir}/systemctl ]; then
  %{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :
  fi
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.script

# This file is already in sytemd-ui rpm
rm -fr %buildroot%_mandir/man1/systemadm.*

# (cg) This should be moving at some point upstream so pre-empt it
mv %{buildroot}%{_sysconfdir}/rpm %{buildroot}%{_prefix}/lib

# (cg) This restores the horrible network name generator.
# See comment above for why this sucks and why it will be removed in mga4
install -p -m 0644 %{SOURCE50} %{buildroot}%{_prefix}/lib/udev/rules.d/
install -p -m 0644 %{SOURCE51} %{buildroot}%{_prefix}/lib/udev/
install -p -m 0755 %{SOURCE52} %{buildroot}%{_prefix}/lib/udev/

%triggerin -- glibc
# reexec daemon on self or glibc update to avoid busy / on shutdown
# trigger is executed on both self and target install so no need to have
# extra own post
if [ $1 -ge 2 -o $2 -ge 2 ] ; then
	%{_bindir}/systemctl daemon-reexec 2>&1 || :
fi

%post
%{_bindir}/systemd-machine-id-setup > /dev/null 2>&1 || :
#%{_bindir}/systemctl daemon-reexec > /dev/null 2>&1 || :

%triggerin units -- %{name}-units < 35-1
# Enable the services we install by default.
        %{_bindir}/systemctl --quiet enable \
                hwclock-load.service \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :
# rc-local is now enabled by default in base package
rm -f %_sysconfdir/systemd/system/multi-user.target.wants/rc-local.service || :

# (blino) systemd 195 changed the prototype of logind's OpenSession()
# see http://lists.freedesktop.org/archives/systemd-devel/2012-October/006969.html
# and http://cgit.freedesktop.org/systemd/systemd/commit/?id=770858811930c0658b189d980159ea1ac5663467
%triggerun -- %{name} < 195-4.mga3
%{_bindir}/systemctl restart systemd-logind.service

%post units
if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(%{_bindir}/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="%{_prefix}/lib/systemd/system/multi-user.target"
        else
                target="%{_prefix}/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        %{_bindir}/ln -sf "$target" %{_sysconfdir}/systemd/system/default.target 2>&1 || :

        # Enable the services we install by default.
        %{_bindir}/systemctl --quiet enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :
fi

hostname_new=`cat %_sysconfdir/hostname 2>/dev/null`
if [ -z $hostname_new ]; then
        hostname_old=`cat /etc/sysconfig/network 2>/dev/null | grep HOSTNAME | cut -d "=" -f2`
        if [ ! -z $hostname_old ]; then
                echo $hostname_old >> %_sysconfdir/hostname
        else
                echo "localhost" >> %_sysconfdir/hostname
        fi
fi


%preun units
if [ $1 -eq 0 ] ; then
        %{_bindir}/systemctl --quiet disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :

        %{_bindir}/rm -f %_sysconfdir/systemd/system/default.target 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        %{_bindir}/systemctl daemon-reload 2>&1 || :
fi

%files
# (cg) Note some of these directories are empty, but that is intended
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/system-generators
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/systemd/system-sleep
%dir %{_prefix}/lib/systemd/ntp-units.d
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.*
%config(noreplace) %{_sysconfdir}/sysconfig/udev_net
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%{_sysconfdir}/xdg/systemd
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%ghost %config(noreplace) %{_sysconfdir}/timezone
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
# (cg) NB dbus policy files are not really config that users are expected to
# edit manually and thus should NOT be marked as config(noreplace).
# This should really be fixed in upstream dbus (work in progress)
# to separate these policy files from /etc and ship them in /usr instead
# but allow override by admins by copying to /etc.
# There are security implications here (CVE's have been issued due to mistakes
# in these type of files)
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%dir %{_sysconfdir}/udev/rules.d
#%{_prefix}/lib/sysctl.d/coredump.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_bindir}/hostnamectl
%{_bindir}/journalctl
%{_bindir}/localectl
%{_bindir}/loginctl
%{_bindir}/systemd
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-coredumpctl
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-notify
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/timedatectl
%{_bindir}/reboot
%{_bindir}/halt
%{_bindir}/poweroff
%{_sbindir}/shutdown
%{_sbindir}/init
%{_sbindir}/telinit
%{_sbindir}/runlevel
%{_sbindir}/udevadm
%{_prefix}/lib/systemd/systemd*
%{_prefix}/lib/systemd/system-generators/systemd-*
%{_prefix}/lib/udev
%{_libdir}/security/pam_systemd.so
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/udevadm
%dir %{_datadir}/systemd
%{_datadir}/systemd/kbd-model-map
%dir %{_datadir}/systemd/gatewayd
%{_datadir}/systemd/gatewayd/browse.html
%{_mandir}/man1/hostnamectl.*
%{_mandir}/man1/journalctl.*
%{_mandir}/man1/localectl.*
%{_mandir}/man1/loginctl.*
%{_mandir}/man1/systemd.*
%{_mandir}/man1/systemd-*
%{_mandir}/man1/timedatectl.*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/pam_systemd.*
%{_mandir}/man8/systemd-*
%{_mandir}/man8/udevadm.*
%{_mandir}/man1/init.*
%{_mandir}/man8/halt.*
%{_mandir}/man8/reboot.*
%{_mandir}/man8/shutdown.*
%{_mandir}/man8/poweroff.*
%{_mandir}/man8/telinit.*
%{_mandir}/man8/runlevel.*
%{_initrddir}/README
%{_logdir}/README
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Automount.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Job.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Mount.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Path.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Service.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Snapshot.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Socket.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Swap.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Target.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Timer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.Unit.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_docdir}/systemd
%dir %{_logdir}/journal

%files tools
%defattr(-,root,root)
%{_bindir}/systemd-analyze

%files units
%defattr(-,root,root)
# (cg) Note some of these directories are empty, but that is intended
# NB I'm not totally sure of the ownership split of directories between systemd and systemd-units.
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/bash_completion.d
%{_bindir}/systemctl
%{_sysconfdir}/bash_completion.d/systemd
%{_sysconfdir}/profile.d/40systemd.sh
%{_sysconfdir}/modules-load.d/*.conf
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%{_mandir}/man1/systemctl.*

%files -n python-%{name}
%defattr(-,root,root)
%{py_platsitedir}/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/systemd
%{_libdir}/libsystemd-*.so
%{_libdir}/pkgconfig/libsystemd-*.pc
%{_datadir}/pkgconfig/systemd.pc
%{_prefix}/lib/rpm/macros.systemd

%files -n %{libdaemon}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-daemon.so.%{libdaemon_major}*

%files -n %{liblogin}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-login.so.%{liblogin_major}*

%files -n %{libjournal}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-journal.so.%{libjournal_major}*

%files -n %{libid128}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-id128.so.%{libid128_major}*

%files -n %{libudev}
%defattr(-,root,root,-)
%{_libdir}/libudev.so.%{libudev_major}*

%files -n %{libudev_devel}
%defattr(-,root,root,-)
%{_libdir}/libudev.so
%{_includedir}/libudev.h
%{_datadir}/pkgconfig/udev.pc
%{_libdir}/pkgconfig/libudev.pc

%files -n %{libgudev}
%defattr(-,root,root,-)
%{_libdir}/libgudev-%{libgudev_api}.so.%{libgudev_major}*

%files -n %{libgudev_gir}
%{_libdir}/girepository-1.0/GUdev-%{libgudev_api}.typelib

%files -n %{libgudev_devel}
%defattr(-,root,root,-)
%{_libdir}/libgudev-%{libgudev_api}.so
%{_includedir}/gudev-%{libgudev_api}
%{_libdir}/pkgconfig/gudev-%{libgudev_api}.pc
%{_datadir}/gir-1.0/GUdev-%{libgudev_api}.gir
