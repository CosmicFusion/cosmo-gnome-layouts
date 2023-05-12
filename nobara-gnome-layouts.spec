BuildArch:              noarch

Name:          nobara-gnome-layouts
Version:       2.2
Release:       2%{?dist}
License:       GPLv2
Group:         System Environment/Libraries
Summary:       Nobara's Gnome layouts App


URL:           https://github.com/CosmicFusion/cosmo-gnome-layouts

Source0:        %{name}-%{version}.tar.gz

BuildRequires:	wget
Requires: /usr/bin/bash
Requires: python3
Requires: python
Requires: gtk3
Requires: gnome-shell
Requires: dconf
Requires: glib2
Requires: python3-gobject
Requires: zenity

# Extensions
Requires: gnome-shell-extension-launch-new-instance
Requires: gnome-shell-extension-just-perfection
Requires: gnome-shell-extension-arc-menu
Requires: gnome-shell-extension-dash-to-dock
Requires: gnome-shell-extension-launch-new-instance
Requires: gnome-shell-extension-places-menu
Requires: gnome-shell-extension-dash-to-panel
Requires: gnome-shell-extension-desktop-icons
Requires: gnome-shell-extension-window-list
Requires: gnome-shell-extension-custom-accent-colors

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/
mv etc %{buildroot}/
mkdir -p %{buildroot}/usr/share/licenses/nobara-gnome-layouts
wget https://raw.githubusercontent.com/CosmicFusion/cosmo-gnome-layouts/main/LICENSE.md -O %{buildroot}/usr/share/licenses/nobara-gnome-layouts/LICENSE

%description
Nobara's Python3 & GTK3 built Gnome layouts App
%files
%attr(0755, root, root) "/usr/bin/nobara-gnome-layouts"
%attr(0644, root, root) "/usr/share/glib-2.0/schemas/org.nobara.layouts.gschema.xml"
%attr(0755, root, root) "/etc/nobara/scripts/nobara-layouts/*"
%attr(0644, root, root) "/usr/share/licenses/nobara-gnome-layouts/LICENSE"
%attr(0644, root, root) "/usr/share/applications/nobara-gnome-layouts.desktop"

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/
