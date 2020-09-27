import setuptools 
setuptools.setup (
    name = "wifiqr-gui",
    version="1.0.1",
    author="Pyae Phyo Hein",
    author_email="pyaephyohein.info.3326@gmail.com",
    descripton="Wifi Qr creater and generator for linux",
    packages=["wifiqr-gui"],
    entry_points = {
        'console_scripts' : ['wifiqr-gui=wifiqr-gui.wifiqr:wifiqr']
    },
    install_requires=[
        'qrcode',
        'PyQt5'
    ]
    )