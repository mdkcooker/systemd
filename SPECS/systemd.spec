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
Version:	204
Release:	%mkrel 2
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
Patch100: 0100-systemctl-does-not-expand-u-so-revert-back-to-I.patch
Patch101: 0101-Start-ctrl-alt-del.target-irreversibly.patch
Patch102: 0102-keymap-Add-support-for-Eject-button-on-MSI-GE60-GE70.patch
Patch103: 0103-sd-journal-check-if-the-pointers-passed-are-the-same.patch
Patch104: 0104-journalctl-add-k-dmesg.patch
Patch105: 0105-units-rework-systemd-random-seed-load-save-.service-.patch
Patch106: 0106-utmp-turn-systemd-update-utmp-shutdown.service-into-.patch
Patch107: 0107-journal-correctly-convert-usec_t-to-timespec.patch
Patch108: 0108-Fix-syscall-__NR_fanotify_mark-.-on-arm.patch
Patch109: 0109-systemd-delta-add-support-for-drop-in-snippets.patch
Patch110: 0110-systemd-delta-count-overrides-only-of-the-requested-.patch
Patch111: 0111-core-fix-DBus-property-ExecMainExitTimestamp.patch
Patch112: 0112-keymap-Add-Samsung-900XC3.patch
Patch113: 0113-keymap-Add-BenQ-JoyBook.patch
Patch114: 0114-keymap-Add-DIXONSP.patch
Patch115: 0115-systemctl-honor-no-legend-in-list-sockets.patch
Patch116: 0116-service-kill-processes-with-SIGKILL-on-watchdog-fail.patch
Patch117: 0117-systemctl-make-systemctl-is-enabled-work-for-templat.patch
Patch118: 0118-systemctl-mangle-names-when-avoiding-dbus.patch
Patch119: 0119-keymap-Add-Logitech-USB-iTouch.patch
Patch120: 0120-systemd-record-efi-timestamps-after-sys-is-mounted.patch
Patch121: 0121-Fix-CPUShares-configuration-option.patch
Patch122: 0122-journald-DO-recalculate-the-ACL-mask-but-only-if-it-.patch
Patch123: 0123-core-read-debug-from-kernel-commandline-and-set-log-.patch
Patch124: 0124-systemctl-add-commands-set-default-and-get-default.patch
Patch125: 0125-systemctl-add-command-set-log-level.patch
Patch126: 0126-systemctl-suggest-systemctl-daemon-reload-without-sy.patch
Patch127: 0127-journal-take-KeepFree-into-account-when-reporting-ma.patch
Patch128: 0128-systemctl-core-allow-nuking-of-symlinks-to-removed-u.patch
Patch129: 0129-units-cleanup-agetty-command-line.patch
Patch130: 0130-systemctl-limit-logs-in-status-to-current-boot.patch
Patch131: 0131-keymap-add-some-more-Asus-laptop-keys.patch
Patch132: 0132-manager-Do-not-handle-SIGKILL-since-we-can-not.patch
Patch133: 0133-service-execute-ExecStopPost-commands-when-the-watch.patch
Patch134: 0134-cgroup-the-tasks-attribute-is-obsolete-cgroup.procs-.patch
Patch135: 0135-logs-show-print-multiline-messages.patch
Patch136: 0136-systemctl-remove-extra-padding-from-status-output.patch
Patch137: 0137-Allow-for-the-use-of-in-remote-host-calls.patch
Patch138: 0138-service-don-t-report-alien-child-as-alive-when-it-s-.patch
Patch139: 0139-journalctl-fix-verbose-output-when-no-logs-are-found.patch
Patch140: 0140-dev-setup-do-not-create-a-dangling-proc-kcore-symlin.patch
Patch141: 0141-journal-simplify-match_free_if_empty.patch
Patch142: 0142-journal-add-ability-to-filter-by-current-user.patch
Patch143: 0143-journalctl-add-system-user-flags.patch
Patch144: 0144-journal-loop-less-in-MATCH_AND_TERM-conditionals.patch
Patch145: 0145-journalctl-no-color-for-reboot-when-not-on-tty.patch
Patch146: 0146-journalctl-print-proper-IDs-with-header.patch
Patch147: 0147-journalctl-print-monotonic-timestamp-in-header.patch
Patch148: 0148-journal-add-sd_journal_open_files.patch
Patch149: 0149-journalctl-allow-the-user-to-specify-the-file-s-to-u.patch
Patch150: 0150-journal-remember-last-direction-of-search-and-keep-o.patch
Patch151: 0151-journal-change-direction-tests-to-use-the-same-conve.patch
Patch152: 0152-journal-letting-interleaved-seqnums-go.patch
Patch153: 0153-journald-do-not-overwrite-syslog-facility-when-parsi.patch
Patch154: 0154-journal-use-initialization-instead-of-zeroing.patch
Patch155: 0155-journald-do-not-calculate-free-space-too-early.patch
Patch156: 0156-journalctl-loginctl-systemctl-systemd-cgls-add-l-as-.patch
Patch157: 0157-mount-when-learning-about-the-root-mount-from-mounti.patch
Patch158: 0158-rules-only-run-systemd-sysctl-when-a-network-device-.patch
Patch159: 0159-udev-handle-network-controllers-in-nonstandard-domai.patch
Patch160: 0160-journalctl-properly-print-headers-of-empty-journals.patch
Patch161: 0161-build-sys-remove-SD_JOURNAL_SYSTEM_ONLY-3-from-Makef.patch

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
Obsoletes: systemd-tools

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

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

# (cg) Add aliases for prefdm.service
ln -s prefdm.service %{buildroot}%{_prefix}/lib/systemd/system/display-manager.service
ln -s prefdm.service %{buildroot}%{_prefix}/lib/systemd/system/dm.service

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants

# (cg) To avoid making life hard for developers, don't package the
# kernel.core_pattern setting until systemd-coredump is a part of an actual
# systemd release and it's made clear how to get the core dumps out of the
# journal.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/50-coredump.conf

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/syslog.target.wants

# And the default symlink we generate automatically based on inittab
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# (bor) make sure we own directory for bluez to install service
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/bluetooth.target.wants

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

# (cg) Just because I'm lazy while testing this....
# TODO deprecate nss-myhostname package
rm -f %{buildroot}%{_libdir}/libnss_myhostname.so.2 %{buildroot}/usr/share/man/man8/nss-myhostname.*
# (cg) We've not decided on this yet, but it'll likely be enabled "soon"
rm -f %{buildroot}%{_prefix}/lib/udev/rules.d/80-net-name-slot.rules


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
%dir %{_prefix}/lib/kernel
%dir %{_prefix}/lib/kernel/install.d
%dir %{_prefix}/lib/binfmt.d
%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.*
%config(noreplace) %{_sysconfdir}/sysconfig/udev_net
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
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
%{_prefix}/lib/sysctl.d/50-default.conf
#%{_prefix}/lib/sysctl.d/50-coredump.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_bindir}/bootctl
%{_bindir}/hostnamectl
%{_bindir}/journalctl
%{_bindir}/kernel-install
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
%{_bindir}/systemd-analyze
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
%{_mandir}/man8/kernel-install.*
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
%{_sysconfdir}/init.d/README
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
%{_prefix}/lib/systemd/catalog/systemd.catalog
%dir %{_logdir}/journal

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
%dir %{_datadir}/bash-completion
%{_bindir}/systemctl
%{_datadir}/bash-completion/completions
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
