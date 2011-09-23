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
Version:	35
Release:	%mkrel 4
License:	GPLv2+
Group:		System/Configuration/Boot and Init
Url:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2
# (bor) for now we use messabus service to start D-Bus
# Patch4:		0005-Set-special-D-Bus-service-to-messagebus.service.patch
# (bor) adapt vconsole service to Mandriva configuration
# Patch5:		0006-Adapt-vconsole-setup-to-Mandriva-configuration-based.patch
# (bor) support libnotify < 0.7; combines d0ef22 and ab85c2 (GIT)
#Patch12:	0001-gnome-ask-password-agent-also-support-libnotify-0.7-.patch
# (bor) take welcome message from /etc/release (adapted by blino)
Patch13:        systemd-30-add-mageia-support.patch

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
Requires:       nss-myhostname
# TODO for P12, remove when it is removed
BuildRequires:	automake 
BuildRequires:	autoconf

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
Conflicts:	%{name} <= 35-10

%description tools
Non essential systemd tools

%package units
Summary:	Configuration files, directories and installation tool for systemd
Group:		System/Configuration/Boot and Init
Requires:	%{name} = %{version}-%{release}

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
Conflicts:	%{name} <= 35-10

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
# TODO for P12, remove when it is removed
automake -c -f
autoconf
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

# The following services are currently executed by rc.sysinit
pushd %{buildroot}/lib/systemd/system/basic.target.wants && {
	rm -f sysctl.service
	rm -f systemd-modules-load.service
	rm -f systemd-tmpfiles.service
	rm -f systemd-tmpfiles-clean.timer
popd
}

# The following services are currently installed by initscripts
pushd %{buildroot}/lib/systemd/system/graphical.target.wants && {
	rm -f display-manager.service
popd
}

# The following services are currently executed by rc.sysinit
pushd %{buildroot}/lib/systemd/system/local-fs.target.wants && {
	rm -f cryptsetup.target
	rm -f fsck-root.service
	rm -f remount-rootfs.service
	rm -f systemd-remount-api-vfs.service
	rm -f var-lock.mount
	rm -f var-run.mount
popd
}

# The following services are currently installed by initscripts
pushd %{buildroot}/lib/systemd/system/multi-user.target.wants && {
	rm -f rc-local.service
	rm -f systemd-ask-password-wall.path
popd
}

# The following services are currently executed by rc.sysinit
pushd %{buildroot}/lib/systemd/system/sysinit.target.wants && {
	rm -f systemd-ask-password-console.path
	rm -f systemd-modules-load.service
	rm -f systemd-random-seed-load.service
	rm -f systemd-sysctl.service
	rm -f systemd-tmpfiles-setup.service
popd
}

# The following services are currently part of initscripts
pushd %{buildroot}/lib/systemd/system && {
	rm -f default.target
	rm -f display-manager.service
	rm -f prefdm.service
	rm -f rc-local.service
	rm -f single.service
	rm -f sysinit.service
popd
}

# (bor) For now mounts are performed by initscripts (Fedora)
sed -i -e 's/^#MountAuto=yes$/MountAuto=no/' \
        -e 's/^#SwapAuto=yes$/SwapAuto=no/' %{buildroot}/etc/systemd/system.conf

# (bor) make sure we own directory for bluez to install service
mkdir -p %{buildroot}/lib/systemd/system/bluetooth.target.wants

# (eugeni) we need /run directory
mkdir %{buildroot}/run


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
	# (bor) do not enable prefdm.service, we start it in initscript
        /bin/systemctl enable \
                getty@.service \
                rc-local.service \
                remote-fs.target 2>&1 || :
fi

%preun units
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                rc-local.service \
                remote-fs.target 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload 2>&1 || :
fi

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%dir %{_sysconfdir}/systemd/user
/usr/lib/tmpfiles.d/legacy.conf
/usr/lib/tmpfiles.d/systemd.conf
/usr/lib/tmpfiles.d/tmp.conf
/usr/lib/tmpfiles.d/x11.conf
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
%dir /lib/systemd
/lib/systemd/systemd-*
/lib/systemd/system-generators/systemd-*
/lib/udev/rules.d/*.rules
/%{_lib}/security/pam_systemd.so
%{_bindir}/systemd-cgls
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
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
/usr/lib/systemd/user/*.target
/usr/lib/systemd/user/*.service
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
%dir /run

%files tools
%defattr(-,root,root)
%{_bindir}/systemd-analyze

%files units
%defattr(-,root,root)
/bin/systemctl
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/tmpfiles.d
%{_sysconfdir}/bash_completion.d/systemctl-bash-completion.sh
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
%{_includedir}/systemd/sd-daemon.h
%{_libdir}/libsystemd-daemon.so
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_datadir}/pkgconfig/systemd.pc

%files -n %{liblogin}
%defattr(-,root,root,-)
%{_libdir}/libsystemd-login.so.%{liblogin_major}*

%files -n %{liblogin_devel}
%defattr(-,root,root,-)
%{_includedir}/systemd/sd-login.h
%{_libdir}/libsystemd-login.so
%{_libdir}/pkgconfig/libsystemd-login.pc

