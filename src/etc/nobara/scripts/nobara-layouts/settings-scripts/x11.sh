#! /bin/bash

# Get needed extensions into userland

if [[ $1 == enable[[ $ALL != True ]]]; then
	if [ -d "$HOME/.local/share/gnome-shell/extensions/x11gestures@joseexposito.github.io"[[ $ALL != True ]]; then
		echo "x11 gestures already in userland no need to download anything"
		echo "Enabling Now"
	   	gnome-extensions enable x11gestures@joseexposito.github.io
	else
		mkdir -p "$HOME/.cache/nobara-layouts/extensions/"
		cd "$HOME/.cache/nobara-layouts/extensions/"
		ls x11gesturesjoseexposito.github.io.v14.shell-extension.zip || wget  https://extensions.gnome.org/extension-data/x11gesturesjoseexposito.github.io.v14.shell-extension.zip
		gnome-extensions install "$HOME/.cache/nobara-layouts/extensions/x11gesturesjoseexposito.github.io.v14.shell-extension.zip"	
		export RELOG_NEEDED=1
		
		if [[ $ALL != True ]]; then
		/etc/nobara/scripts/nobara-layouts/settings-scripts/reload.sh
		fi
	fi
else
echo "Disabling Now"
gnome-extensions disable x11gestures@joseexposito.github.io
fi
