import sys
import ffmpeg
from pathlib import Path

class ConverterEngine:
    
    def convert(self, input_path: str, format_output: str) -> None:
        if getattr(sys, "frozen", False):
            storage_path = Path(sys.executable).parent / "storage"
        else:
            storage_path = Path(__file__).resolve().parents[3] / "storage"
        videos_path = storage_path / "videos"
        ffmpeg_path = storage_path / "ffmpeg.exe"
        videos_path.mkdir(parents=True, exist_ok=True)
        if not Path(input_path).is_file():
            raise FileNotFoundError("❌ Vídeo a ser convertido não foi encontrado.")
        if not ffmpeg_path.is_file():
            raise FileNotFoundError('❌ FFmpeg não localizado em "storage". Baixe e coloque seu executável na pasta.')
        format_output = format_output.lower().lstrip(".")
        video_name = Path(input_path).stem + f".{format_output}"
        output = videos_path / video_name
        ffmpeg.input(input_path).output(
            str(output),
            vcodec="libx264",
            acodec="aac",
            movflags="faststart"
        ).run(cmd=str(ffmpeg_path))
