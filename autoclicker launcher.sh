#!/bin/bash

if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
  zenity --warning --text="This autoclicker requires an X11 session, but you're on Wayland.\n\nPlease log out and choose 'GNOME on Xorg' or 'X11' from the login screen."
  exit 1
fi

#!/bin/bash
cd "$(dirname "$0")"
"$(which python3)" autoclicker.py

