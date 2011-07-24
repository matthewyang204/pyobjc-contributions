'''
Python mapping for the SyncServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import CoreData

from SyncServices import _metadata

sys.modules['SyncServices'] = mod = objc.ObjCLazyModule('SyncServices',
    "com.apple.syncservices",
    objc.pathForFramework("/System/Library/Frameworks/SyncServices.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       'objc': objc,
    }, ( CoreData,))