import sys
from cx_Freeze import setup, Executable

# Configurações básicas do build
build_options = {
    "packages": [],
    "excludes": []
}

# Define o modo GUI no Windows
base = "Win32GUI" if sys.platform == "win32" else None

# Setup do executável
setup(
    name="Localize",
    version="1.0",
    description="Aplicação para consulta de dados",
    options={"build_exe": build_options},
    executables=[Executable("main.py", base=base)]
)
