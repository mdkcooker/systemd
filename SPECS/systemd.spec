# macros for sysvinit transition - should be equal to
# sysvinit %version-%release-plus-1
%define sysvinit_version 2.87
%define sysvinit_release %mkrel 9

%define libdaemon_major 0
%define liblogin_major 0

%define libdaemon %mklibname systemd-daemon %{libdaemon_major}
%define libdaemon_devel %mklibname -d systemd-daemon %{libdaemon_major}

%define liblogin %mklibname systemd-login %{liblogin_major}
%define liblogin_devel %mklibname -d systemd-login %{liblogin_major}


Summary:	A System and Session Manager
Name:		systemd
Version:	37
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Configuration/Boot and Init
Url:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2

# (cg) Upstream patches from git
Patch100: 0100-util-properly-detect-what-the-last-capability-is.patch
Patch101: 0101-manager-fix-a-crash-in-isolating.patch
Patch102: 0102-service-Drop-rcN.d-runlevels-from-SysV-services-that.patch
Patch103: 0103-audit-do-not-complain-if-kernel-lacks-audit.patch
Patch104: 0104-systemctl-completion-always-invoke-with-no-legend.patch


Patch500: systemd-36-add-mageia-support.patch
# (cg/bor) clean up directories on boot as done by rc.sysinit
Patch501: systemd-18-clean-dirs-on-boot.patch
# (cg/bor) reset /etc/mtab on boot (why is it not a link)?
Patch502: systemd-18-reset-mtab-on-boot.patch
# (cg/bor) fix potential deadlock when onseshot unit is not finished
Patch503: systemd-19-apply-timeoutsec-to-oneshot-too.patch
Patch504: systemd-tmpfilesd-utmp-temp-patch.patch
# (cg/tpg) Patches from upstream git
Patch505: systemd-halt-pre.patch
Patch506: systemd-33-rc-local.patch


BuildRequires:	dbus-devel >= 1.4.0
BuildRequires:	libudev-devel >= 172
BuildRequires:	libcap-devel
BuildRequires:	tcp_wrappers-devel
BuildRequires:	pam-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	vala >= 0.9
BuildRequires:	gtk2-devel  
BuildRequires:	glib2-devel
BuildRequires:	libnotify-devel
BuildRequires:	intltool
BuildRequires:  gperf
Requires:	systemd-units = %{version}-%{release}
Requires:	dbus >= 1.3.2
Requires:	udev >= 172
Requires:	initscripts >= 9.21-3
Requires:	util-linux-ng >= 2.18
Requires:	nss-myhostname
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
Conflicts:	%{name} <= 35-4

%description tools
Non essential systemd tools

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		System/Configuration/Boot and Init
Requires:	%{name} = %{version}-%{release}
Conflicts:	initscripts < 9.25

%description units
Basic configuration files, directories and installation tool for the systemd
system and session manager.

%package gtk
Summary:        Graphical frontend for systemd
Group:          System/Configuration/Boot and Init
Requires:       %{name} = %{version}-%{release}

%description gtk
Graphical front-end for systemd.

%package sysvinit
Summary:        System V init tools
Group:          System/Configuration/Boot and Init
Requires:       %{name} = %{version}-%{release}
# (eugeni) systemd should work as a drop-in replacement for sysvinit, but not obsolete it
Provides:       sysvinit = %sysvinit_version-%sysvinit_release, SysVinit = %sysvinit_release-%sysvinit_release
Conflicts:      sysvinit < %sysvinit_version-%sysvinit_release, SysVinit < %sysvinit_release-%sysvinit_release

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package -n %{libdaemon}
Summary:       Systemd-daemon library package
Group:                 System/Libraries
Provides:      libsystemd-daemon = %{version}-%{release}

%description -n %{libdaemon}
This package provides the systemd-daemon shared library.

%package -n %{libdaemon_devel}
Summary:       Systemd-daemon library development files
Group:                 Development/C
Requires:      %{libdaemon} = %{version}-%{release}
Provides:      libsystemd-daemon-devel = %{version}-%{release}
Conflicts:	%{name} <= 35-4

%description -n %{libdaemon_devel}
This package provides the development files for the systemd-daemon shared library.

%package -n %{liblogin}
Summary:       Systemd-login library package
Group:                 System/Libraries
Provides:      libsystemd-login = %{version}-%{release}

%description -n %{liblogin}
This package provides the systemd-login shared library.

%package -n %{liblogin_devel}
Summary:       Systemd-login library development files
Group:                 Development/C
Requires:      %{liblogin} = %{version}-%{release}
Provides:      libsystemd-login-devel = %{version}-%{release}

%description -n %{liblogin_devel}
This package provides the development files for the systemd-login shared library.

%prep
%setup -q
%apply_patches
find src/ -name "*.vala" -exec touch '{}' \;

%build
# TODO for P13, remove when it is removed
autoreconf -fi
%configure2_5x \
	--with-rootdir= \
	--with-sysvinit-path=%{_initrddir} \
	--with-sysvrcd-path=%{_sysconfdir}/rc.d 

%make

%install
rm -rf %{buildroot}

%makeinstall_std
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/sbin
ln -s ../bin/systemd %{buildroot}/sbin/init
ln -s ../bin/systemctl %{buildroot}/sbin/reboot
ln -s ../bin/systemctl %{buildroot}/sbin/halt
ln -s ../bin/systemctl %{buildroot}/sbin/poweroff
ln -s ../bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../bin/systemctl %{buildroot}/sbin/telinit
ln -s ../bin/systemctl %{buildroot}/sbin/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants
rm -f %{buildroot}%{_sysconfdir}/systemd/system/display-manager.service

