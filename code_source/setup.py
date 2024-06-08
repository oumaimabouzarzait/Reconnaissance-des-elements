from setuptools import setup

APP = ['finalopencv.py']
OPTIONS = {
    'argv_emulation': True
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_required=['py2app']
)
