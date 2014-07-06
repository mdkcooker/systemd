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
Version:	208
Release:	%mkrel 16
License:	GPLv2+
Group:		System/Boot and Init
Url:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz

Source10: 50-udev-mageia.rules
Source11: 69-printeracl.rules
# (hk) udev rules for zte 3g modems with drakx-net
Source12: 61-mobile-zte-drakx-net.rules

# (blino) net rules and helpers
Source20: 81-net.rules
Source21: udev_net_create_ifcfg
Source22: udev_net_action
Source23: udev_net.sysconfig

# (cg) "Stable" Patches for v208 from http://cgit.freedesktop.org/systemd/systemd-stable/log/?h=v208-stable
Patch001: 0001-acpi-fptd-fix-memory-leak-in-acpi_get_boot_usec.patch
Patch002: 0002-fix-lingering-references-to-var-lib-backlight-random.patch
Patch003: 0003-acpi-make-sure-we-never-free-an-uninitialized-pointe.patch
Patch004: 0004-systemctl-fix-name-mangling-for-sysv-units.patch
Patch005: 0005-cryptsetup-fix-OOM-handling-when-parsing-mount-optio.patch
Patch006: 0006-journald-add-missing-error-check.patch
Patch007: 0007-bus-fix-potentially-uninitialized-memory-access.patch
Patch008: 0008-dbus-fix-return-value-of-dispatch_rqueue.patch
Patch009: 0009-modules-load-fix-error-handling.patch
Patch010: 0010-efi-never-call-qsort-on-potentially-NULL-arrays.patch
Patch011: 0011-strv-don-t-access-potentially-NULL-string-arrays.patch
Patch012: 0012-mkdir-pass-a-proper-function-pointer-to-mkdir_safe_i.patch
Patch013: 0013-tmpfiles.d-include-setgid-perms-for-run-log-journal.patch
Patch014: 0014-execute.c-always-set-SHELL.patch
Patch015: 0015-man-Improve-the-description-of-parameter-X-in-tmpfil.patch
Patch016: 0016-execute-more-debugging-messages.patch
Patch017: 0017-gpt-auto-generator-exit-immediately-if-in-container.patch
Patch018: 0018-systemd-order-remote-mounts-from-mountinfo-before-re.patch
Patch019: 0019-manager-when-verifying-whether-clients-may-change-en.patch
Patch020: 0020-logind-fix-bus-introspection-data-for-TakeControl.patch
Patch021: 0021-mount-check-for-NULL-before-reading-pm-what.patch
Patch022: 0022-core-do-not-add-what-to-RequiresMountsFor-for-networ.patch
Patch023: 0023-utf8-fix-utf8_is_printable.patch
Patch024: 0024-shared-util-fix-off-by-one-error-in-tag_to_udev_node.patch
Patch025: 0025-systemd-serialize-deserialize-forbid_restart-value.patch
Patch026: 0026-core-unify-the-way-we-denote-serialization-attribute.patch
Patch027: 0027-journald-fix-minor-memory-leak.patch
Patch028: 0028-keymap-Fix-Samsung-900X-34-C.patch
Patch029: 0029-do-not-accept-garbage-from-acpi-firmware-performance.patch
Patch030: 0030-journald-remove-rotated-file-from-hashmap-when-rotat.patch
Patch031: 0031-login-fix-invalid-free-in-sd_session_get_vt.patch
Patch032: 0032-login-make-sd_session_get_vt-actually-work.patch
Patch033: 0033-udevadm.xml-document-resolve-names-option-for-test.patch
Patch034: 0034-Never-call-qsort-on-potentially-NULL-arrays.patch
Patch035: 0035-dbus-common-avoid-leak-in-error-path.patch
Patch036: 0036-drop-ins-check-return-value.patch
Patch037: 0037-Make-sure-that-we-don-t-dereference-NULL.patch
#Patch038: 0038-gitignore-ignore-clang-analyze-output.patch
Patch039: 0039-man-add-more-markup-to-udevadm-8.patch
Patch040: 0040-shared-util-Fix-glob_extend-argument.patch
Patch041: 0041-Fix-bad-assert-in-show_pid_array.patch
Patch042: 0042-Fix-for-SIGSEGV-in-systemd-bootchart-on-short-living.patch
Patch043: 0043-man-document-the-b-special-boot-option.patch
Patch044: 0044-logind-allow-unprivileged-session-device-access.patch
Patch045: 0045-rules-expose-loop-block-devices-to-systemd.patch
Patch046: 0046-rules-don-t-limit-some-of-the-rules-to-the-add-actio.patch
Patch047: 0047-tmpfiles-log-unaccessible-FUSE-mount-points-only-as-.patch
Patch048: 0048-hwdb-update.patch
Patch049: 0049-rules-remove-pointless-MODE-settings.patch
Patch050: 0050-analyze-set-white-backgound.patch
Patch051: 0051-shell-completion-dump-has-moved-to-systemd-analyze.patch
Patch052: 0052-systemd-use-unit-name-in-PrivateTmp-directories.patch
Patch053: 0053-catalog-remove-links-to-non-existent-wiki-pages.patch
Patch054: 0054-journalctl-add-list-boots-to-show-boot-IDs-and-times.patch
Patch055: 0055-udev-builtin-path_id-add-support-for-bcma-bus.patch
Patch056: 0056-udev-ata_id-log-faling-ioctls-as-debug.patch
Patch057: 0057-libudev-default-log_priority-to-INFO.patch
Patch058: 0058-nspawn-only-pass-in-slice-setting-if-it-is-set.patch
Patch059: 0059-zsh-completion-add-systemd-run.patch
Patch060: 0060-man-explain-NAME-in-systemctl-man-page.patch
Patch061: 0061-virt-move-caching-of-virtualization-check-results-in.patch
Patch062: 0062-systemctl-fix-typo-in-help-text.patch
Patch063: 0063-analyze-plot-place-the-text-on-the-side-with-most-sp.patch
Patch064: 0064-detect_virtualization-returns-NULL-pass-empty-string.patch
Patch065: 0065-rules-load-path_id-on-DRM-devices.patch
Patch066: 0066-rules-simply-60-drm.rules.patch
Patch067: 0067-udev-builtin-keyboard-Fix-large-scan-codes-on-32-bit.patch
Patch068: 0068-nspawn-log-out-of-memory-errors.patch
Patch069: 0069-Configurable-Timeouts-Restarts-default-values.patch
Patch070: 0070-man-fix-typo.patch
Patch071: 0071-man-do-not-use-term-in-para.patch
Patch072: 0072-cgroup-run-PID-1-in-the-root-cgroup.patch
Patch073: 0073-shutdown-trim-the-cgroup-tree-on-loop-iteration.patch
Patch074: 0074-nspawn-split-out-pty-forwaring-logic-into-ptyfwd.c.patch
Patch075: 0075-nspawn-explicitly-terminate-machines-when-we-exit-ns.patch
Patch076: 0076-run-support-system-to-match-other-commands-even-if-r.patch
Patch077: 0077-acpi-fpdt-break-on-zero-or-negative-length-read.patch
Patch078: 0078-man-add-rationale-into-systemd-halt-8.patch
Patch079: 0079-systemd-python-convert-keyword-value-to-string.patch
Patch080: 0080-systemctl-make-LOAD-column-width-dynamic.patch
Patch081: 0081-Make-hibernation-test-work-for-swap-files.patch
Patch082: 0082-man-add-docs-for-sd_is_special-and-some-man-page-sym.patch
Patch083: 0083-systemctl-return-r-instead-of-always-returning-0.patch
Patch084: 0084-journal-fix-minor-memory-leak.patch
Patch085: 0085-manager-configurable-StartLimit-default-values.patch
Patch086: 0086-man-units-fix-installation-of-systemd-nspawn-.servic.patch
Patch087: 0087-systemd-fix-memory-leak-in-cgroup-code.patch
Patch088: 0088-button-don-t-exit-if-we-cannot-handle-a-button-press.patch
Patch089: 0089-timer-properly-format-relative-timestamps-in-the-fut.patch
Patch090: 0090-timer-consider-usec_t-1-an-invalid-timestamp.patch
Patch091: 0091-udev-usb_id-remove-obsoleted-bInterfaceSubClass-5-ma.patch
Patch092: 0092-Add-support-for-saving-restoring-keyboard-backlights.patch
Patch093: 0093-static-nodes-don-t-call-mkdir.patch
Patch094: 0094-Fix-kmod-error-message-to-have-correct-version-requi.patch
Patch095: 0095-systemd-python-fix-booted-and-add-two-functions-to-d.patch
Patch096: 0096-activate-mention-E-in-the-help-text.patch
Patch097: 0097-activate-fix-crash-when-s-is-passed.patch
Patch098: 0098-journal-timestamp-support-on-console-messages.patch
Patch099: 0099-man-add-bootctl-8.patch
Patch100: 0100-zsh-completion-add-bootctl.patch
Patch101: 0101-Resolve-dev-console-to-the-active-tty-instead-of-jus.patch
Patch102: 0102-Only-disable-output-on-console-during-boot-if-needed.patch
Patch103: 0103-Fix-possible-lack-of-status-messages-on-shutdown-reb.patch
Patch104: 0104-fsck-modernization.patch
Patch105: 0105-Introduce-udev-object-cleanup-functions.patch
Patch106: 0106-util-allow-trailing-semicolons-on-define_trivial_cle.patch
Patch107: 0107-fsck-fstab-generator-be-lenient-about-missing-fsck.-.patch
Patch108: 0108-fstab-generator-use-RequiresOverridable-for-fsck-uni.patch
Patch109: 0109-bash-completion-journalctl-file.patch
Patch110: 0110-random-seed-improve-debugging-messages-a-bit.patch
Patch111: 0111-Fix-RemainAfterExit-services-keeping-a-hold-on-conso.patch
Patch112: 0112-tmpfiles-adjust-excludes-for-the-new-per-service-pri.patch
Patch113: 0113-core-socket-fix-SO_REUSEPORT.patch
Patch114: 0114-localed-match-converted-keymaps-before-legacy.patch
Patch115: 0115-keymap-Add-Toshiba-Satellite-U940.patch
Patch116: 0116-calendar-support-yearly-and-annually-names-the-same-.patch
Patch117: 0117-hashmap-be-a-bit-more-conservative-with-pre-allocati.patch
Patch118: 0118-manager-don-t-do-plymouth-in-a-container.patch
Patch119: 0119-nspawn-add-new-drop-capability-switch.patch
Patch120: 0120-valgrind-make-running-PID-1-in-valgrind-useful.patch
Patch121: 0121-efi-boot-generator-don-t-mount-boot-eagerly.patch
Patch122: 0122-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch123: 0123-journal-when-appending-to-journal-file-allocate-larg.patch
Patch124: 0124-journal-make-table-const.patch
Patch125: 0125-journald-keep-statistics-on-how-of-we-hit-miss-the-m.patch
Patch126: 0126-journal-optimize-bisection-logic-a-bit-by-caching-th.patch
Patch127: 0127-journal-fix-iteration-when-we-go-backwards-from-the-.patch
Patch128: 0128-journal-allow-journal_file_copy_entry-to-work-on-non.patch
Patch129: 0129-journal-simplify-pre-allocation-logic.patch
Patch130: 0130-journald-mention-how-long-we-needed-to-flush-to-var-.patch
Patch131: 0131-automount-log-info-about-triggering-process.patch
Patch132: 0132-virt-split-detect_vm-into-separate-functions.patch
Patch133: 0133-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch134: 0134-sysfs-show.c-return-negative-error.patch
Patch135: 0135-util.c-check-if-return-value-from-ttyname_r-is-0-ins.patch
Patch136: 0136-docs-remove-unneeded-the-s-in-gudev-docs.patch
Patch137: 0137-man-explicitly-say-when-multiple-units-can-be-specif.patch
Patch138: 0138-systemd-treat-reload-failure-as-failure.patch
Patch139: 0139-journal-fail-silently-in-sd_j_sendv-if-journal-is-un.patch
Patch140: 0140-systemd-add-a-start-job-for-all-units-specified-with.patch
# (cg) NB This patch is buggy and causes /run/nologin problems (rhbz#1043212)
# but it is reverted again below.
Patch141: 0141-core-device-ignore-SYSTEMD_WANTS-in-user-mode.patch
Patch142: 0142-Fix-memory-leak-in-stdout-journal-streams.patch
Patch143: 0143-man-document-is-enabled-output.patch
# (cg) Below is not technically a backport (fixed differently upstream in kdbus work?)
Patch144: 0144-hostnamed-avoid-using-NULL-in-error-path.patch
# (cg) Below is not technically a backport (fixed differently upstream in kdbus work)
Patch145: 0145-logind-use-correct-who-enum-values-with-KillUnit.patch
# (cg) Revert buggy patch mentioned a few lines above
Patch146: 0146-Revert-systemd-add-a-start-job-for-all-units-specifi.patch
# (cg) Below is not technically a backport (fixed differently upstream in kdbus work?)
Patch147: 0147-core-do-not-segfault-if-swap-activity-happens-when-p.patch
Patch148: 0148-kernel-install-add-h-help.patch
Patch149: 0149-kernel-install-fix-help-output.patch
Patch150: 0150-man-improve-wording-and-comma-usage-in-systemd.journ.patch
Patch151: 0151-drop-several-entries-from-kbd-model-map-whose-kbd-la.patch
Patch152: 0152-correct-name-of-Tajik-kbd-layout-in-kbd-model-map.patch
Patch153: 0153-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch154: 0154-Ensure-unit-is-journaled-for-short-lived-or-oneshot-.patch
Patch155: 0155-libudev-hwdb-use-libudev-not-systemd-logging.patch
Patch156: 0156-core-manager-remove-infinite-loop.patch
Patch157: 0157-util-check-for-overflow-in-greedy_realloc.patch
Patch158: 0158-journald-use-a-bit-more-cleanup-magic.patch
Patch159: 0159-journald-malloc-less-when-streaming-messages.patch
Patch160: 0160-activate-clean-up-inherited-descriptors.patch
Patch161: 0161-man-explain-in-more-detail-how-SYSTEMD_READY-influen.patch
Patch162: 0162-units-don-t-run-readahead-done-timers-in-containers.patch
Patch163: 0163-test-fileio-replace-mktemp-with-mkstemp-to-avoid-war.patch
Patch164: 0164-journal-pipe-journalctl-help-output-into-a-pager.patch
Patch165: 0165-nspawn-complain-and-continue-if-machine-has-same-id.patch
Patch166: 0166-man-beef-up-ExecStart-description.patch
Patch167: 0167-man-remove-advice-to-avoid-setting-the-same-var-more.patch
Patch168: 0168-systemctl-add-the-plain-option-to-the-help-message.patch
Patch169: 0169-Fix-a-few-resource-leaks-in-error-paths.patch
Patch170: 0170-Fix-a-few-signed-unsigned-format-string-issues.patch
Patch171: 0171-util-try-harder-to-increase-the-send-recv-buffers-of.patch
Patch172: 0172-execute-also-set-SO_SNDBUF-when-spawning-a-service-w.patch
Patch173: 0173-journal-file-protect-against-alloca-0.patch
Patch174: 0174-man-describe-journalctl-show-cursor.patch
Patch175: 0175-journal-fix-against-theoretical-undefined-behavior.patch
Patch176: 0176-journald-downgrade-warning-message-when-dev-kmsg-doe.patch
Patch177: 0177-journal-file.c-remove-redundant-assignment-of-variab.patch
Patch178: 0178-login-Don-t-stop-a-running-user-manager-from-garbage.patch
Patch179: 0179-libudev-devices-received-from-udev-are-always-initia.patch
Patch180: 0180-log-don-t-reopen-dev-console-each-time-we-call-log_o.patch
Patch181: 0181-log-when-we-log-to-dev-console-and-got-disconnected-.patch
Patch182: 0182-loginctl-when-showing-device-tree-of-seats-with-no-d.patch
Patch183: 0183-man-be-more-explicit-about-option-arguments-that-tak.patch
Patch184: 0184-man-add-DOI-for-refereed-article-on-Forward-Secure-S.patch
Patch185: 0185-journalctl-zsh-completion-fix-several-issues-in-help.patch
Patch186: 0186-keymap-Refactor-Acer-tables.patch
Patch187: 0187-logging-reduce-send-timeout-to-something-more-sensib.patch
Patch188: 0188-DEFAULT_PATH_SPLIT_USR-macro.patch
Patch189: 0189-fstab-generator-Do-not-try-to-fsck-non-devices.patch
Patch190: 0190-logind-remove-dead-variable.patch
Patch191: 0191-hwdb-update.patch
Patch192: 0192-delta-replace-readdir_r-with-readdir.patch
Patch193: 0193-delta-fix-delta-for-drop-ins.patch
Patch194: 0194-delta-if-prefix-is-specified-only-show-overrides-the.patch
Patch195: 0195-log-log_error-and-friends-add-a-newline-after-each-l.patch
Patch196: 0196-man-units-tmpfiles.d-5-cleanup.patch
Patch197: 0197-tmpfiles-introduce-the-concept-of-unsafe-operations.patch
Patch198: 0198-sleep-config-fix-useless-check-for-swapfile-type.patch
Patch199: 0199-journalctl-make-sure-b-foobar-cannot-be-misunderstoo.patch
Patch200: 0200-man-resolve-word-omissions.patch
Patch201: 0201-man-improvements-to-comma-placement.patch
Patch202: 0202-man-grammar-and-wording-improvements.patch
Patch203: 0203-man-document-fail-nofail-auto-noauto.patch
Patch204: 0204-man-fix-description-of-is-enabled-returned-value.patch
Patch205: 0205-man-fix-Type-reference.patch
Patch206: 0206-man-fix-Type-reference-v2.patch
Patch207: 0207-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch208: 0208-man-add-a-note-about-propagating-signals.patch
Patch209: 0209-man-include-autoconf-snippet-in-daemon-7.patch
Patch210: 0210-systemd-python-fix-setting-of-exception-codes.patch
Patch211: 0211-systemd-python-fix-listen_fds-under-Python-2.patch
Patch212: 0212-man-expand-on-some-more-subtle-points-in-systemd.soc.patch
Patch213: 0213-tmpfiles-rename-unsafe-to-boot.patch
Patch214: 0214-sleep-config-Dereference-pointer-before-check-for-NU.patch
Patch215: 0215-sleep-config-fix-double-free.patch
Patch216: 0216-rules-drivers-do-not-reset-RUN-list.patch
Patch217: 0217-core-manager-print-info-about-interesting-signals.patch
Patch218: 0218-core-service-check-if-mainpid-matches-only-if-it-is-.patch
Patch219: 0219-man-typo-fix.patch
Patch220: 0220-swap-remove-if-else-with-the-same-data-path.patch
Patch221: 0221-hwdb-update.patch
Patch222: 0222-journal-Add-missing-byte-order-conversions.patch
Patch223: 0223-hwdb-change-key-mappings-for-Samsung-90X3A.patch
Patch224: 0224-hwdb-add-Samsung-700G.patch
Patch225: 0225-hwdb-remove-duplicate-entry-for-Samsung-700Z.patch
Patch226: 0226-hwdb-fix-match-for-Thinkpad-X201-tablet.patch
Patch227: 0227-keymap-Recognize-different-Toshiba-Satellite-capital.patch
Patch228: 0228-sleep.c-fix-typo.patch
Patch229: 0229-delta-ensure-that-d_type-will-be-set-on-every-fs.patch
Patch230: 0230-tmpfiles-don-t-allow-label_fix-to-print-ENOENT-when-.patch
Patch231: 0231-man-mention-which-variables-will-be-expanded-in-Exec.patch
Patch232: 0232-hwdb-Add-support-for-Toshiba-Satellite-P75-A7200-key.patch
Patch233: 0233-journal-fix-access-to-munmapped-memory-in-sd_journal.patch
Patch234: 0234-gpt-auto-generator-skip-nonexistent-devices.patch
Patch235: 0235-gpt-auto-generator-use-EBADSLT-code-when-unable-to-d.patch
Patch236: 0236-journald-do-not-free-space-when-disk-space-runs-low.patch
Patch237: 0237-man-add-busctl-1.patch
Patch238: 0238-journalctl-flip-to-full-by-default.patch
Patch239: 0239-coredumpctl-in-case-of-error-free-pattern-after-prin.patch
Patch240: 0240-shell-completion-remove-load-from-systemctl.patch
Patch241: 0241-units-drop-Install-section-from-multi-user.target-an.patch
Patch242: 0242-systemctl-skip-native-unit-file-handling-if-sysv-fil.patch
Patch243: 0243-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch244: 0244-udev-static_node-do-not-exit-rule-after-first-static.patch
Patch245: 0245-cryptsetup-Support-key-slot-option.patch
Patch246: 0246-pam_systemd-Ignore-vtnr-when-seat-seat0.patch
Patch247: 0247-keymap-Add-HP-Chromebook-14-Falco.patch
Patch248: 0248-keymap-Add-release-quirk-for-Acer-AOA-switchvideomod.patch
Patch249: 0249-keymap-Add-Sony-Vaio-VGN-FW250.patch
Patch250: 0250-keymap-Add-Toshiba-EQUIUM.patch
Patch251: 0251-tmpfiles-fix-memory-leak-of-exclude_prefixes.patch
Patch252: 0252-analyze-fix-plot-issues-when-using-gummiboot.patch
Patch253: 0253-udev-add-zram-to-the-list-of-devices-inappropriate-f.patch
Patch254: 0254-bash-completion-fix-completion-of-complete-verbs.patch
Patch255: 0255-shell-completion-fix-completion-of-localectl-set-loc.patch
Patch256: 0256-zsh-completions-kernel-install-only-show-existing-ke.patch
Patch257: 0257-core-fix-crashes-if-locale.conf-contains-invalid-utf.patch
Patch258: 0258-core-do-not-print-invalid-utf-8-in-error-messages.patch
Patch259: 0259-cryptsetup-generator-auto-add-deps-for-device-as-pas.patch
Patch260: 0260-man-fix-reference-in-systemd-inhibit-1.patch
Patch261: 0261-man-fix-another-reference-in-systemd-inhibit-1.patch
Patch262: 0262-fstab-generator-Create-fsck-root-symlink-with-correc.patch
Patch263: 0263-efi-fix-Undefined-reference-efi_loader_get_boot_usec.patch
Patch264: 0264-core-make-StopWhenUnneeded-work-in-conjunction-with-.patch
Patch265: 0265-man-always-place-programlisting-and-programlisting-i.patch
Patch266: 0266-Temporary-work-around-for-slow-shutdown-due-to-unter.patch
Patch267: 0267-pam-module-fix-warning-about-ignoring-vtnr.patch
Patch268: 0268-pam_systemd-do-not-set-XDG_RUNTIME_DIR-if-the-sessio.patch
Patch269: 0269-core-do-not-segfault-if-proc-swaps-cannot-be-opened.patch
Patch270: 0270-Revert-login-Don-t-stop-a-running-user-manager-from-.patch
Patch271: 0271-Revert-journalctl-flip-to-full-by-default.patch
Patch272: 0272-util-fix-handling-of-trailing-whitespace-in-split_qu.patch
Patch273: 0273-udev-net_id-Introduce-predictable-network-names-for-.patch
Patch274: 0274-utils-silence-the-compiler-warning.patch
Patch275: 0275-fix-SELinux-check-for-transient-units.patch
Patch276: 0276-s390-getty-generator-initialize-essential-system-ter.patch
Patch277: 0277-pam-use-correct-log-level.patch
Patch278: 0278-nspawn-if-we-don-t-find-bash-try-sh.patch
Patch279: 0279-units-systemd-logind-fails-hard-without-dbus.patch
Patch280: 0280-man-fix-grammatical-errors-and-other-formatting-issu.patch
Patch281: 0281-man-replace-STDOUT-with-standard-output-etc.patch
Patch282: 0282-man-use-spaces-instead-of-tabs.patch
Patch283: 0283-macro-add-a-macro-to-test-whether-a-value-is-in-a-sp.patch
Patch284: 0284-core-fix-property-changes-in-transient-units.patch
Patch285: 0285-core-more-exact-test-on-the-procfs-special-string-de.patch
Patch286: 0286-doc-update-punctuation.patch
Patch287: 0287-doc-resolve-missing-extraneous-words-or-inappropriat.patch
Patch288: 0288-doc-choose-different-words-to-improve-clarity.patch
Patch289: 0289-doc-properly-use-XML-entities.patch
Patch290: 0290-man-machinectl-there-is-no-command-kill-machine.patch
Patch291: 0291-load-modules-properly-return-a-failing-error-code-if.patch
Patch292: 0292-machinectl-add-bash-completion.patch
Patch293: 0293-delta-add-bash-completion.patch
Patch294: 0294-man-document-MAINPID.patch
Patch295: 0295-man-busctl-typo-fix.patch
Patch296: 0296-journal-don-t-clobber-return-parameters-of-sd_journa.patch
Patch297: 0297-udev-make-sure-we-always-return-a-valid-error-code-i.patch
Patch298: 0298-bootctl-add-bash-completion.patch
Patch299: 0299-selinux-Don-t-attempt-to-load-policy-in-initramfs-if.patch
Patch300: 0300-man-there-is-no-ExecStopPre-for-service-units.patch
Patch301: 0301-man-document-that-per-interface-sysctl-variables-are.patch
Patch302: 0302-journal-downgrade-vaccuum-message-to-debug-level.patch
Patch303: 0303-core-gc-half-created-stub-units.patch
Patch304: 0304-getty-generator-verify-ttys-before-we-make-use-of-th.patch
Patch305: 0305-units-serial-getty-.service-add-Install-section.patch
Patch306: 0306-README-document-that-var-run-must-be-a-symlink-run.patch
Patch307: 0307-Use-var-run-dbus-system_bus_socket-for-the-D-Bus-soc.patch
Patch308: 0308-mount-don-t-send-out-PropertiesChanged-message-if-ac.patch
Patch309: 0309-mount-don-t-fire-PropertiesChanged-signals-for-mount.patch
Patch310: 0310-logs-show-fix-corrupt-output-with-empty-messages.patch
Patch311: 0311-journalctl-refuse-extra-arguments-with-verify-and-si.patch
Patch312: 0312-cdrom_id-use-the-old-MMC-fallback.patch
Patch313: 0313-udev-rules-setup-tty-permissions-and-group-for-sclp_.patch
Patch314: 0314-bash-add-completion-for-systemd-nspawn.patch
Patch315: 0315-add-bash-completion-for-systemd-cgls.patch
Patch316: 0316-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch317: 0317-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch318: 0318-Allow-fractional-parts-in-disk-sizes.patch
Patch319: 0319-add-bash-completion-for-systemd-cgtop.patch
Patch320: 0320-execute-free-directory-path-if-we-fail-to-remove-it-.patch
Patch321: 0321-add-bash-completion-for-systemd-detect-virt.patch
Patch322: 0322-Do-not-print-invalid-UTF-8-in-error-messages.patch
Patch323: 0323-add-bash-completion-for-systemd-cat.patch
Patch324: 0324-journal-assume-that-next-entry-is-after-previous-ent.patch
Patch325: 0325-journal-forget-file-after-encountering-an-error.patch
Patch326: 0326-logind-ignore-failing-close-on-session-devices.patch
Patch327: 0327-core-introduce-new-stop-protocol-for-unit-scopes.patch
Patch328: 0328-core-watch-SIGCHLD-more-closely-to-track-processes-o.patch
Patch329: 0329-logind-rework-session-shutdown-logic.patch
Patch330: 0330-logind-order-all-scopes-after-both-systemd-logind.se.patch
Patch331: 0331-logind-given-that-we-can-now-relatively-safely-shutd.patch
Patch332: 0332-logind-fix-reference-to-systemd-user-sessions.servic.patch
Patch333: 0333-logind-add-forgotten-call-to-user_send_changed.patch
Patch334: 0334-logind-save-session-after-setting-the-stopping-flag.patch
Patch335: 0335-logind-save-user-state-after-stopping-the-session.patch
Patch336: 0336-logind-initialize-timer_fd.patch
Patch337: 0337-logind-pass-pointer-to-User-object-to-user_save.patch
Patch338: 0338-core-allow-PIDs-to-be-watched-by-two-units-at-the-sa.patch
Patch339: 0339-core-correctly-unregister-PIDs-from-PID-hashtables.patch
Patch340: 0340-logind-uninitialized-timer_fd-is-set-to-1.patch
Patch341: 0341-logind-add-forgotten-return-statement.patch
Patch342: 0342-core-fix-detection-of-dead-processes.patch
Patch343: 0343-Fix-prototype-of-get_process_state.patch
Patch344: 0344-core-check-for-return-value-from-get_process_state.patch
Patch345: 0345-man-update-link-to-LSB.patch
Patch346: 0346-man-systemd-bootchart-fix-spacing-in-command.patch
Patch347: 0347-man-add-missing-comma.patch
Patch348: 0348-build-sys-Don-t-distribute-generated-udev-rule.patch
Patch349: 0349-units-Do-not-unescape-instance-name-in-systemd-backl.patch
Patch350: 0350-util-add-timeout-to-generator-execution.patch
Patch351: 0351-input_id-Recognize-buttonless-joystick-types.patch
Patch352: 0352-logind-fix-policykit-checks.patch
Patch353: 0353-nspawn-don-t-try-mknod-of-dev-console-with-the-corre.patch
Patch354: 0354-build-sys-Find-the-tools-for-users-with-no-sbin-usr-.patch
Patch355: 0355-rules-mark-loop-device-as-SYSTEMD_READY-0-if-no-file.patch
Patch356: 0356-man-multiple-sleep-modes-are-to-be-separated-by-whit.patch
Patch357: 0357-man-fix-description-of-systemctl-after-before.patch
Patch358: 0358-udev-properly-detect-reference-to-unexisting-part-of.patch
Patch359: 0359-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch360: 0360-gpt-auto-generator-don-t-return-OOM-on-parentless-de.patch
Patch361: 0361-man-improve-wording-of-systemctl-s-after-before.patch
Patch362: 0362-cgroup-it-s-not-OK-to-invoke-alloca-in-loops.patch
Patch363: 0363-hwdb-update.patch
Patch364: 0364-core-don-t-try-to-relabel-mounts-before-we-loaded-th.patch
Patch365: 0365-man-explain-that-the-journal-field-SYSLOG_IDENTIFIER.patch
Patch366: 0366-man-be-more-specific-when-EnvironmentFile-is-read.patch
Patch367: 0367-systemctl-kill-mode-is-long-long-gone-don-t-mention-.patch
Patch368: 0368-systemctl-add-more-verbose-explanation-of-kill-who-a.patch
Patch369: 0369-ask-password-when-the-user-types-a-overly-long-passw.patch
Patch370: 0370-util-consider-both-fuse.glusterfs-and-glusterfs-netw.patch
Patch371: 0371-core-do-not-read-system-boot-timestamps-in-systemd-u.patch
Patch372: 0372-hwdb-Update-database-of-Bluetooth-company-identifier.patch
Patch373: 0373-Add-hwdb-entry-for-Samsung-Series-7-Ultra.patch
Patch374: 0374-udev-do-not-export-static-node-tags-for-non-existing.patch
Patch375: 0375-journalctl-free-arg_file-on-exit.patch
Patch376: 0376-journal-fix-export-of-messages-containing-newlines.patch
Patch377: 0377-tty-ask-password-agent-return-negative-errno.patch
Patch378: 0378-systemd-python-use-.hex-instead-of-.get_hex.patch


