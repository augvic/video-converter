from PyInstaller.building.build_main import Analysis
from PyInstaller.building.api import EXE, PYZ
from os import path, makedirs

analysis = Analysis(
    scripts=['main.py'],
    pathex=[path.abspath('.')],
    datas=[],
    optimize=0
)

pyz = PYZ(analysis.pure)

exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    name='VideoConverter',
    upx=True,
    icon="icon.ico"
)

storage_path = path.abspath(path.join(path.dirname(__name__), "dist", "storage"))
makedirs(storage_path, exist_ok=True)
