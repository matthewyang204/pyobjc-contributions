# This file is generated by objective.metadata
#
# Last update: Fri May 10 14:29:34 2024
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
constants = """$$"""
enums = """$$"""
misc.update({})
misc.update({})
misc.update({})
functions = {
    "SSRandomPointForSizeWithinRect": (
        b"{CGPoint=dd}{CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}",
    ),
    "SSRandomIntBetween": (b"iii",),
    "SSRandomFloatBetween": (b"ddd",),
    "SSCenteredRectInRect": (
        b"{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}",
    ),
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"ScreenSaverView", b"hasConfigureSheet", {"retval": {"type": "Z"}})
    r(
        b"ScreenSaverView",
        b"initWithFrame:isPreview:",
        {"arguments": {3: {"type": "Z"}}},
    )
    r(b"ScreenSaverView", b"isAnimating", {"retval": {"type": "Z"}})
    r(b"ScreenSaverView", b"isPreview", {"retval": {"type": "Z"}})
    r(b"ScreenSaverView", b"performGammaFade", {"retval": {"type": "Z"}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("ScreenSaverView", b"initWithFrame:")
objc.registerNewKeywordsFromSelector("ScreenSaverView", b"initWithFrame:isPreview:")
expressions = {}

# END OF FILE
