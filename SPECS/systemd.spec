# macros for sysvinit transition - should be equal to
# sysvinit %version-%release-plus-1
%define sysvinit_version 2.87
%define sysvinit_release %mkrel 15

%define libdaemon_major 0
%define liblogin_major 0
%define libjournal_major 0
%define libid128_major 0

%define libdaemon %mklibname systemd-daemon %{libdaemon_major}
%define libdaemon_devel %mklibname -d systemd-daemon %{libdaemon_major}

%define liblogin %mklibname systemd-login %{liblogin_major}
%define liblogin_devel %mklibname -d systemd-login %{liblogin_major}

%define libjournal %mklibname systemd-journal %{libjournal_major}
%define libjournal_devel %mklibname -d systemd-journal %{libjournal_major}

%define libid128 %mklibname systemd-id128 %{libid128_major}
%define libid128_devel %mklibname -d systemd-id128 %{libid128_major}

Summary:	A System and Session Manager
Name:		systemd
Version:	44
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Configuration/Boot and Init
Url:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz

# (cg) Upstream cherry picks
Patch100: 0100-util-never-follow-symlinks-in-rm_rf_children.patch
Patch101: 0101-journal-react-with-immediate-rotation-to-a-couple-of.patch
Patch102: 0102-journal-PAGE_SIZE-is-not-known-on-ppc-and-other-arch.patch
Patch103: 0103-man-systemd-cat-1-typo-fix.patch
Patch104: 0104-logind-close-FIFO-before-ending-sessions-cleanly.patch
Patch105: 0105-man-minor-typo-in-reference-to-manual-page.patch
Patch106: 0106-journalctl-loginctl-drop-systemd-prefix-in-binary-na.patch
Patch107: 0107-build-sys-do-not-set-CFLAGS-directly.patch
Patch108: 0108-build-sys-separate-ldflags-from-cflags.patch
Patch109: 0109-cat-fix-priority-type.patch
Patch110: 0110-units-don-t-mount-tmpfs-on-media-anymore.patch
Patch111: 0111-units-get-rid-of-var-run.mount-and-var-lock.mount.patch
Patch112: 0112-journal-properly-handle-if-we-interleave-files-with-.patch
Patch113: 0113-job-fix-loss-of-ordering-with-restart-jobs.patch
Patch114: 0114-job-add-debug-prints-where-job-type-gets-changed.patch
Patch115: 0115-rename-etc-systemd-systemd-login-journal-d.conf-to-l.patch

# (cg/bor) clean up directories on boot as done by rc.sysinit
# - Lennart should be poked about this (he couldn't think why he hadn't done it already)
Patch500: 0500-Clean-directories-that-were-cleaned-up-by-rc.sysinit.patch
# (cg/bor) fix potential deadlock when onseshot unit is not finished
# - Lennart will do this eventually but believes this patch is insufficient.
Patch501: 0501-apply-TimeoutSec-to-oneshot-services-too.patch
Patch502: 0502-Some-more-tmpfiles-fixes.patch
Patch503: 0503-mageia-Change-the-unit-for-prefdm.service-to-make-it.patch
Patch504: 0504-hack-Fix-syslog.socket-to-not-cause-a-deadlock.patch
Patch505: 0505-main-Add-failsafe-to-the-sysvinit-compat-cmdline-key.patch
Patch506: 0506-mageia-Fallback-message-when-display-manager-fails.patch
Patch507: 0507-mageia-not-upstream-Add-mount-automount-units-for-pr.patch
Patch508: 0508-mount-Add-a-new-remote-fs-target-to-specifically-del.patch
Patch509: 0509-analyze-Cosmetic-exit-when-the-bootup-is-not-yet-com.patch


BuildRequires:	dbus-devel >= 1.4.0
BuildRequires:	libudev-devel >= 172
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
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
Requires:	systemd-units = %{version}-%{release}
Requires:	dbus >= 1.3.2
Requires:	udev >= 172
Requires:	initscripts >= 9.21-3
Requires:	util-linux-ng >= 2.18
Requires:	nss-myhostname
Requires:	lockdev
Conflicts:	initscripts < 9.25

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
Group:		System/Configuration/Boot and Init
Requires:	%{name} = %{version}-%{release}
Requires:	python-dbus
Requires:	python-cairo
Conflicts:	%{name} <= 37-15

%description tools
Non essential systemd tools

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		System/Configuration/Boot and Init
Requires:	%{name} = %{version}-%{release}
Conflicts:	initscripts < 9.25
Requires(post): coreutils grep awk

%description units
Basic configuration files, directories and installation tool for the systemd
system and session manager.

