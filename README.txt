=====================================================
 SUDOSWARM MACRO - for Bee Swarm Simulator on Linux
=====================================================

This is an automatic gathering macro for Bee Swarm Simulator,
made for Linux (Linux Mint is what it was built and tested on).
Everything on your computer can be fresh - the only thing you
need to already have installed is the Roblox client "Sober".

--------------------------------------------------------------------------------
WHAT YOU NEED BEFORE STARTING
--------------------------------------------------------------------------------
- Linux (this guide is for Linux Mint, Ubuntu, and other Ubuntu-style distros)
- The Sober app installed, and Roblox working in it
- An internet connection for the first-time setup (one time only)

--------------------------------------------------------------------------------
STEP 1 - DOWNLOAD AND EXTRACT
--------------------------------------------------------------------------------
1. On the GitHub page, press the green "Code" button and choose
   "Download ZIP" (or download SudoSwarm-Macro.zip wherever it is shared).
2. Right-click the downloaded zip and choose "Extract Here"
   (or "Extract to..."). You MUST end up with a FOLDER - opening the
   zip alone is not enough!
   NOTE: a GitHub download usually extracts to a folder called
   SudoSwarm-Macro-main - that is fine, just remember the name.
3. Leave it in Downloads, or move the folder somewhere permanent
   like your Home folder.
4. Check it: inside the folder there should be 5 files
   (run.sh, macro_test.py, gui_background.webp, title_icon.png, README.txt)

--------------------------------------------------------------------------------
STEP 2 - ONE-TIME SYSTEM SETUP
--------------------------------------------------------------------------------
A fresh Linux install is missing 3 small things. Copy-paste this whole
command into a Terminal and press Enter:

    sudo apt update && sudo apt install -y python3-venv python3-tk xdotool

(New to the Terminal? Open one with Ctrl + Alt + T. The command asks for
your password - while typing it, nothing shows on screen. That is normal.)

--------------------------------------------------------------------------------
STEP 3 - START THE MACRO
--------------------------------------------------------------------------------
IN THE TERMINAL, type these two lines (press Enter after each):

    cd ~/Downloads/SudoSwarm-Macro
    ./run.sh

- "cd" moves the terminal into the folder you extracted. If the GitHub
  download extracted to SudoSwarm-Macro-main, use that name instead:
      cd ~/Downloads/SudoSwarm-Macro-main
  (if you moved the folder somewhere else, adjust the path)

IF THE FIRST LINE FAILS with "No such file or directory":
the folder is not in Downloads. Easiest fix for beginners:
1. Type   cd    (with ONE space after it, do NOT press Enter yet)
2. Drag the extracted SudoSwarm-Macro folder from the file manager straight
   into the Terminal - the real path pastes itself in
3. Press Enter, then continue with   ./run.sh

THE FIRST START downloads the Python modules the macro needs.
This takes 1-3 minutes and only happens once. You will see:
    First run detected - setting up the macro...
Then the SudoSwarm Macro window appears.

NOTE: if the terminal says "Permission denied", run this once, then try again:
    chmod +x run.sh

Every time after that, opening the macro is just:
    cd (folder)   then   ./run.sh
The window must stay open while the macro runs - pressing its X closes it.

--------------------------------------------------------------------------------
STEP 4 - USING THE MACRO WINDOW
--------------------------------------------------------------------------------
The SudoSwarm Macro window has:

  Select Target Field     - the field the macro will gather in
                            (17 fields supported)
  Select Your Sprinkler   - which sprinkler you own. It MUST be in your
                            hotbar slot 1 for all fields.
  Movement Pattern        - "Line Method" sweeps back and forth,
                            "Box Outline Method" sweeps in a square
  Gather Time (Minutes)   - minutes of gathering per visit (2 is a good start)
  Movespeed (Min 20)      - your in-game Movement Speed status. Same as game,
                            minimum value 20, exact match = exact routes
  Security Mode           - see below

