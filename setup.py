from cx_Freeze import setup, Executable
import sys
import os

# Adicione o caminho do ffmpeg.exe e do ícone
ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ffmpeg.exe')
icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text-to-speech.ico')  # Substitua pelo nome do seu arquivo ICO

# Adicione as dependências necessárias
build_exe_options = {
    "packages": ["os", "subprocess", "whisper", "docx", "PyQt5"],
    "include_files": [ffmpeg_path, icon_path]  # Inclui o ffmpeg.exe e o ícone no pacote
}

setup(
    name="TranscriptionApp",
    version="0.1",
    description="Aplicativo de Transcrição de Vídeo para DOCX",
    options={"build_exe": build_exe_options},
    executables=[Executable("TranscriptionApp.py", base="Win32GUI" if sys.platform == "win32" else None, icon=icon_path)]
)