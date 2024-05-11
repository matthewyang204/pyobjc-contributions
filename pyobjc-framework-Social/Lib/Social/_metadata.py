# This file is generated by objective.metadata
#
# Last update: Sat May 11 11:06:12 2024
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
constants = """$SLServiceTypeFacebook$SLServiceTypeLinkedIn$SLServiceTypeSinaWeibo$SLServiceTypeTencentWeibo$SLServiceTypeTwitter$"""
enums = """$SLRequestMethodDELETE@2$SLRequestMethodGET@0$SLRequestMethodPOST@1$SLRequestMethodPUT@3$"""
misc.update({"SLRequestMethod": NewType("SLRequestMethod", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"SLComposeServiceViewController", b"isContentValid", {"retval": {"type": b"Z"}})
    r(
        b"SLRequest",
        b"performRequestWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