# (cg/bor) clean up directories on boot as done by rc.sysinit
# - Lennart should be poked about this (he couldn't think why he hadn't done it already)
Patch500: 0500-Clean-directories-that-were-cleaned-up-by-rc.sysinit.patch
Patch501: 0501-main-Add-failsafe-to-the-sysvinit-compat-cmdline-key.patch
Patch502: 0502-mageia-Fallback-message-when-display-manager-fails.patch
Patch503: 0503-Disable-modprobe-pci-devices-on-coldplug-for-storage.patch
Patch504: 0504-Allow-booting-from-live-cd-in-virtualbox.patch
Patch505: 0505-reinstate-TIMEOUT-handling.patch
Patch506: 0506-udev-Allow-the-udevadm-settle-timeout-to-be-set-via-.patch
Patch507: 0507-Mageia-Relax-perms-on-sys-kernel-debug-for-lspcidrak.patch
Patch508: 0508-udev-rules-Apply-SuSE-patch-to-restore-cdrom-cdrw-dv.patch
Patch509: 0509-pam_systemd-Always-reset-XDG_RUNTIME_DIR.patch
Patch510: 0510-logind-Partial-backport-of-cc377381.patch
Patch511: 0511-pam-Suppress-errors-in-the-SuSE-patch-to-unset-XDG_R.patch
Patch512: 0512-Revert-systemctl-skip-native-unit-file-handling-if-s.patch
Patch513: 0513-systemctl-Do-not-attempt-native-calls-for-enable-dis.patch
Patch514: 0514-systemctl-Ensure-the-no-reload-and-no-redirect-optio.patch

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
# (cg) don't add more deps for now but add this when cauldron reopens.
#BuildRequires:	pkgconfig(libqrencode)
Requires(pre):	filesystem >= 2.1.9-18
Requires(pre):	shadow-utils
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
Requires:	chkconfig > 1.3.61-2
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

