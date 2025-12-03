# Hard to Love v0.28 - Script Bugfix Patch

## What This Patch Fixes

This patch fixes critical bugs in Hard to Love v0.28:

1. **Episode 6 TypeError** (line 2698 in ep06.rpy)
   - Fixed: `TypeError: %c requires int or char` error in Madison's dialogue
   - Issue: Unescaped `%` character in "1% chance" text caused formatting error

2. **Episode 4 Image Display Bug** (ep04_nanmad23)
   - Fixed: Image condition order in ep04_images.rpy
   - Issue: Image displayed incorrectly compared to ep04_nanmad22 and ep04_madnan01
   - The ConditionSwitch had conditions in wrong order, causing wrong variant to display

## Installation Instructions

### ⚠️ IMPORTANT: Back Up Your Original File First!

Before installing this patch, **create a backup** of your original `scripts.rpa` file:

1. Navigate to your game installation folder
2. Open the `game` subfolder
3. Find the file named `scripts.rpa`
4. **Copy it to a safe location** (e.g., rename it to `scripts.rpa.backup`)

### Installation Steps

1. **Download** the bugfix `scripts.rpa` file (approximately 180 MB)

2. **Locate your game folder:**
   - Windows: Usually `C:\Program Files\HardtoLove\` or wherever you installed the game
   - Mac: Right-click the app → "Show Package Contents" → Navigate to `Contents/Resources/autorun/`
   - Linux: Your game installation directory

3. **Open the `game` subfolder** inside your game installation folder

4. **Replace the file:**
   - Delete or rename the old `scripts.rpa` file
   - Copy the new `scripts.rpa` from this patch into the `game` folder

5. **Launch the game** - The bugs should now be fixed!

### ⚠️ DO NOT Extract or Rename the File

- The file **MUST** be named exactly `scripts.rpa`
- Do **NOT** extract or unpack the `.rpa` file
- Do **NOT** try to install individual `.rpy` or `.rpyc` files
- The `.rpa` file is an archive that Ren'Py reads directly

## Compatibility

- **Game Version:** v0.28 only
- **Save Files:** Your existing saves should work fine with this patch
- **Platforms:** Windows, Mac, Linux

## Verification

After installation, you can verify the fix is working:

1. Load a save or start a new game
2. Play through Episode 6 - Madison's dialogue should display without errors
3. In Episode 4, the Nana/Madison image variants should display correctly based on your choices

## Troubleshooting

### Game won't start after installing patch

1. Make sure the file is named exactly `scripts.rpa` (not `scripts.rpa.rpa` or any other variation)
2. Make sure it's in the `game` folder, not the root game folder
3. Restore your backup `scripts.rpa` and try the installation again

### Getting errors about missing files

- This patch only updates scripts, not images or audio
- Make sure you're using the **full v0.28 game** as the base
- This is not a standalone version

### Still seeing the bugs

1. Verify you replaced the correct `scripts.rpa` file in the `game` folder
2. Close and restart the game completely
3. If using old saves, try advancing past the problematic scene

## Rollback Instructions

If you experience any issues:

1. Delete the new `scripts.rpa` from the `game` folder
2. Restore your backup (`scripts.rpa.backup`) by renaming it back to `scripts.rpa`
3. Your game will return to its original state

## File Information

- **File Name:** `scripts.rpa`
- **File Size:** ~180 MB
- **Location:** `game/scripts.rpa` (inside your game folder)
- **Version:** v0.28 bugfix

## Support

If you encounter any issues not covered here, please report them with:
- Your operating system
- The exact error message (if any)
- What you were doing when the problem occurred

---

**Note:** This is an unofficial community bugfix patch. Always keep backups of your original game files.
