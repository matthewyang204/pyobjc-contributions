# This file is generated by objective.metadata
#
# Last update: Sat May 11 10:54:50 2024
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
constants = """$SAErrorDomain$"""
enums = """$SAAuthorizationStatusAuthorized@2$SAAuthorizationStatusDenied@1$SAAuthorizationStatusNotDetermined@0$SACrashDetectionEventResponseAttempted@0$SACrashDetectionEventResponseDisabled@1$SAEmergencyResponseManagerVoiceCallStatusActive@1$SAEmergencyResponseManagerVoiceCallStatusDialing@0$SAEmergencyResponseManagerVoiceCallStatusDisconnected@2$SAEmergencyResponseManagerVoiceCallStatusFailed@3$SAErrorInvalidArgument@3$SAErrorNotAllowed@2$SAErrorNotAuthorized@1$SAErrorOperationFailed@4$"""
misc.update(
    {
        "SAEmergencyResponseManagerVoiceCallStatus": NewType(
            "SAEmergencyResponseManagerVoiceCallStatus", int
        ),
        "SAErrorCode": NewType("SAErrorCode", int),
        "SAAuthorizationStatus": NewType("SAAuthorizationStatus", int),
        "SACrashDetectionEventResponse": NewType("SACrashDetectionEventResponse", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"crashDetectionManager:didDetectEvent:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"emergencyResponseManager:didUpdateVoiceCallStatus:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}},
        },
    )
    r(b"SACrashDetectionManager", b"isAvailable", {"retval": {"type": b"Z"}})
    r(
        b"SACrashDetectionManager",
        b"requestAuthorizationWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"q"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SAEmergencyResponseManager",
        b"dialVoiceCallToPhoneNumber:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
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
