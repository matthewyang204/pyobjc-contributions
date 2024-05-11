# This file is generated by objective.metadata
#
# Last update: Sat May 11 11:02:02 2024
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
constants = """$AXAnimatedImagesEnabledDidChangeNotification$AXMFiHearingDevicePairedUUIDsDidChangeNotification$AXMFiHearingDeviceStreamingEarDidChangeNotification$AXPrefersHorizontalTextLayoutDidChangeNotification$"""
enums = """$AXChartContentDirectionBottomToTop@3$AXChartContentDirectionLeftToRight@0$AXChartContentDirectionRadialClockwise@4$AXChartContentDirectionRadialCounterClockwise@5$AXChartContentDirectionRightToLeft@1$AXChartContentDirectionTopToBottom@2$AXCustomContentImportanceDefault@0$AXCustomContentImportanceHigh@1$AXHearingDeviceEarBoth@6$AXHearingDeviceEarLeft@2$AXHearingDeviceEarNone@0$AXHearingDeviceEarRight@4$AXScaleTypeLinear@0$AXScaleTypeLn@2$AXScaleTypeLog10@1$"""
misc.update(
    {
        "AXChartDescriptorContentDirection": NewType(
            "AXChartDescriptorContentDirection", int
        ),
        "AXHearingDeviceEar": NewType("AXHearingDeviceEar", int),
        "AXNumericDataAxisDescriptorScale": NewType(
            "AXNumericDataAxisDescriptorScale", int
        ),
        "AXCustomContentImportance": NewType("AXCustomContentImportance", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "AXMFiHearingDeviceStreamingEar": (b"Q",),
    "AXSupportsBidirectionalAXMFiHearingDeviceStreaming": (b"Z",),
    "AXAnimatedImagesEnabled": (b"Z",),
    "AXNameFromColor": (b"@^{CGColor=}",),
    "AXMFiHearingDevicePairedUUIDs": (b"@",),
    "AXPrefersHorizontalTextLayout": (b"Z",),
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AXDataSeriesDescriptor",
        b"initWithAttributedName:isContinuous:dataPoints:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"AXDataSeriesDescriptor",
        b"initWithName:isContinuous:dataPoints:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"AXDataSeriesDescriptor", b"isContinuous", {"retval": {"type": b"Z"}})
    r(
        b"AXDataSeriesDescriptor",
        b"setIsContinuous:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"AXNumericDataAxisDescriptor",
        b"initWithAttributedTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"d"}},
                    }
                }
            }
        },
    )
    r(
        b"AXNumericDataAxisDescriptor",
        b"initWithTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:",
        {
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"d"}},
                    }
                }
            }
        },
    )
    r(
        b"AXNumericDataAxisDescriptor",
        b"setValueDescriptionProvider:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"d"}},
                    }
                }
            }
        },
    )
    r(
        b"NSObject",
        b"accessibilityBrailleMapRenderRegion",
        {"required": False, "retval": {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"}},
    )
    r(
        b"NSObject",
        b"accessibilityBrailleMapRenderer",
        {"required": False, "retval": {"type": b"@?"}},
    )
    r(
        b"NSObject",
        b"accessibilityChartDescriptor",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"accessibilityCustomContent",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"accessibilityCustomContentBlock",
        {
            "required": False,
            "retval": {
                "callable": {
                    "retval": {"type": b"@"},
                    "arguments": {0: {"type": b"^v"}},
                },
                "type": b"@?",
            },
        },
    )
    r(b"NSObject", b"attributedTitle", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"setAccessibilityBrailleMapRenderRegion:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"}},
        },
    )
    r(
        b"NSObject",
        b"setAccessibilityBrailleMapRenderer:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                }
            },
        },
    )
    r(
        b"NSObject",
        b"setAccessibilityChartDescriptor:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setAccessibilityCustomContent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setAccessibilityCustomContentBlock",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"NSObject",
        b"setAccessibilityCustomContentBlock:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": b"@?",
                }
            },
        },
    )
    r(
        b"NSObject",
        b"setAttributedTitle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setTitle:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"title", {"required": True, "retval": {"type": b"@"}})
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "AXCategoricalDataAxisDescriptor", b"initWithAttributedTitle:categoryOrder:"
)
objc.registerNewKeywordsFromSelector(
    "AXCategoricalDataAxisDescriptor", b"initWithTitle:categoryOrder:"
)
objc.registerNewKeywordsFromSelector(
    "AXChartDescriptor",
    b"initWithAttributedTitle:summary:xAxisDescriptor:yAxisDescriptor:additionalAxes:series:",
)
objc.registerNewKeywordsFromSelector(
    "AXChartDescriptor",
    b"initWithAttributedTitle:summary:xAxisDescriptor:yAxisDescriptor:series:",
)
objc.registerNewKeywordsFromSelector(
    "AXChartDescriptor",
    b"initWithTitle:summary:xAxisDescriptor:yAxisDescriptor:additionalAxes:series:",
)
objc.registerNewKeywordsFromSelector(
    "AXChartDescriptor",
    b"initWithTitle:summary:xAxisDescriptor:yAxisDescriptor:series:",
)
objc.registerNewKeywordsFromSelector("AXDataPoint", b"initWithX:y:")
objc.registerNewKeywordsFromSelector("AXDataPoint", b"initWithX:y:additionalValues:")
objc.registerNewKeywordsFromSelector(
    "AXDataPoint", b"initWithX:y:additionalValues:label:"
)
objc.registerNewKeywordsFromSelector(
    "AXDataSeriesDescriptor", b"initWithAttributedName:isContinuous:dataPoints:"
)
objc.registerNewKeywordsFromSelector(
    "AXDataSeriesDescriptor", b"initWithName:isContinuous:dataPoints:"
)
objc.registerNewKeywordsFromSelector(
    "AXNumericDataAxisDescriptor",
    b"initWithAttributedTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:",
)
objc.registerNewKeywordsFromSelector(
    "AXNumericDataAxisDescriptor",
    b"initWithTitle:lowerBound:upperBound:gridlinePositions:valueDescriptionProvider:",
)
expressions = {}

# END OF FILE