%package -n nss-myhostname
Summary:	systemd provided glibc plugin for local system host name resolution
Group:		System/Base

%description -n nss-myhostname
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

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
  --with-rc-local-script-path-start=/etc/rc.d/rc.local \
  --enable-chkconfig \
  --disable-static \
  --disable-selinux \
  --with-firmware-path=%{_prefix}/lib/firmware/updates:%{_prefix}/lib/firmware

%make

%install
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
mkdir -p %{buildroot}%{_sysconfdir}/udev
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin

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


%triggerin -- glibc
# reexec daemon on self or glibc update to avoid busy / on shutdown
# trigger is executed on both self and target install so no need to have
# extra own post
if [ $1 -ge 2 -o $2 -ge 2 ] ; then
	%{_bindir}/systemctl daemon-reexec 2>&1 || :
fi

%pre
# (cg) Cannot use rpm-helper scripts as it results in a cyclical dep as
# rpm-helper requires systemd-units which in turn requires systemd...
if ! getent group %{name}-journal >/dev/null 2>&1; then
  /usr/sbin/groupadd -r %{name}-journal >/dev/null || :
fi

# Write on first install or upgrade from MGA3.
if [ ! -r %{_prefix}/lib/sysctl.d/50-default.conf ]; then
  if [ ! -d %{_sysconfdir}/sysctl.d ]; then
    mkdir -m 0755 %{_sysconfdir}/sysctl.d
  fi
  cat > %{_sysconfdir}/sysctl.d/51-alt-sysrq.conf << EOF
