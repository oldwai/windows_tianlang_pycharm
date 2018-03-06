# -*- mode: python -*-

block_cipher = None


a = Analysis(['test_get.py', 'Ver_push_sys_BasePage.py', 'LoginPage.py'],
             pathex=['E:\\Pycharm_py\\selenium_py\\ver_push_system'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test_get',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='F:\\test.ico')
