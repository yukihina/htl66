## Patch file - Enables family relationship terms (Mom, Dad, Sister, etc.)
## This file must be distributed separately as patch.rpa
##
## IMPORTANT: init -1003 runs BEFORE def_chars.rpy (-1002) to ensure
## persistent.patch_applied is True when character definitions are created

init -1003 python:
    # Set the persistent flag that def_chars.rpy checks
    renpy.persistent.patch_applied = True

    # Also set patch_activated for compatibility
    global patch_activated
    patch_activated = True