%package sysvinit
Summary:        System V init tools
Group:          System/Configuration/Boot and Init
Requires:       %{name} = %{version}-%{release}
# (eugeni) systemd should work as a drop-in replacement for sysvinit, but not obsolete it
Provides:       sysvinit = %sysvinit_version-%sysvinit_release
Conflicts:      SysVinit

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package -n %{libdaemon}
Summary:       Systemd-daemon library package
Group:         System/Libraries
Provides:      libsystemd-daemon = %{version}-%{release}

%description -n %{libdaemon}
This package provides the systemd-daemon shared library.

%package -n %{libdaemon_devel}
Summary:       Systemd-daemon library development files
Group:         Development/C
Requires:      %{libdaemon} = %{version}-%{release}
Provides:      libsystemd-daemon-devel = %{version}-%{release}
Conflicts:	%{name} <= 35-4

%description -n %{libdaemon_devel}
This package provides the development files for the systemd-daemon shared library.

%package -n %{liblogin}
Summary:       Systemd-login library package
Group:         System/Libraries
Provides:      libsystemd-login = %{version}-%{release}

%description -n %{liblogin}
This package provides the systemd-login shared library.

%package -n %{liblogin_devel}
Summary:       Systemd-login library development files
Group:         Development/C
Requires:      %{liblogin} = %{version}-%{release}
Provides:      libsystemd-login-devel = %{version}-%{release}

%description -n %{liblogin_devel}
This package provides the development files for the systemd-login shared library.

%package -n %{libjournal}
Summary:       Systemd-journal library package
Group:         System/Libraries
Provides:      libsystemd-journal = %{version}-%{release}

%description -n %{libjournal}
This package provides the systemd-journal shared library.

%package -n %{libjournal_devel}
Summary:       Systemd-journal library development files
Group:         Development/C
Requires:      %{libjournal} = %{version}-%{release}
Provides:      libsystemd-journal-devel = %{version}-%{release}

%description -n %{libjournal_devel}
This package provides the development files for the systemd-journal shared library.

%package -n %{libid128}
Summary:       Systemd-id128 library package
Group:         System/Libraries
Provides:      libsystemd-id128 = %{version}-%{release}

%description -n %{libid128}
This package provides the systemd-id128 shared library.

%package -n %{libid128_devel}
Summary:       Systemd-id128 library development files
Group:         Development/C
Requires:      %{libid128} = %{version}-%{release}
Provides:      libsystemd-id128-devel = %{version}-%{release}

%description -n %{libid128_devel}
This package provides the development files for the systemd-id128 shared library.

%prep
%setup -q
%apply_patches
find src/ -name "*.vala" -exec touch '{}' \;

%build
%configure2_5x \
  --with-distro=mageia \
  --disable-gtk \
  --disable-coredump \
  --disable-static \
  --with-rootprefix= \
  --with-rootlibdir=/%{_lib}

%make

%install
rm -rf %{buildroot}

%makeinstall_std
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/sbin
ln -s ../lib/systemd/systemd %{buildroot}/bin/systemd
ln -s ../lib/systemd/systemd %{buildroot}/sbin/init
ln -s ../bin/systemctl %{buildroot}/sbin/reboot
ln -s ../bin/systemctl %{buildroot}/sbin/halt
ln -s ../bin/systemctl %{buildroot}/sbin/poweroff
ln -s ../bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../bin/systemctl %{buildroot}/sbin/telinit
ln -s ../bin/systemctl %{buildroot}/sbin/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}/etc/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}/lib/systemd/system/syslog.target.wants

# And the default symlink we generate automatically based on inittab
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# (bor) make sure we own directory for bluez to install service
mkdir -p %{buildroot}/lib/systemd/system/bluetooth.target.wants

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

# (bor) disable legacy output to console, it just messes things up
sed -i -e 's/^#SysVConsole=yes$/SysVConsole=no/' \
  %{buildroot}/etc/systemd/system.conf

# (bor) enable rpcbind.target by default so we have something to plug
# portmapper service into
ln -s ../rpcbind.target %{buildroot}/lib/systemd/system/multi-user.target.wants

# (eugeni) install /run
mkdir %{buildroot}/run

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

# Let rsyslog read from /proc/kmsg for now
sed -i -e 's/\#ImportKernel=yes/ImportKernel=no/' %{buildroot}%{_sysconfdir}/systemd/journald.conf

# Create unowned folders
mkdir -p %{buildroot}%{_libdir}/systemd/user/

# automatic systemd release on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.filter << EOF
^./lib/systemd/system/
^./etc/systemd/system/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.script << EOF
#!/bin/sh
if /bin/mountpoint -q /sys/fs/cgroup/systemd; then
  if [ -x /bin/systemctl ]; then
  /bin/systemctl daemon-reload >/dev/null 2>&1 || :
  fi
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.script

