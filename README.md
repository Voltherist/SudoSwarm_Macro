# 🐝 SudoSwarm Macro — Bee Swarm Simulator auto-gathering for Linux

**SudoSwarm** is an automatic gathering macro for Bee Swarm Simulator (via the Linux Roblox client **Sober**).
Built for Linux Mint (Ubuntu-family X11 sessions). It walks your character to any of **17 supported fields**, deploys your sprinkler, and gathers honey hands-free — with safety stops, screen-lock security mode, and per-field tuned routes.

> ⚠️ **Use at your own risk.** Like any macro, using it can get your Roblox account banned. Use a secondary/throwaway account if you care about your main.

---

## ✨ What it does

- Walks to the field you choose using cannon (or W/S/D walk-in for Coconut & Pepper Field) and gathers on a tuned sweep pattern
- Choose **Line Method** (back-and-forth sweep) or **Box Outline Method** (square sweep)
- **Jump-cast sprinkler** layouts for Basic / Silver / Golden / Diamond Drenchers / Supreme Saturator (sprinkler must be in hotbar **slot 1**)
- Loops field → hive resets until your gather timer runs out, releasing every key instantly when it stops
- **Security Mode (optional):** if your cursor leaves the game window or the game loses keyboard focus, the macro stops **and locks your screen** (`cinnamon-screensaver-command -l`, with fallbacks) so guests can't use your session while you're away
- **Fail-safe:** slam your mouse into any screen corner → the macro dies and releases all keys
- 17 fields supported: Sunflower, Dandelion, Mushroom, Blue Flower, Clover, Spider, Strawberry, Bamboo, Pineapple, Pumpkin, Cactus, Rose, Pine Tree, Stump, Coconut, Pepper, Mountain Top

---

## 📥 How to install (fresh Linux, only Sober installed)

**1. Download this repository** — green **Code** button → **Download ZIP** → extract it
(GitHub usually creates a folder like `SudoSwarm_Macro-main` — that's fine)

**2. One-time system setup** — open a Terminal (`Ctrl + Alt + T`) and paste:

```bash
sudo apt update && sudo apt install -y python3-venv python3-tk xdotool
```

**3. Start the macro** (adjust the folder name if yours differs):

```bash
cd ~/Downloads/SudoSwarm_Macro-main
./run.sh
```

The first start installs the Python modules it needs (1–3 min, internet required, **one time only**). After that it launches instantly.
If `./run.sh` says `Permission denied`, run `chmod +x run.sh` once and try again.

---

## 🕹 How to use

Open the game window in Sober (keep it **windowed**, not minimized/fullscreen), click into the game so it has keyboard focus, then in the **SudoSwarm Macro** window:

| Setting | Meaning |
|---|---|
| Select Target Field | Where the macro gathers |
| Select Your Sprinkler | Must be in hotbar **slot 1** |
| Movement Pattern | Line Method or Box Outline Method |
| Gather Time (Minutes) | Minutes per harvest visit |
| Movespeed (Min 20) | **Must exactly match** your in-game Movement Speed status or routes drift |
| Security Mode | Yes = stop + screen lock if you walk away |

Press **START AUTOMATIC HARVEST**, keep the cursor inside the game window, and watch the terminal for status.
Press **STOP MACRO** to end it, or slam the mouse into a screen corner for an emergency kill.

While it runs, **keep the game window visible and the cursor inside it** — leaving either stops the macro by design (and with Security Mode = Yes, locks your screen).

---

## 🔒 About the protected code

`macro_test.py` ships as a **protected (obfuscated) build** — it looks like gibberish on purpose:

- It contains no readable source at rest and refuses to run if edited
- You never need to edit it — `run.sh` handles everything (venv setup, dependencies, launch)
- If you see `[SUDOSWARM] This copy of the macro is corrupted or was edited`, download a fresh copy

---

## 🧯 Troubleshooting (quick list)

| Problem | Fix |
|---|---|
| `cd: No such file or directory` | The extracted folder isn't in `~/Downloads` — type `cd ` (with a space), **drag the extracted folder into the Terminal**, press Enter |
| `Permission denied` on `./run.sh` | `chmod +x run.sh` |
| Macro asks for the `sudo apt install` command | Run exactly what it prints, then `./run.sh` again |
| "Could not find the Roblox/Sober window" | Open Roblox into the game; don't minimize the window |
| Keyboard presses land in the wrong place | You're on a **Wayland** session — the macro needs X11. Check `echo $XDG_SESSION_TYPE` (must say `x11`; Mint's default is X11) |
| Character misses the field | Movespeed does not match your in-game status |
| Other distro (Fedora/Arch) | `Fedora: sudo dnf install python3-tkinter xdotool` · `Arch: sudo pacman -S python-pip tk xdotool`, then `./run.sh` |

Everything you need is in this README - no other files required.

---

## 📄 License

Released under the **SudoSwarm Proprietary License** (see `LICENSE.md`):
free for **personal use by the original downloader** — no modification, no reverse engineering, no redistribution, no claiming it as your own, no commercial use. All rights reserved by [Voltherist](https://github.com/Voltherist).

---

*Made with vanilla Python + Tkinter + PyAutoGUI. No game files are read, nothing phones home, nothing is stored on your machine beyond the modules `run.sh` installs.*
