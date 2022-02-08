# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['EDP_stage1_Bprime.py'],
             pathex=['D:\\Desktop\\EDP stage 1 program\\EDP_stage1_Bprime_1.3'],
             binaries=[],
             datas=[],
             hiddenimports=['psychopy.visual.line','psychopy.visual.rect','psychopy.iohub.devices.display','google.cloud.core','scipy.spatial'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='EDP_stage1_Bprime',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='EDP_stage1_Bprime')
