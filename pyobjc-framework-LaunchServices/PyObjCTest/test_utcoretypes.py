
from PyObjCTools.TestSupport import *

import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices

class TestUTCoreTypes (TestCase):
    def testConstants(self):
        self.assertIsInstance(LaunchServices.kUTTypeItem, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeContent, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCompositeContent, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeApplication, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMessage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeContact, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeArchive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeDiskImage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeData, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeDirectory, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeResolvable, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeSymLink, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMountPoint, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAliasFile, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAliasRecord, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeURL, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeFileURL, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePlainText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeUTF8PlainText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeUTF16ExternalPlainText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeUTF16PlainText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeRTF, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeHTML, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeXML, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeSourceCode, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeObjectiveCSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCPlusPlusSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeObjectiveCPlusPlusSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCHeader, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCPlusPlusHeader, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJavaSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePDF, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeRTFD, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeFlatRTFD, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeTXNTextAndMultimediaData, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeWebArchive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeImage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJPEG, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJPEG2000, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeTIFF, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePICT, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeGIF, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePNG, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeQuickTimeImage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAppleICNS, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeBMP, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeICO, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAudiovisualContent, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMovie, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeVideo, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAudio, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeQuickTimeMovie, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMPEG, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMPEG4, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMP3, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMPEG4Audio, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAppleProtectedMPEG4Audio, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeFolder, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeVolume, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePackage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeBundle, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeFramework, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeApplicationBundle, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeApplicationFile, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeVCard, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeInkText, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(LaunchServices.kUTTypeURLBookmarkData, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeDelimitedText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCommaSeparatedText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeTabSeparatedText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeUTF8TabSeparatedText, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAssemblyLanguageSource, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAppleScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeOSAScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeOSAScriptBundle, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJavaScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeShellScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePerlScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePythonScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeRubyScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePHPScript, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJSON, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePropertyList, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeXMLPropertyList, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeBinaryPropertyList, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeRawImage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeScalableVectorGraphics, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMPEG2Video, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMPEG2TransportStream, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAppleProtectedMPEG4Video, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAVIMovie, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeAudioInterchangeFileFormat, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeWaveformAudio, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeMIDIAudio, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePlaylist, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeM3UPlaylist, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePluginBundle, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeSpotlightImporter, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeQuickLookGenerator, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeXPCService, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeUnixExecutable, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeWindowsExecutable, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJavaClass, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeJavaArchive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeSystemPreferencesPane, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeGNUZipArchive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeBzip2Archive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeZipArchive, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeSpreadsheet, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePresentation, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeToDoItem, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeCalendarEvent, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeEmailMessage, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeInternetLocation, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeFont, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeBookmark, unicode)
        self.assertIsInstance(LaunchServices.kUTType3DContent, unicode)
        self.assertIsInstance(LaunchServices.kUTTypePKCS12, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeX509Certificate, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeElectronicPublication, unicode)
        self.assertIsInstance(LaunchServices.kUTTypeLog, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(LaunchServices.kUTTypeSwiftSource, unicode)

if __name__ == "__main__":
    main()
