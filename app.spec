# -*- mode: python ; coding: utf-8 -*-


import os

for address, dirs, files in os.walk('.'):
    if 'site-packages' in os.path.basename(address):
        if 'lib64' in address:
            continue
        site_packages = address
block_cipher = None


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        (os.path.join(site_packages, 'customtkinter'), 'customtkinter/'),
        ],
    hiddenimports=['sip', 'cffi'],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)

