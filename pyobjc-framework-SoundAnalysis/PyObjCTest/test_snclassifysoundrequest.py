import SoundAnalysis
from PyObjCTools.TestSupport import *


class TestSNClassifySoundRequest(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            SoundAnalysis.SNClassifySoundRequest.initWithMLModel_error_, 1
        )