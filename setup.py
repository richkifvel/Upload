# -*- coding: utf-8 -*-
from setuptools import setup



APP = ['/Users/richlovell/Documents/Scripts/Python/Upload/Upload.py']
APP_NAME = "Uploader"
DATA_FILES = ['/Users/richlovell/Documents/Scripts/Python/Upload/Upload.sh']





OPTIONS = {
    'argv_emulation': True,
    'iconfile': '/Users/richlovell/Documents/Scripts/Python/Upload/iconB.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Making Sandwiches",
        'CFBundleIdentifier': "com.kifvel.osx.uploader",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2017, Richard Kifvel, All Rights Reserved"
    }
}


setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)



#setup(
#    app=["Upload.py"],
#    setup_requires=["py2app"],
#)



#/Users/richlovell/Documents/Scripts/Python/Upload/