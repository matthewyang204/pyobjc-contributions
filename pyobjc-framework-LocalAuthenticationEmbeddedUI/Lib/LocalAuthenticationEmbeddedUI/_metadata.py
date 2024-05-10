# This file is generated by objective.metadata
#
# Last update: Fri May 10 13:05:42 2024
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
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"LARight",
        b"authorizeWithLocalizedReason:inPresentationContext:completion:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("LAAuthenticationView", b"initWithCoder:")
objc.registerNewKeywordsFromSelector("LAAuthenticationView", b"initWithContext:")
objc.registerNewKeywordsFromSelector(
    "LAAuthenticationView", b"initWithContext:controlSize:"
)
objc.registerNewKeywordsFromSelector("LAAuthenticationView", b"initWithFrame:")
expressions = {}

# END OF FILE
