# -*- mode: python ; coding: utf-8 -*-

import platform

block_cipher = None
application_name = 'SourceCalc'
icon_file = './ui/icon'
icon_extension = '.icns' if platform.system() == 'Darwin' else '.ico'

a = Analysis(['main.py'],
             pathex=['./'],
             binaries=[],
             datas=[],
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
             bundle_identifier='com.manchenkov.source_calc',
             info_plist={
                 'NSPrincipalClass': 'NSApplication',
                 'NSAppleScriptEnabled': False,
             })
