'''
Wrappers for the "GameplayKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="4.1b1"

setup(
    name='pyobjc-framework-GameplayKit',
    description = "Wrappers for the framework GameplayKit on macOS",
    min_os_level="10.11",
    packages = [ "GameplayKit" ],
    ext_modules = [
        Extension("GameplayKit._GameplayKit",
            [ "Modules/_GameplayKit.m" ],
            extra_link_args=["-framework", "GameplayKit"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_GameplayKit')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-SpriteKit>='+VERSION,
    ],
    long_description=__doc__,
)