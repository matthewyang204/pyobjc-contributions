from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRContentProperties (TestCase):

    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRISOLevel, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeSet, unicode)
        self.assertIsInstance(DiscRecording.kDRPublisher, unicode)
        self.assertIsInstance(DiscRecording.kDRDataPreparer, unicode)
        self.assertIsInstance(DiscRecording.kDRSystemIdentifier, unicode)
        self.assertIsInstance(DiscRecording.kDRApplicationIdentifier, unicode)
        self.assertIsInstance(DiscRecording.kDRCopyrightFile, unicode)
        self.assertIsInstance(DiscRecording.kDRAbstractFile, unicode)
        self.assertIsInstance(DiscRecording.kDRBibliographicFile, unicode)
        self.assertIsInstance(DiscRecording.kDRBlockSize, unicode)
        self.assertIsInstance(DiscRecording.kDRDefaultDate, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeCreationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeModificationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeCheckedDate, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeExpirationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRVolumeEffectiveDate, unicode)
        self.assertIsInstance(DiscRecording.kDRISOMacExtensions, unicode)
        self.assertIsInstance(DiscRecording.kDRISORockRidgeExtensions, unicode)
        self.assertIsInstance(DiscRecording.kDRSuppressMacSpecificFiles, unicode)
        self.assertIsInstance(DiscRecording.kDRAllFilesystems, unicode)
        self.assertIsInstance(DiscRecording.kDRISO9660, unicode)
        self.assertIsInstance(DiscRecording.kDRISO9660LevelOne, unicode)
        self.assertIsInstance(DiscRecording.kDRISO9660LevelTwo, unicode)
        self.assertIsInstance(DiscRecording.kDRJoliet, unicode)
        self.assertIsInstance(DiscRecording.kDRHFSPlus, unicode)
        self.assertIsInstance(DiscRecording.kDRUDF, unicode)
        self.assertIsInstance(DiscRecording.kDRISO9660VersionNumber, unicode)
        self.assertIsInstance(DiscRecording.kDRInvisible, unicode)
        self.assertIsInstance(DiscRecording.kDRCreationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRContentModificationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRAttributeModificationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRAccessDate, unicode)
        self.assertIsInstance(DiscRecording.kDRBackupDate, unicode)
        self.assertIsInstance(DiscRecording.kDRRecordingDate, unicode)
        self.assertIsInstance(DiscRecording.kDREffectiveDate, unicode)
        self.assertIsInstance(DiscRecording.kDRExpirationDate, unicode)
        self.assertIsInstance(DiscRecording.kDRPosixFileMode, unicode)
        self.assertIsInstance(DiscRecording.kDRPosixUID, unicode)
        self.assertIsInstance(DiscRecording.kDRPosixGID, unicode)
        self.assertIsInstance(DiscRecording.kDRHFSPlusTextEncodingHint, unicode)
        self.assertIsInstance(DiscRecording.kDRHFSPlusCatalogNodeID, unicode)
        self.assertIsInstance(DiscRecording.kDRMacFileType, unicode)
        self.assertIsInstance(DiscRecording.kDRMacFileCreator, unicode)
        self.assertIsInstance(DiscRecording.kDRMacWindowBounds, unicode)
        self.assertIsInstance(DiscRecording.kDRMacIconLocation, unicode)
        self.assertIsInstance(DiscRecording.kDRMacScrollPosition, unicode)
        self.assertIsInstance(DiscRecording.kDRMacWindowView, unicode)
        self.assertIsInstance(DiscRecording.kDRMacFinderFlags, unicode)
        self.assertIsInstance(DiscRecording.kDRMacExtendedFinderFlags, unicode)
        self.assertIsInstance(DiscRecording.kDRMacFinderHideExtension, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFWriteVersion, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVersion102, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVersion150, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFPrimaryVolumeDescriptorNumber, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVolumeSequenceNumber, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFMaxVolumeSequenceNumber, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFInterchangeLevel, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFMaxInterchangeLevel, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFApplicationIdentifierSuffix, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVolumeSetIdentifier, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVolumeSetTimestamp, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFVolumeSetImplementationUse, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFRealTimeFile, unicode)
        self.assertIsInstance(DiscRecording.kDRUDFExtendedFilePermissions, unicode)


if __name__ == "__main__":
    main()
