import ffmpeg
from os import path
from pathlib import Path

class Response:
    
    def __init__(self, success: bool, message: str) -> None:
        self.success = success
        self.message = message

class ConverterEngine:
    
    def convert(self, input: str) -> Response:
        try:
            storage_path = path.abspath(path.join(path.dirname(__file__), "..", "storage"))
            video_name = Path(input).name
            video_name = video_name.split(".")[0] + ".mp4"
            output = storage_path + "\\" + video_name
            print(input)
            print(output)
            ffmpeg.input(input).output(output, vcodec="libx264", acodec="aac", movflags="faststart").run(cmd=storage_path + "\\" + "ffmpeg.exe")
            return Response(success=True, message="✅ Vídeo convertido com sucesso.")
        except Exception as error:
            raise Exception(f"❌ Erro no conversor: {error}")
