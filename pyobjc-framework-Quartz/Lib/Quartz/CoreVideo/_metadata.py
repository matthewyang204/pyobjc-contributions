# This file is generated by objective.metadata
#
# Last update: Sat May 11 10:59:23 2024
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
misc.update(
    {
        "CVTimeStamp": objc.createStructType(
            "Quartz.CoreVideo.CVTimeStamp",
            b"{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
            [
                "version",
                "videoTimeScale",
                "videoTime",
                "hostTime",
                "rateScalar",
                "videoRefreshPeriod",
                "smpteTime",
                "flags",
                "reserved",
            ],
        ),
        "CVPlanarPixelBufferInfo_YCbCrBiPlanar": objc.createStructType(
            "Quartz.CoreVideo.CVPlanarPixelBufferInfo_YCbCrBiPlanar",
            b"{CVPlanarPixelBufferInfo_YCbCrBiPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}",
            ["componentInfoY", "componentInfoCbCr"],
        ),
        "CVPlanarPixelBufferInfo_YCbCrPlanar": objc.createStructType(
            "Quartz.CoreVideo.CVPlanarPixelBufferInfo_YCbCrPlanar",
            b"{CVPlanarPixelBufferInfo_YCbCrPlanar={CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}{CVPlanarComponentInfo=iI}}",
            ["componentInfoY", "componentInfoCb", "componentInfoCr"],
        ),
        "CVPlanarComponentInfo": objc.createStructType(
            "Quartz.CoreVideo.CVPlanarComponentInfo",
            b"{CVPlanarComponentInfo=iI}",
            ["offset", "rowBytes"],
        ),
        "CVTime": objc.createStructType(
            "Quartz.CoreVideo.CVTime",
            b"{CVTime=qii}",
            ["timeValue", "timeScale", "flags"],
        ),
        "CVSMPTETime": objc.createStructType(
            "Quartz.CoreVideo.CVSMPTETime",
            b"{CVSMPTETime=ssIIIssss}",
            [
                "subframes",
                "subframeDivisor",
                "counter",
                "type",
                "flags",
                "hours",
                "minutes",
                "seconds",
                "frames",
            ],
        ),
        "CVPlanarPixelBufferInfo": objc.createStructType(
            "Quartz.CoreVideo.CVPlanarPixelBufferInfo",
            b"{CVPlanarPixelBufferInfo=[1{CVPlanarComponentInfo=iI}]}",
            ["componentInfo"],
        ),
    }
)
constants = """$kCVBufferMovieTimeKey$kCVBufferNonPropagatedAttachmentsKey$kCVBufferPropagatedAttachmentsKey$kCVBufferTimeScaleKey$kCVBufferTimeValueKey$kCVImageBufferAlphaChannelIsOpaque$kCVImageBufferAlphaChannelModeKey$kCVImageBufferAlphaChannelMode_PremultipliedAlpha$kCVImageBufferAlphaChannelMode_StraightAlpha$kCVImageBufferAmbientViewingEnvironmentKey$kCVImageBufferCGColorSpaceKey$kCVImageBufferChromaLocationBottomFieldKey$kCVImageBufferChromaLocationTopFieldKey$kCVImageBufferChromaLocation_Bottom$kCVImageBufferChromaLocation_BottomLeft$kCVImageBufferChromaLocation_Center$kCVImageBufferChromaLocation_DV420$kCVImageBufferChromaLocation_Left$kCVImageBufferChromaLocation_Top$kCVImageBufferChromaLocation_TopLeft$kCVImageBufferChromaSubsamplingKey$kCVImageBufferChromaSubsampling_411$kCVImageBufferChromaSubsampling_420$kCVImageBufferChromaSubsampling_422$kCVImageBufferCleanApertureHeightKey$kCVImageBufferCleanApertureHorizontalOffsetKey$kCVImageBufferCleanApertureKey$kCVImageBufferCleanApertureVerticalOffsetKey$kCVImageBufferCleanApertureWidthKey$kCVImageBufferColorPrimariesKey$kCVImageBufferColorPrimaries_DCI_P3$kCVImageBufferColorPrimaries_EBU_3213$kCVImageBufferColorPrimaries_ITU_R_2020$kCVImageBufferColorPrimaries_ITU_R_709_2$kCVImageBufferColorPrimaries_P22$kCVImageBufferColorPrimaries_P3_D65$kCVImageBufferColorPrimaries_SMPTE_C$kCVImageBufferContentLightLevelInfoKey$kCVImageBufferDisplayDimensionsKey$kCVImageBufferDisplayHeightKey$kCVImageBufferDisplayWidthKey$kCVImageBufferFieldCountKey$kCVImageBufferFieldDetailKey$kCVImageBufferFieldDetailSpatialFirstLineEarly$kCVImageBufferFieldDetailSpatialFirstLineLate$kCVImageBufferFieldDetailTemporalBottomFirst$kCVImageBufferFieldDetailTemporalTopFirst$kCVImageBufferGammaLevelKey$kCVImageBufferICCProfileKey$kCVImageBufferLogTransferFunctionKey$kCVImageBufferLogTransferFunction_AppleLog$kCVImageBufferMasteringDisplayColorVolumeKey$kCVImageBufferPixelAspectRatioHorizontalSpacingKey$kCVImageBufferPixelAspectRatioKey$kCVImageBufferPixelAspectRatioVerticalSpacingKey$kCVImageBufferPreferredCleanApertureKey$kCVImageBufferRegionOfInterestKey$kCVImageBufferTransferFunctionKey$kCVImageBufferTransferFunction_EBU_3213$kCVImageBufferTransferFunction_ITU_R_2020$kCVImageBufferTransferFunction_ITU_R_2100_HLG$kCVImageBufferTransferFunction_ITU_R_709_2$kCVImageBufferTransferFunction_Linear$kCVImageBufferTransferFunction_SMPTE_240M_1995$kCVImageBufferTransferFunction_SMPTE_C$kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ$kCVImageBufferTransferFunction_SMPTE_ST_428_1$kCVImageBufferTransferFunction_UseGamma$kCVImageBufferTransferFunction_sRGB$kCVImageBufferYCbCrMatrixKey$kCVImageBufferYCbCrMatrix_DCI_P3$kCVImageBufferYCbCrMatrix_ITU_R_2020$kCVImageBufferYCbCrMatrix_ITU_R_601_4$kCVImageBufferYCbCrMatrix_ITU_R_709_2$kCVImageBufferYCbCrMatrix_P3_D65$kCVImageBufferYCbCrMatrix_SMPTE_240M_1995$kCVIndefiniteTime@{CVTime=qii}$kCVMetalTextureCacheMaximumTextureAgeKey$kCVMetalTextureStorageMode$kCVMetalTextureUsage$kCVOpenGLBufferHeight$kCVOpenGLBufferInternalFormat$kCVOpenGLBufferMaximumMipmapLevel$kCVOpenGLBufferPoolMaximumBufferAgeKey$kCVOpenGLBufferPoolMinimumBufferCountKey$kCVOpenGLBufferTarget$kCVOpenGLBufferWidth$kCVOpenGLTextureCacheChromaSamplingModeAutomatic$kCVOpenGLTextureCacheChromaSamplingModeBestPerformance$kCVOpenGLTextureCacheChromaSamplingModeHighestQuality$kCVOpenGLTextureCacheChromaSamplingModeKey$kCVPixelBufferBytesPerRowAlignmentKey$kCVPixelBufferCGBitmapContextCompatibilityKey$kCVPixelBufferCGImageCompatibilityKey$kCVPixelBufferExtendedPixelsBottomKey$kCVPixelBufferExtendedPixelsLeftKey$kCVPixelBufferExtendedPixelsRightKey$kCVPixelBufferExtendedPixelsTopKey$kCVPixelBufferHeightKey$kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey$kCVPixelBufferIOSurfaceOpenGLESFBOCompatibilityKey$kCVPixelBufferIOSurfaceOpenGLESTextureCompatibilityKey$kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey$kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey$kCVPixelBufferIOSurfacePropertiesKey$kCVPixelBufferMemoryAllocatorKey$kCVPixelBufferMetalCompatibilityKey$kCVPixelBufferOpenGLCompatibilityKey$kCVPixelBufferOpenGLESCompatibilityKey$kCVPixelBufferOpenGLESTextureCacheCompatibilityKey$kCVPixelBufferOpenGLTextureCacheCompatibilityKey$kCVPixelBufferPixelFormatTypeKey$kCVPixelBufferPlaneAlignmentKey$kCVPixelBufferPoolAllocationThresholdKey$kCVPixelBufferPoolFreeBufferNotification$kCVPixelBufferPoolMaximumBufferAgeKey$kCVPixelBufferPoolMinimumBufferCountKey$kCVPixelBufferProResRAWKey_BlackLevel$kCVPixelBufferProResRAWKey_ColorMatrix$kCVPixelBufferProResRAWKey_GainFactor$kCVPixelBufferProResRAWKey_MetadataExtension$kCVPixelBufferProResRAWKey_RecommendedCrop$kCVPixelBufferProResRAWKey_SenselSitingOffsets$kCVPixelBufferProResRAWKey_WhiteBalanceBlueFactor$kCVPixelBufferProResRAWKey_WhiteBalanceCCT$kCVPixelBufferProResRAWKey_WhiteBalanceRedFactor$kCVPixelBufferProResRAWKey_WhiteLevel$kCVPixelBufferVersatileBayerKey_BayerPattern$kCVPixelBufferWidthKey$kCVPixelFormatBitsPerBlock$kCVPixelFormatBlackBlock$kCVPixelFormatBlockHeight$kCVPixelFormatBlockHorizontalAlignment$kCVPixelFormatBlockVerticalAlignment$kCVPixelFormatBlockWidth$kCVPixelFormatCGBitmapContextCompatibility$kCVPixelFormatCGBitmapInfo$kCVPixelFormatCGImageCompatibility$kCVPixelFormatCodecType$kCVPixelFormatComponentRange$kCVPixelFormatComponentRange_FullRange$kCVPixelFormatComponentRange_VideoRange$kCVPixelFormatComponentRange_WideRange$kCVPixelFormatConstant$kCVPixelFormatContainsAlpha$kCVPixelFormatContainsGrayscale$kCVPixelFormatContainsRGB$kCVPixelFormatContainsSenselArray$kCVPixelFormatContainsYCbCr$kCVPixelFormatFillExtendedPixelsCallback$kCVPixelFormatFourCC$kCVPixelFormatHorizontalSubsampling$kCVPixelFormatName$kCVPixelFormatOpenGLCompatibility$kCVPixelFormatOpenGLESCompatibility$kCVPixelFormatOpenGLFormat$kCVPixelFormatOpenGLInternalFormat$kCVPixelFormatOpenGLType$kCVPixelFormatPlanes$kCVPixelFormatQDCompatibility$kCVPixelFormatVerticalSubsampling$kCVZeroTime@{CVTime=qii}$"""
enums = """$COREVIDEO_INCLUDED_IOSURFACE_HEADER_FILE@1$kCVAttachmentMode_ShouldNotPropagate@0$kCVAttachmentMode_ShouldPropagate@1$kCVPixelBufferLock_ReadOnly@1$kCVPixelBufferPoolFlushExcessBuffers@1$kCVPixelFormatType_128RGBAFloat@1380410945$kCVPixelFormatType_14Bayer_BGGR@1650943796$kCVPixelFormatType_14Bayer_GBRG@1734505012$kCVPixelFormatType_14Bayer_GRBG@1735549492$kCVPixelFormatType_14Bayer_RGGB@1919379252$kCVPixelFormatType_16BE555@16$kCVPixelFormatType_16BE565@1110783541$kCVPixelFormatType_16Gray@1647392359$kCVPixelFormatType_16LE555@1278555445$kCVPixelFormatType_16LE5551@892679473$kCVPixelFormatType_16LE565@1278555701$kCVPixelFormatType_16VersatileBayer@1651519798$kCVPixelFormatType_1IndexedGray_WhiteIsZero@33$kCVPixelFormatType_1Monochrome@1$kCVPixelFormatType_24BGR@842285639$kCVPixelFormatType_24RGB@24$kCVPixelFormatType_2Indexed@2$kCVPixelFormatType_2IndexedGray_WhiteIsZero@34$kCVPixelFormatType_30RGB@1378955371$kCVPixelFormatType_30RGBLEPackedWideGamut@1999843442$kCVPixelFormatType_32ABGR@1094862674$kCVPixelFormatType_32ARGB@32$kCVPixelFormatType_32AlphaGray@1647522401$kCVPixelFormatType_32BGRA@1111970369$kCVPixelFormatType_32RGBA@1380401729$kCVPixelFormatType_40ARGBLEWideGamut@1999908961$kCVPixelFormatType_40ARGBLEWideGamutPremultiplied@1999908973$kCVPixelFormatType_420YpCbCr10BiPlanarFullRange@2019963440$kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange@2016686640$kCVPixelFormatType_420YpCbCr8BiPlanarFullRange@875704422$kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange@875704438$kCVPixelFormatType_420YpCbCr8Planar@2033463856$kCVPixelFormatType_420YpCbCr8PlanarFullRange@1714696752$kCVPixelFormatType_420YpCbCr8VideoRange_8A_TriPlanar@1982882104$kCVPixelFormatType_422YpCbCr10@1983000880$kCVPixelFormatType_422YpCbCr10BiPlanarFullRange@2019963442$kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange@2016686642$kCVPixelFormatType_422YpCbCr16@1983000886$kCVPixelFormatType_422YpCbCr16BiPlanarVideoRange@1937125938$kCVPixelFormatType_422YpCbCr8@846624121$kCVPixelFormatType_422YpCbCr8BiPlanarFullRange@875704934$kCVPixelFormatType_422YpCbCr8BiPlanarVideoRange@875704950$kCVPixelFormatType_422YpCbCr8FullRange@2037741158$kCVPixelFormatType_422YpCbCr8_yuvs@2037741171$kCVPixelFormatType_422YpCbCr_4A_8BiPlanar@1630697081$kCVPixelFormatType_4444AYpCbCr16@2033463606$kCVPixelFormatType_4444AYpCbCr8@2033463352$kCVPixelFormatType_4444AYpCbCrFloat@1916036716$kCVPixelFormatType_4444YpCbCrA8@1983131704$kCVPixelFormatType_4444YpCbCrA8R@1916022840$kCVPixelFormatType_444YpCbCr10@1983131952$kCVPixelFormatType_444YpCbCr10BiPlanarFullRange@2019963956$kCVPixelFormatType_444YpCbCr10BiPlanarVideoRange@2016687156$kCVPixelFormatType_444YpCbCr16BiPlanarVideoRange@1937126452$kCVPixelFormatType_444YpCbCr16VideoRange_16A_TriPlanar@1932812659$kCVPixelFormatType_444YpCbCr8@1983066168$kCVPixelFormatType_444YpCbCr8BiPlanarFullRange@875836518$kCVPixelFormatType_444YpCbCr8BiPlanarVideoRange@875836534$kCVPixelFormatType_48RGB@1647589490$kCVPixelFormatType_4Indexed@4$kCVPixelFormatType_4IndexedGray_WhiteIsZero@36$kCVPixelFormatType_64ARGB@1647719521$kCVPixelFormatType_64RGBAHalf@1380411457$kCVPixelFormatType_64RGBALE@1815491698$kCVPixelFormatType_64RGBA_DownscaledProResRAW@1651521076$kCVPixelFormatType_8Indexed@8$kCVPixelFormatType_8IndexedGray_WhiteIsZero@40$kCVPixelFormatType_ARGB2101010LEPacked@1815162994$kCVPixelFormatType_DepthFloat16@1751410032$kCVPixelFormatType_DepthFloat32@1717855600$kCVPixelFormatType_DisparityFloat16@1751411059$kCVPixelFormatType_DisparityFloat32@1717856627$kCVPixelFormatType_Lossless_32BGRA@641877825$kCVPixelFormatType_Lossless_420YpCbCr10PackedBiPlanarVideoRange@645428784$kCVPixelFormatType_Lossless_420YpCbCr8BiPlanarFullRange@641230384$kCVPixelFormatType_Lossless_420YpCbCr8BiPlanarVideoRange@641234480$kCVPixelFormatType_Lossless_422YpCbCr10PackedBiPlanarVideoRange@645428786$kCVPixelFormatType_Lossy_32BGRA@759318337$kCVPixelFormatType_Lossy_420YpCbCr10PackedBiPlanarVideoRange@762869296$kCVPixelFormatType_Lossy_420YpCbCr8BiPlanarFullRange@758670896$kCVPixelFormatType_Lossy_420YpCbCr8BiPlanarVideoRange@758674992$kCVPixelFormatType_Lossy_422YpCbCr10PackedBiPlanarVideoRange@762869298$kCVPixelFormatType_OneComponent10@1278226736$kCVPixelFormatType_OneComponent12@1278226738$kCVPixelFormatType_OneComponent16@1278226742$kCVPixelFormatType_OneComponent16Half@1278226536$kCVPixelFormatType_OneComponent32Float@1278226534$kCVPixelFormatType_OneComponent8@1278226488$kCVPixelFormatType_TwoComponent16@843264310$kCVPixelFormatType_TwoComponent16Half@843264104$kCVPixelFormatType_TwoComponent32Float@843264102$kCVPixelFormatType_TwoComponent8@843264056$kCVReturnAllocationFailed@-6662$kCVReturnDisplayLinkAlreadyRunning@-6671$kCVReturnDisplayLinkCallbacksNotSet@-6673$kCVReturnDisplayLinkNotRunning@-6672$kCVReturnError@-6660$kCVReturnFirst@-6660$kCVReturnInvalidArgument@-6661$kCVReturnInvalidDisplay@-6670$kCVReturnInvalidPixelBufferAttributes@-6682$kCVReturnInvalidPixelFormat@-6680$kCVReturnInvalidPoolAttributes@-6691$kCVReturnInvalidSize@-6681$kCVReturnLast@-6699$kCVReturnPixelBufferNotMetalCompatible@-6684$kCVReturnPixelBufferNotOpenGLCompatible@-6683$kCVReturnPoolAllocationFailed@-6690$kCVReturnRetry@-6692$kCVReturnSuccess@0$kCVReturnUnsupported@-6663$kCVReturnWouldExceedAllocationThreshold@-6689$kCVSMPTETimeRunning@2$kCVSMPTETimeType24@0$kCVSMPTETimeType25@1$kCVSMPTETimeType2997@4$kCVSMPTETimeType2997Drop@5$kCVSMPTETimeType30@3$kCVSMPTETimeType30Drop@2$kCVSMPTETimeType5994@7$kCVSMPTETimeType60@6$kCVSMPTETimeValid@1$kCVTimeIsIndefinite@1$kCVTimeStampBottomField@131072$kCVTimeStampHostTimeValid@2$kCVTimeStampIsInterlaced@196608$kCVTimeStampRateScalarValid@16$kCVTimeStampSMPTETimeValid@4$kCVTimeStampTopField@65536$kCVTimeStampVideoHostTimeValid@3$kCVTimeStampVideoRefreshPeriodValid@8$kCVTimeStampVideoTimeValid@1$kCVVersatileBayer_BayerPattern_BGGR@3$kCVVersatileBayer_BayerPattern_GBRG@2$kCVVersatileBayer_BayerPattern_GRBG@1$kCVVersatileBayer_BayerPattern_RGGB@0$kReturnRetry@-6692$"""
misc.update(
    {
        "CVPixelBufferPoolFlushFlags": NewType("CVPixelBufferPoolFlushFlags", int),
        "CVTimeStampFlags": NewType("CVTimeStampFlags", int),
        "CVSMPTETimeType": NewType("CVSMPTETimeType", int),
        "CVPixelBufferLockFlags": NewType("CVPixelBufferLockFlags", int),
        "CVSMPTETimeFlags": NewType("CVSMPTETimeFlags", int),
        "CVTimeFlags": NewType("CVTimeFlags", int),
        "CVAttachmentMode": NewType("CVAttachmentMode", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "CVImageBufferGetEncodedSize": (b"{CGSize=dd}^{__CVBuffer=}",),
    "CVOpenGLTextureRelease": (b"v^{__CVBuffer=}",),
    "CVPixelBufferPoolRelease": (b"v^{__CVPixelBufferPool=}",),
    "CVPixelBufferPoolGetTypeID": (b"Q",),
    "CVYCbCrMatrixGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVPixelBufferCreate": (
        b"i^{__CFAllocator=}QQI^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {5: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVOpenGLBufferPoolGetTypeID": (b"Q",),
    "CVPixelBufferFillExtendedPixels": (b"i^{__CVBuffer=}",),
    "CVOpenGLTextureCacheRetain": (
        b"^{__CVOpenGLTextureCache=}^{__CVOpenGLTextureCache=}",
    ),
    "CVOpenGLBufferPoolCreateOpenGLBuffer": (
        b"i^{__CFAllocator=}^{__CVOpenGLBufferPool=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetCurrentCGDisplay": (b"i^{__CVDisplayLink=}I",),
    "CVBufferSetAttachment": (b"v^{__CVBuffer=}^{__CFString=}@I",),
    "CVGetCurrentHostTime": (b"Q", "", {"variadic": False}),
    "CVPixelBufferPoolCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVPixelBufferPool=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferGetHeightOfPlane": (b"Q^{__CVBuffer=}Q",),
    "CVBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVBufferHasAttachment": (b"Z^{__CVBuffer=}^{__CFString=}",),
    "CVDisplayLinkTranslateTime": (
        b"i^{__CVDisplayLink=}^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
        "",
        {"arguments": {1: {"type_modifier": "n"}, 2: {"type_modifier": "o"}}},
    ),
    "CVPixelBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVPixelBufferGetPlaneCount": (b"Q^{__CVBuffer=}",),
    "CVOpenGLTextureCacheRelease": (b"v^{__CVOpenGLTextureCache=}",),
    "CVPixelBufferGetBaseAddress": (
        b"^v^{__CVBuffer=}",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "CVOpenGLBufferPoolRelease": (b"v^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferLockBaseAddress": (b"i^{__CVBuffer=}Q",),
    "CVMetalTextureCacheCreateFromImage": (
        b"i@@@@QQQ^@",
        "",
        {"arguments": {7: {"already_cfretained": True, "type_modifier": "o"}}},
    ),
    "CVOpenGLTextureCacheGetTypeID": (b"Q",),
    "CVMetalTextureCacheCreateTextureFromImage": (
        b"i^{__CFAllocator=}^{__CVMetalTextureCache=}^{__CVBuffer=}^{__CFDictionary=}QQQQ^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {8: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVOpenGLTextureIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVMetalTextureCacheFlush": (b"v^{__CVMetalTextureCache=}Q",),
    "CVPixelBufferPoolCreatePixelBuffer": (
        b"i^{__CFAllocator=}^{__CVPixelBufferPool=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferGetTypeID": (b"Q",),
    "CVDisplayLinkGetActualOutputVideoRefreshPeriod": (b"d^{__CVDisplayLink=}",),
    "CVPixelBufferGetWidth": (b"Q^{__CVBuffer=}",),
    "CVMetalTextureCacheGetTypeID": (b"Q",),
    "CVDisplayLinkCreateWithCGDisplay": (
        b"iI^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVBufferRelease": (b"v^{__CVBuffer=}",),
    "CVBufferCopyAttachments": (
        b"^{__CFDictionary=}^{__CVBuffer=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVDisplayLinkGetCurrentTime": (
        b"i^{__CVDisplayLink=}^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes": (
        b"^{__CFArray=}^{__CFAllocator=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferPoolGetAttributes": (b"^{__CFDictionary=}^{__CVPixelBufferPool=}",),
    "CVBufferGetAttachments": (b"^{__CFDictionary=}^{__CVBuffer=}I",),
    "CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType": (
        b"v^{__CFDictionary=}I",
    ),
    "CVOpenGLBufferPoolCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{__CFDictionary=}^^{__CVOpenGLBufferPool=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkRetain": (b"^{__CVDisplayLink=}^{__CVDisplayLink=}",),
    "CVPixelBufferCreateWithIOSurface": (
        b"i^{__CFAllocator=}^{__IOSurface=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkCreateWithOpenGLDisplayMask": (
        b"iI^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetOutputHandler": (
        b"i^{__CVDisplayLink=}@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "^{__CVDisplayLink=}"},
                            2: {
                                "type": "^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            3: {
                                "type": "^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            4: {"type": "Q"},
                            5: {"type": "o^Q"},
                        },
                    }
                }
            }
        },
    ),
    "CVYCbCrMatrixGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVOpenGLBufferCreate": (
        b"i^{__CFAllocator=}QQ^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferPoolCreatePixelBufferWithAuxAttributes": (
        b"i^{__CFAllocator=}^{__CVPixelBufferPool=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {3: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVOpenGLTextureCacheFlush": (b"v^{__CVOpenGLTextureCache=}Q",),
    "CVDisplayLinkCreateWithActiveCGDisplays": (
        b"i^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {0: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkGetNominalOutputVideoRefreshPeriod": (
        b"{CVTime=qii}^{__CVDisplayLink=}",
    ),
    "CVPixelBufferCreateResolvedAttributesDictionary": (
        b"i^{__CFAllocator=}^{__CFArray=}^^{__CFDictionary=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkSetOutputCallback": (
        b"i^{__CVDisplayLink=}^?^v",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"i"},
                        "arguments": {
                            0: {"type": b"^{__CVDisplayLink=}"},
                            1: {
                                "type": b"^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "n",
                            },
                            2: {
                                "type": b"^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}",
                                "type_modifier": "N",
                            },
                            3: {"type": b"Q"},
                            4: {"type": b"^Q", "type_modifier": "o"},
                            5: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "CVOpenGLTextureGetName": (b"I^{__CVBuffer=}",),
    "CVOpenGLBufferRelease": (b"v^{__CVBuffer=}",),
    "CVOpenGLTextureRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVOpenGLBufferPoolGetAttributes": (b"^{__CFDictionary=}^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferGetWidthOfPlane": (b"Q^{__CVBuffer=}Q",),
    "CVBufferPropagateAttachments": (b"v^{__CVBuffer=}^{__CVBuffer=}",),
    "CVPixelBufferPoolRetain": (b"^{__CVPixelBufferPool=}^{__CVPixelBufferPool=}",),
    "CVPixelBufferGetHeight": (b"Q^{__CVBuffer=}",),
    "CVColorPrimariesGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVOpenGLBufferGetTypeID": (b"Q",),
    "CVDisplayLinkRelease": (b"v^{__CVDisplayLink=}",),
    "CVBufferGetAttachment": (
        b"@^{__CVBuffer=}^{__CFString=}^I",
        "",
        {"arguments": {2: {"type_modifier": "o"}}},
    ),
    "CVDisplayLinkStop": (b"i^{__CVDisplayLink=}",),
    "CVPixelFormatDescriptionCreateWithPixelFormatType": (
        b"^{__CFDictionary=}^{__CFAllocator=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVMetalTextureGetCleanTexCoords": (
        b"v^{__CVBuffer=}^f^f^f^f",
        "",
        {
            "arguments": {
                1: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                2: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                3: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
                4: {"c_array_of_fixed_length": 2, "type_modifier": "o"},
            }
        },
    ),
    "CVPixelBufferGetIOSurface": (b"^{__IOSurface=}^{__CVBuffer=}",),
    "CVOpenGLTextureCacheCreateTextureFromImage": (
        b"i^{__CFAllocator=}^{__CVOpenGLTextureCache=}^{__CVBuffer=}^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVDisplayLinkCreateWithCGDisplays": (
        b"i^Iq^^{__CVDisplayLink=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                0: {"c_array_length_in_arg": 1, "type_modifier": "n"},
                2: {"already_cfretained": True, "type_modifier": "o"},
            },
        },
    ),
    "CVPixelBufferPoolGetPixelBufferAttributes": (
        b"^{__CFDictionary=}^{__CVPixelBufferPool=}",
    ),
    "CVOpenGLTextureGetTypeID": (b"Q",),
    "CVIsCompressedPixelFormatAvailable": (b"ZI",),
    "CVImageBufferIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVBufferCopyAttachment": (
        b"@^{__CVBuffer=}^{__CFString=}^I",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"type_modifier": "o"}},
        },
    ),
    "CVMetalTextureGetTexture": (b"@^{__CVBuffer=}",),
    "CVPixelBufferIsPlanar": (b"Z^{__CVBuffer=}",),
    "CVBufferRemoveAllAttachments": (b"v^{__CVBuffer=}",),
    "CVTransferFunctionGetIntegerCodePointForString": (b"i^{__CFString=}",),
    "CVPixelBufferCreateWithBytes": (
        b"i^{__CFAllocator=}QQI^vQ^?^v^{__CFDictionary=}^^{__CVBuffer=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                6: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"^v"}},
                    }
                }
            },
        },
    ),
    "CVMetalTextureGetTypeID": (b"Q",),
    "CVOpenGLBufferPoolRetain": (b"^{__CVOpenGLBufferPool=}^{__CVOpenGLBufferPool=}",),
    "CVPixelBufferUnlockBaseAddress": (b"i^{__CVBuffer=}Q",),
    "CVImageBufferGetCleanRect": (b"{CGRect={CGPoint=dd}{CGSize=dd}}^{__CVBuffer=}",),
    "CVImageBufferCreateColorSpaceFromAttachments": (
        b"^{CGColorSpace=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVPixelBufferGetBytesPerRowOfPlane": (b"Q^{__CVBuffer=}Q",),
    "CVColorPrimariesGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVDisplayLinkStart": (b"i^{__CVDisplayLink=}",),
    "CVDisplayLinkGetTypeID": (b"Q",),
    "CVImageBufferGetDisplaySize": (b"{CGSize=dd}^{__CVBuffer=}",),
    "CVPixelBufferGetDataSize": (b"Q^{__CVBuffer=}",),
    "CVOpenGLBufferPoolGetOpenGLBufferAttributes": (
        b"^{__CFDictionary=}^{__CVOpenGLBufferPool=}",
    ),
    "CVOpenGLBufferAttach": (b"i^{__CVBuffer=}^{_CGLContextObject=}Iii",),
    "CVPixelBufferGetBaseAddressOfPlane": (
        b"^v^{__CVBuffer=}Q",
        "",
        {"retval": {"c_array_of_variable_length": True}},
    ),
    "CVDisplayLinkIsRunning": (b"Z^{__CVDisplayLink=}",),
    "CVPixelBufferGetPixelFormatType": (b"I^{__CVBuffer=}",),
    "CVBufferRemoveAttachment": (b"v^{__CVBuffer=}^{__CFString=}",),
    "CVPixelBufferCopyCreationAttributes": (
        b"^{__CFDictionary=}^{__CVBuffer=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CVOpenGLBufferGetAttributes": (b"^{__CFDictionary=}^{__CVBuffer=}",),
    "CVDisplayLinkGetOutputVideoLatency": (b"{CVTime=qii}^{__CVDisplayLink=}",),
    "CVPixelBufferGetBytesPerRow": (b"Q^{__CVBuffer=}",),
    "CVMetalTextureCacheCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}@^{__CFDictionary=}^^{__CVMetalTextureCache=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {4: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferGetExtendedPixels": (
        b"v^{__CVBuffer=}^Q^Q^Q^Q",
        "",
        {
            "arguments": {
                1: {"type_modifier": "o"},
                2: {"type_modifier": "o"},
                3: {"type_modifier": "o"},
                4: {"type_modifier": "o"},
            }
        },
    ),
    "CVTransferFunctionGetStringForIntegerCodePoint": (b"^{__CFString=}i",),
    "CVImageBufferGetColorSpace": (b"^{CGColorSpace=}^{__CVBuffer=}",),
    "CVDisplayLinkGetCurrentCGDisplay": (b"I^{__CVDisplayLink=}",),
    "CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext": (
        b"i^{__CVDisplayLink=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}",
    ),
    "CVPixelBufferRelease": (b"v^{__CVBuffer=}",),
    "CVBufferSetAttachments": (b"v^{__CVBuffer=}^{__CFDictionary=}I",),
    "CVOpenGLTextureGetTarget": (b"I^{__CVBuffer=}",),
    "CVGetHostClockFrequency": (b"d", "", {"variadic": False}),
    "CVGetHostClockMinimumTimeDelta": (b"I", "", {"variadic": False}),
    "CVOpenGLBufferRetain": (b"^{__CVBuffer=}^{__CVBuffer=}",),
    "CVMetalTextureIsFlipped": (b"Z^{__CVBuffer=}",),
    "CVOpenGLTextureCacheCreate": (
        b"i^{__CFAllocator=}^{__CFDictionary=}^{_CGLContextObject=}^{_CGLPixelFormatObject=}^{__CFDictionary=}^^{__CVOpenGLTextureCache=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {5: {"already_cfretained": True, "type_modifier": "o"}},
        },
    ),
    "CVPixelBufferPoolFlush": (b"v^{__CVPixelBufferPool=}Q",),
    "CVOpenGLTextureGetCleanTexCoords": (
        b"v^{__CVBuffer=}^f^f^f^f",
        "",
        {
            "arguments": {
                1: {"c_array_of_fixed_length": 2, "type_modifier": "n"},
                2: {"c_array_of_fixed_length": 2, "type_modifier": "n"},
                3: {"c_array_of_fixed_length": 2, "type_modifier": "n"},
                4: {"c_array_of_fixed_length": 2, "type_modifier": "n"},
            }
        },
    ),
}
aliases = {
    "CVDIRECT3DSURFACE": "LPDIRECT3DSURFACE9",
    "COREVIDEO_SUPPORTS_OPENGLES": "COREVIDEO_FALSE",
    "CV_NONNULL": "__nonnull",
    "COREVIDEO_SUPPORTS_PERMANENT_ALLOCATOR": "COREVIDEO_FALSE",
    "CVImageBufferRef": "CVBufferRef",
    "COREVIDEO_SUPPORTS_PREFETCH": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_OPENGL": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_IOSURFACE": "COREVIDEO_TRUE",
    "COREVIDEO_USE_DERIVED_ENUMS_FOR_CONSTANTS": "COREVIDEO_TRUE",
    "CV_INLINE": "CF_INLINE",
    "kCVReturnError": "kCVReturnFirst",
    "COREVIDEO_SUPPORTS_DIRECT3D": "COREVIDEO_FALSE",
    "CVDIRECT3DTEXTURE": "LPDIRECT3DTEXTURE9",
    "COREVIDEO_DECLARE_NULLABILITY": "COREVIDEO_TRUE",
    "CV_RELEASES_ARGUMENT": "CF_RELEASES_ARGUMENT",
    "COREVIDEO_SUPPORTS_DISPLAYLINK": "COREVIDEO_TRUE",
    "CV_RETURNS_RETAINED": "CF_RETURNS_RETAINED",
    "CV_NULLABLE": "__nullable",
    "COREVIDEO_USE_IOSURFACEREF": "COREVIDEO_FALSE",
    "CVDIRECT3DDEVICE": "LPDIRECT3DDEVICE9",
    "COREVIDEO_SUPPORTS_METAL": "COREVIDEO_TRUE",
    "COREVIDEO_SUPPORTS_GLES_TEX_IMAGE_IOSURFACE": "COREVIDEO_SUPPORTS_IOSURFACE",
    "CVDIRECT3D": "LPDIRECT3D9",
    "COREVIDEO_SUPPORTS_COLORSPACE": "COREVIDEO_TRUE",
    "CV_RETURNS_RETAINED_PARAMETER": "CF_RETURNS_RETAINED",
}
cftypes = [
    ("CVBufferRef", b"^{__CVBuffer=}", "CVBufferGetTypeID", None),
    ("CVDisplayLinkRef", b"^{__CVDisplayLink=}", "CVDisplayLinkGetTypeID", None),
    ("CVMetalTextureCacheRef", b"^{__CVMetalTextureCache=}", None, None),
    (
        "CVOpenGLBufferPoolRef",
        b"^{__CVOpenGLBufferPool=}",
        "CVOpenGLBufferPoolGetTypeID",
        None,
    ),
    (
        "CVOpenGLTextureCacheRef",
        b"^{__CVOpenGLTextureCache=}",
        "CVOpenGLTextureCacheGetTypeID",
        None,
    ),
    (
        "CVPixelBufferPoolRef",
        b"^{__CVPixelBufferPool=}",
        "CVPixelBufferPoolGetTypeID",
        None,
    ),
    ("CVOpenGLBufferRef", b"^{__CVOpenGLBuffer=}", "CVOpenGLBufferGetTypeID", None),
    ("CVPixelBufferRef", b"^{__CVPixelBuffer=}", "CVPixelBufferGetTypeID", None),
    ("CVOpenGLTextureRef", b"^{__CVOpenGLTexture=}", "CVOpenGLTextureGetTypeID", None),
]
expressions = {}

# END OF FILE