# This file ensures that the Alt+SysRq Magic keys still work.
# This setting is insecure, although commonly expected and you can remove this
# file to disable this feature. It will not be readded on future systemd
# upgrades/updates.
# http://en.wikipedia.org/wiki/Magic_SysRq_key#Security
kernel.sysrq = 1
EOF

fi

%post
%{_bindir}/systemd-machine-id-setup > /dev/null 2>&1 || :
%{_prefix}/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :
#%{_bindir}/systemctl daemon-reexec > /dev/null 2>&1 || :
%{_bindir}/udevadm hwdb --update >/dev/null 2>&1 || :
%{_bindir}/journalctl --update-catalog >/dev/null 2>&1 || :

if [ $1 == 1 ]; then
	# On first install process all tmpfiles that may have been installed before us
	# Hard requires on some packages on systemd might make cyclic deps on early
	# transactions.
	# We avoid systemd.conf so as not to create /run/nologin
	# NOTE We can probably revert to using filetriggers again for tmpfiles now that
	#      there is a --boot option which should make running --create without a
	#      basename config nice and safe.
	for tmpfile in %{_prefix}/lib/tmpfiles.d/*.conf; do
		if [ -f "$tmpfile" -a "$tmpfile" != "%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf" ]; then
			/usr/bin/systemd-tmpfiles --create $(basename "$tmpfile")
		fi
	done
fi

# (blino) systemd 195 changed the prototype of logind's OpenSession()
# see http://lists.freedesktop.org/archives/systemd-devel/2012-October/006969.html
# and http://cgit.freedesktop.org/systemd/systemd/commit/?id=770858811930c0658b189d980159ea1ac5663467
%triggerun -- %{name} < 195-4.mga3
%{_bindir}/systemctl restart systemd-logind.service

# (cg) mageia 4 introduces the Consistent Network Device Names feature
# https://wiki.mageia.org/en/Feature:NetworkDeviceNameChange
# To prevent it being enabled on upgrades and breaking configs, we ensure the
# feature is disabled when we detect an older version of systemd being removed.
%triggerun -- %{name} < 206
echo >&2
echo "Disabling Persistent Network Device Names due to upgrade." >&2
echo "To enable, rm %{_sysconfdir}/udev/rules.d/80-net-name-slot.rules and your" >&2
echo "%{_sysconfdir}/udev/rules.d/70-persistent-net.rules files." >&2
echo "Note: Some reconfiguration of firewall and network config scripts will also" >&2
echo "      be required if you do this" >&2
echo >&2
mkdir -p %{_sysconfdir}/udev/rules.d >/dev/null 2>&1 || :
ln -s /dev/null %{_sysconfdir}/udev/rules.d/80-net-name-slot.rules >/dev/null 2>&1 || :

%triggerun -- %{name} < 208
chgrp -R systemd-journal /var/log/journal || :
chmod 02755 /var/log/journal || :
if [ -f /etc/machine-id ]; then
	chmod 02755 /var/log/journal/$(cat /etc/machine-id) || :
fi

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
                getty@tty1.service \
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

%triggerin units -- %{name}-units < 35-1
# Enable the services we install by default.
        %{_bindir}/systemctl --quiet enable \
                hwclock-load.service \
                getty@tty1.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service \
                2>&1 || :
# rc-local is now enabled by default in base package
rm -f %_sysconfdir/systemd/system/multi-user.target.wants/rc-local.service || :


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
%ghost %{_sysconfdir}/udev/hwdb.bin
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
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.machine1.conf
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%{_sysconfdir}/pam.d/%{name}-user
%dir %{_sysconfdir}/udev/rules.d
# (cg) NB See pre script for soemthing that relies on this name...
# If it is ever renamed, change the pre script too
%{_prefix}/lib/sysctl.d/50-default.conf
#%{_prefix}/lib/sysctl.d/50-coredump.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
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
%{_bindir}/machinectl
%{_bindir}/systemd
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-coredumpctl
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-notify
%{_bindir}/systemd-run
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
%{_mandir}/man1/bootctl.*
%{_mandir}/man1/busctl.*
%{_mandir}/man1/hostnamectl.*
%{_mandir}/man1/journalctl.*
%{_mandir}/man1/localectl.*
%{_mandir}/man1/loginctl.*
%{_mandir}/man1/machinectl.*
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
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
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
%attr(02755,root,systemd-journal) %dir %{_logdir}/journal

%files units
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
%{_datadir}/zsh/site-functions
%{_sysconfdir}/profile.d/40systemd.sh
%{_sysconfdir}/modules-load.d/*.conf
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%{_mandir}/man1/systemctl.*

%files -n python-%{name}
%{py_platsitedir}/%{name}

%files devel
%{_includedir}/systemd
%{_libdir}/libsystemd-*.so
%{_libdir}/pkgconfig/libsystemd-*.pc
%{_datadir}/pkgconfig/systemd.pc
%{_prefix}/lib/rpm/macros.d/macros.systemd

%files -n nss-myhostname
%{_mandir}/man8/nss-myhostname.*
%{_libdir}/libnss_myhostname.so.2

%files -n %{libdaemon}
%{_libdir}/libsystemd-daemon.so.%{libdaemon_major}*

%files -n %{liblogin}
%{_libdir}/libsystemd-login.so.%{liblogin_major}*

%files -n %{libjournal}
%{_libdir}/libsystemd-journal.so.%{libjournal_major}*

%files -n %{libid128}
%{_libdir}/libsystemd-id128.so.%{libid128_major}*

%files -n %{libudev}
%{_libdir}/libudev.so.%{libudev_major}*

%files -n %{libudev_devel}
%{_libdir}/libudev.so
%{_includedir}/libudev.h
%{_datadir}/pkgconfig/udev.pc
%{_libdir}/pkgconfig/libudev.pc

%files -n %{libgudev}
%{_libdir}/libgudev-%{libgudev_api}.so.%{libgudev_major}*

%files -n %{libgudev_gir}
%{_libdir}/girepository-1.0/GUdev-%{libgudev_api}.typelib

%files -n %{libgudev_devel}
%{_libdir}/libgudev-%{libgudev_api}.so
%{_includedir}/gudev-%{libgudev_api}
%{_libdir}/pkgconfig/gudev-%{libgudev_api}.pc
%{_datadir}/gir-1.0/GUdev-%{libgudev_api}.gir