# And the default symlink we generate automatically based on inittab
rm -f %{buildroot}%{_sysconfdir}/systemd/system/default.target

# We are not prepared to deal with tmpfs /var/run or /var/lock
pushd %{buildroot}/lib/systemd/system/local-fs.target.wants && {
  rm -f var-lock.mount
  rm -f var-run.mount
popd
}

# (bor) make sure we own directory for bluez to install service
mkdir -p %{buildroot}/lib/systemd/system/bluetooth.target.wants

# use consistent naming and permissions for completion scriplets
mv %{buildroot}%{_sysconfdir}/bash_completion.d/systemctl-bash-completion.sh \
  %{buildroot}%{_sysconfdir}/bash_completion.d/systemctl
chmod 644 %{buildroot}%{_sysconfdir}/bash_completion.d/systemctl

# (tpg) use systemd's own mounting capability
sed -i -e 's/^#MountAuto=yes$/MountAuto=yes/' \
  %{buildroot}/etc/systemd/system.conf

sed -i -e 's/^#SwapAuto=yes$/SwapAuto=yes/' \
  %{buildroot}/etc/systemd/system.conf

# (bor) disable legacy output to console, it just messes things up
sed -i -e 's/^#SysVConsole=yes$/SysVConsole=no/' \
  %{buildroot}/etc/systemd/system.conf

# (bor) enable rpcbind.target by default so we have something to plug
# portmapper service into
ln -s ../rpcbind.target %{buildroot}/lib/systemd/system/multi-user.target.wants

# (eugeni) install /run
mkdir %{buildroot}/run

# add missing ttys (mdv #63600)
mkdir -p %{buildroot}/etc/systemd/system/getty.target.wants
pushd %{buildroot}/etc/systemd/system/getty.target.wants
  for _term in 1 2 3 4 5 6 ; do
    ln -s /lib/systemd/system/getty@.service getty@tty$_term.service
  done
popd

# create modules.conf as a symlink to /etc/
ln -s /etc/modules %{buildroot}%{_sysconfdir}/modules-load.d/modules.conf
# (tpg) symlink also modprobe.preload because a lot of modules are inserted there from drak* stuff
ln -s /etc/modprobe.preload %{buildroot}%{_sysconfdir}/modules-load.d/modprobe-preload.conf

# (tpg) add rpm macros
#install -m 0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d/%{name}.macros

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/os-release
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info

%clean
rm -rf %{buildroot}

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
                rsyslog.service \
                2>&1 || :
# rc-local is now enabled by default in base package
rm -f /etc/systemd/system/multi-user.target.wants/rc-local.service || :

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
                hwclock-load.service \
                getty@.service \
                quotaon.service \
                quotacheck.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                rsyslog.service \
                2>&1 || :
fi

%preun units
if [ $1 -eq 0 ] ; then
        /bin/systemctl --quiet disable \
                hwclock-load.service \
                getty@.service \
                quotaon.service \
                quotacheck.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                rsyslog.service \
                2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload 2>&1 || :
fi

%files
%defattr(-,root,root)
# (cg) Note some of these directories are empty, but that is intended
%dir /run
%dir /lib/systemd
%dir /lib/systemd/system-generators
%dir /lib/systemd/system-shutdown
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_sysconfdir}/systemd/systemd-logind.conf
%{_sysconfdir}/systemd/user.conf
%{_sysconfdir}/xdg/systemd
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/os-release
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
/bin/systemd
/bin/systemd-ask-password
/bin/systemd-loginctl
/bin/systemd-machine-id-setup
/bin/systemd-notify
/bin/systemd-tmpfiles
/bin/systemd-tty-ask-password-agent
/lib/systemd/systemd-*
/lib/systemd/system-generators/systemd-*
/lib/udev/rules.d/*.rules
/%{_lib}/security/pam_systemd.so
%{_bindir}/systemd-cgls
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_datadir}/systemd/kbd-model-map
%{_mandir}/man1/systemd.*
%{_mandir}/man1/systemd-notify.*
%{_mandir}/man1/systemd-cgls.*
%{_mandir}/man1/systemd-ask-password.1.*
%{_mandir}/man1/systemd-loginctl.1.*
%{_mandir}/man1/systemd-nspawn.1.*
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
%dir %{_sysconfdir}/systemd/system/getty.target.wants
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/bash_completion.d
/bin/systemctl
%{_sysconfdir}/bash_completion.d/systemctl
%{_sysconfdir}/modules-load.d/*.conf
%{_sysconfdir}/systemd/system/getty.target.wants/getty@*.service
/lib/systemd/system
%{_mandir}/man1/systemctl.*

%files gtk
%defattr(-,root,root)
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*

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
%{_libdir}/libsystemd-daemon.so.%{libdaemon_major}*

%files -n %{libdaemon_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-daemon.h
%{_libdir}/libsystemd-daemon.so
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_datadir}/pkgconfig/systemd.pc

%files -n %{liblogin}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-login.so.%{liblogin_major}*

%files -n %{liblogin_devel}
%defattr(-,root,root,-)
%dir %{_includedir}/systemd
%{_includedir}/systemd/sd-login.h
%{_libdir}/libsystemd-login.so
%{_libdir}/pkgconfig/libsystemd-login.pc