# This file is already in sytemd-ui rpm
rm -fr %buildroot%_mandir/man1/systemadm.*

%triggerin -- glibc
# reexec daemon on self or glibc update to avoid busy / on shutdown
# trigger is executed on both self and target install so no need to have
# extra own post
if [ $1 -ge 2 -o $2 -ge 2 ] ; then
	/bin/systemctl daemon-reexec 2>&1 || :
fi

%post
/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
#/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

%triggerin units -- %{name}-units < 35-1
# Enable the services we install by default.
        /bin/systemctl --quiet enable \
                hwclock-load.service \
                getty@.service \
                quotaon.service \
                quotacheck.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :
# rc-local is now enabled by default in base package
rm -f %_sysconfdir/systemd/system/multi-user.target.wants/rc-local.service || :

%post units
if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/lib/systemd/system/graphical.target"
        else
                target="/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" %{_sysconfdir}/systemd/system/default.target 2>&1 || :

        # Enable the services we install by default.
        /bin/systemctl --quiet enable \
                getty@.service \
                quotaon.service \
                quotacheck.service \
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
        /bin/systemctl --quiet disable \
                getty@.service \
                quotaon.service \
                quotacheck.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :

        /bin/rm -f %_sysconfdir/systemd/system/default.target 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload 2>&1 || :
fi

%files
# (cg) Note some of these directories are empty, but that is intended
%dir /run
%dir /lib/systemd
%dir /lib/systemd/system-generators
%dir /lib/systemd/system-shutdown
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%dir %_libdir/systemd
%dir %_libdir/systemd/user/
%{_var}/lib/rpm/filetriggers/systemd-daemon-reload.*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
#%{_prefix}/lib/sysctl.d/coredump.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_sysconfdir}/systemd/logind.conf
%{_sysconfdir}/systemd/user.conf
%{_sysconfdir}/xdg/systemd
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%ghost %config(noreplace) %{_sysconfdir}/timezone
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
/bin/journalctl
/bin/loginctl
/bin/systemd
/bin/systemd-ask-password
/bin/systemd-machine-id-setup
/bin/systemd-notify
/bin/systemd-tmpfiles
/bin/systemd-tty-ask-password-agent
/lib/systemd/systemd*
/lib/systemd/system-generators/systemd-*
/lib/udev/rules.d/*.rules
/%{_lib}/security/pam_systemd.so
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_datadir}/systemd/kbd-model-map
%{_mandir}/man1/journalctl.*
%{_mandir}/man1/loginctl.*
%{_mandir}/man1/systemd.*
%{_mandir}/man1/systemd-*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/pam_systemd.*
%{_mandir}/man8/systemd-tmpfiles.*
%{_prefix}/lib/systemd/user/*.target
%{_prefix}/lib/systemd/user/*.service
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
/bin/systemctl
%{_sysconfdir}/bash_completion.d/systemd
%{_sysconfdir}/profile.d/40systemd.sh
%{_sysconfdir}/modules-load.d/*.conf
/lib/systemd/system
%{_mandir}/man1/systemctl.*

%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files sysvinit
%defattr(-,root,root,-)
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%{_mandir}/man1/init.*
%{_mandir}/man8/halt.*
%{_mandir}/man8/reboot.*
%{_mandir}/man8/shutdown.*
%{_mandir}/man8/poweroff.*
%{_mandir}/man8/telinit.*
%{_mandir}/man8/runlevel.*

%files -n %{libdaemon}
%defattr(-,root,root,-)
/%{_lib}/libsystemd-daemon.so.%{libdaemon_major}*

%files -n %{libdaemon_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-daemon.h
%{_libdir}/libsystemd-daemon.so
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_datadir}/pkgconfig/systemd.pc
# TODO: Move in its own sub package
%{_includedir}/systemd/sd-messages.h

%files -n %{liblogin}
%defattr(-,root,root,-)
/%{_lib}/libsystemd-login.so.%{liblogin_major}*

%files -n %{liblogin_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-login.h
%{_libdir}/libsystemd-login.so
%{_libdir}/pkgconfig/libsystemd-login.pc

%files -n %{libjournal}
%defattr(-,root,root,-)
/%{_lib}/libsystemd-journal.so.%{libjournal_major}*

%files -n %{libjournal_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-journal.h
%{_libdir}/libsystemd-journal.so
%{_libdir}/pkgconfig/libsystemd-journal.pc

%files -n %{libid128}
%defattr(-,root,root,-)
/%{_lib}/libsystemd-id128.so.%{libid128_major}*

%files -n %{libid128_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-id128.h
%{_libdir}/libsystemd-id128.so
%{_libdir}/pkgconfig/libsystemd-id128.pc
