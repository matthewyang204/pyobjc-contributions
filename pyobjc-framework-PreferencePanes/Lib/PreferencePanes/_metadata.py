# This file is generated by objective.metadata
#
# Last update: Fri May 10 14:22:13 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$NSPrefPaneHelpMenuAnchorKey$NSPrefPaneHelpMenuInfoPListKey$NSPrefPaneHelpMenuTitleKey$NSPreferencePaneCancelUnselectNotification$NSPreferencePaneDoUnselectNotification$NSPreferencePaneSwitchToPaneNotification$NSPreferencePaneUpdateHelpMenuNotification$NSPreferencePrefPaneIsAvailableNotification$"""
enums = """$NSUnselectCancel@0$NSUnselectLater@2$NSUnselectNow@1$"""
misc.update(
    {"NSPreferencePaneUnselectReply": NewType("NSPreferencePaneUnselectReply", int)}
)
misc.update({})
misc.update(
    {
        "kNSPrefPaneHelpMenuAnchorKey": "anchor",
        "kNSPrefPaneHelpMenuTitleKey": "title",
        "kNSPrefPaneHelpMenuInfoPListKey": "NSPrefPaneHelpAnchors",
    }
)
aliases = {
    "kNSPrefPaneHelpMenuAnchorKey": "NSPrefPaneHelpMenuAnchorKey",
    "kNSPrefPaneHelpMenuTitleKey": "NSPrefPaneHelpMenuTitleKey",
    "kNSPrefPaneHelpMenuInfoPListKey": "NSPrefPaneHelpMenuInfoPListKey",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"NSPreferencePane", b"autoSaveTextFields", {"retval": {"type": "Z"}})
    r(b"NSPreferencePane", b"isSelected", {"retval": {"type": "Z"}})
    r(b"NSPreferencePane", b"replyToShouldUnselect:", {"arguments": {2: {"type": "Z"}}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("NSPreferencePane", b"initWithBundle:")
expressions = {}

# END OF FILE
