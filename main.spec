# -*- mode: python ; coding: utf-8 -*-
import platform

from PyInstaller.building.api import COLLECT, EXE, PYZ
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.osx import BUNDLE

block_cipher = None
application_name = 'SourceCalc'
application_id = 'com.manchenkov.source_calc'
icon_file = './src/data/icon'
icon_extension = '.icns' if platform.system() == 'Darwin' else '.ico'
entry_point = 'src/main.py'

a = Analysis([entry_point],
             pathex=['./'],
             binaries=[],
             datas=[('./src/data/icon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=application_name,
          debug=False,
          bootloader_ignore_signals=False,
          icon=f"{icon_file}{icon_extension}",
          strip=False,
          upx=True,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=application_name)

app = BUNDLE(coll,
             name=f"{application_name}.app",
             icon=f"{icon_file}{icon_extension}",
             bundle_identifier=application_id,
             info_plist={
                 'NSPrincipalClass': 'NSApplication',
                 'NSAppleScriptEnabled': False,
             })