Then:
  START AUTOMATIC HARVEST - begins the macro (you see it print status in
                            the terminal, that is normal and useful)
  STOP MACRO              - stops the macro instantly at any time

HOW A RUN GOES:
1. Put the game window on the screen (do NOT keep it minimized)
2. Click START, click into the Sober/Roblox window so it has keyboard focus,
   and keep the mouse cursor INSIDE the game window
3. The macro resets your character to the hive (Esc, R, Enter), walks to the
   field with cannon or walk-in start, and gathers until the gather time
   is up, then returns to the hive and repeats
4. To do another field, press STOP, pick the next field, press START

--------------------------------------------------------------------------------
SECURITY MODE (SCREEN LOCK)
--------------------------------------------------------------------------------
Security Mode = No (default):  if something stops the macro, it just stops.
Security Mode = Yes:           if your cursor moves out of the game window
                               (or the game loses keyboard focus), the macro
                               stops AND the screen locks, so nobody can use
                               your session while you are away. Unlock with
                               your password and press START again.

Useful if you leave the computer running and walk away all night.
Note: the choice resets to No every time you open the macro.

--------------------------------------------------------------------------------
EMERGENCY STOP (ALWAYS WORKS)
--------------------------------------------------------------------------------
Slam your mouse into any corner of the screen. PyAutoGUI's fail-safe kills
the macro and every held key/mouse click is released.

--------------------------------------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------------------------------------
The terminal says "No such file or directory" on the cd line
    The extracted folder isn't at ~/Downloads/SudoSwarm-Macro. Use the
    drag-and-drop trick from Step 3, or find where you extracted it and use
    that folder in the cd command instead.

"Permission denied" when running ./run.sh
    Run:  chmod +x run.sh   then start again with ./run.sh

"[SUDOSWARM] This copy of the macro is corrupted or was edited."
    The macro_test.py file was changed or the download was cut short.
    Download the macro again and extract it fresh - do not edit the file;
    it is machine-generated on purpose and cannot be hand-modified.

The terminal says to run the sudo apt install command
    Do exactly what it prints, then run ./run.sh again.

"Could not find the Roblox/Sober window"
    The Sober window is minimized or not open. Open Roblox into the game and
    keep the window visible (not minimized), then start again.

"Could not load the GUI background / GUI title icon"
    The file gui_background.webp or title_icon.png was deleted or renamed -
    put it back, or ignore it (the macro still works, with a plain
    background / no icon next to the title).

The macro stops itself with a message like "the mouse cursor left the
Roblox/Sober window..."
    It is working as designed: your cursor/hover left the game window.
    Move the cursor back in and press START to run again.

The window never appears at all / keyboard presses go to the wrong place
    You are probably running a Wayland session. The macro needs X11. Check
    with:  echo $XDG_SESSION_TYPE   (must say x11; Linux Mint's default is X11)

The routes drift / character misses the field
    Make sure Movespeed EXACTLY matches your in-game Movement Speed status,
    and that speed-changing extras ( movement speed boosts, Hidden Tiles etc.)
    are not altering your speed while it runs. Every route is matched to your
    exact Movespeed value (minimum 20).

Different Linux (Fedora, Arch, etc.)
    The macro works on any X11 Linux. Install the same three things with your
    distro's package manager, e.g.:
      Fedora:  sudo dnf install python3-tkinter xdotool
      Arch:    sudo pacman -S python-pip tk xdotool
    The ./run.sh script handles everything else automatically.

--------------------------------------------------------------------------------
ALWAYS REMEMBER
--------------------------------------------------------------------------------
- Every macro risks a BAN on Roblox. Use it at your own risk on your own
  account (a throwaway/secondary account is sensible).
- Keep the game window visible at all times, mouse inside the game window.
- Don't maximize to fullscreen; windowed mode is what the routes are aimed at
  (a window around 800x600 works well).
- This macro only presses your keyboard/mouse - it does not read game files,
  does not talk to the internet, and stores nothing on your PC.
=====================================================
Have fun and happy farming!
=====================================================
