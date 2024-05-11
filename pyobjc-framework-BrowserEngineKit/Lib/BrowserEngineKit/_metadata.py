# This file is generated by objective.metadata
#
# Last update: Sat May 11 11:04:38 2024
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
enums = """$BEGestureTypeDoubleTap@3$BEGestureTypeDoubleTapAndHold@2$BEGestureTypeForceTouch@15$BEGestureTypeIMPhraseBoundaryDrag@14$BEGestureTypeLoupe@0$BEGestureTypeOneFingerDoubleTap@8$BEGestureTypeOneFingerTap@1$BEGestureTypeOneFingerTripleTap@9$BEGestureTypeTwoFingerRangedSelectGesture@11$BEGestureTypeTwoFingerSingleTap@10$BEPhraseBoundaryChanged@4$BESelectionFlagsNone@0$BESelectionFlipped@2$BESelectionTouchPhaseEnded@2$BESelectionTouchPhaseEndedMovingBackward@4$BESelectionTouchPhaseEndedMovingForward@3$BESelectionTouchPhaseEndedNotMoving@5$BESelectionTouchPhaseMoved@1$BESelectionTouchPhaseStarted@0$BEWordIsNearTap@1$"""
misc.update(
    {
        "BESelectionFlags": NewType("BESelectionFlags", int),
        "BESelectionTouchPhase": NewType("BESelectionTouchPhase", int),
        "BEGestureType": NewType("BEGestureType", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"BELayerHierarchy",
        b"layerHierarchyWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BELayerHierarchyHostingTransactionCoordinator",
        b"coordinatorWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BEMediaEnvironment",
        b"activateWithError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BEMediaEnvironment",
        b"makeCaptureSessionWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BEMediaEnvironment",
        b"suspendWithError:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BENetworkingProcess",
        b"grantCapability:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BENetworkingProcess",
        b"makeLibXPCConnectionError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BENetworkingProcess",
        b"networkProcessWithInterruptionHandler:completion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"BEProcessCapability",
        b"requestWithError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BERenderingProcess",
        b"grantCapability:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BERenderingProcess",
        b"makeLibXPCConnectionError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BERenderingProcess",
        b"renderingProcessWithInterruptionHandler:completion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"BEWebContentProcess",
        b"grantCapability:error:",
        {"arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"BEWebContentProcess",
        b"makeLibXPCConnectionError:",
        {"arguments": {2: {"type_modifier": b"o"}}},
    )
    r(
        b"BEWebContentProcess",
        b"webContentProcessWithInterruptionHandler:completion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(b"NSObject", b"invalidate", {"required": True, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"invalidateTextEntryContextForTextInput:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"isValid", {"required": True, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"selectionDidChangeForTextInput:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"selectionWillChangeForTextInput:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"shouldDeferEventHandlingToSystemForTextInput:context:",
        {
            "required": True,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"systemDidChangeSelectionForInteraction:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"systemWillChangeSelectionForInteraction:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"textInput:deferReplaceTextActionToSystem:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"textInput:setCandidateSuggestions:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("BEMediaEnvironment", b"initWithWebPageURL:")
objc.registerNewKeywordsFromSelector("BETextSuggestion", b"initWithInputText:")
objc.registerNewKeywordsFromSelector(
    "BEWebAppManifest", b"initWithJSONData:manifestURL:"
)
expressions = {}

# END OF FILE
