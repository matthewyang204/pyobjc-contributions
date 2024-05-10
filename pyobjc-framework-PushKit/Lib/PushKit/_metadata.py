# This file is generated by objective.metadata
#
# Last update: Fri May 10 14:23:09 2024
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
constants = """$PKPushTypeComplication$PKPushTypeFileProvider$PKPushTypeVoIP$"""
enums = """$$"""
misc.update({})
misc.update({"PKPushType": NewType("PKPushType", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"pushRegistry:didInvalidatePushTokenForType:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"pushRegistry:didReceiveIncomingPushWithPayload:forType:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"pushRegistry:didReceiveIncomingPushWithPayload:forType:withCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"pushRegistry:didUpdatePushCredentials:forType:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("PKPushRegistry", b"initWithQueue:")
expressions = {}

# END OF FILE
