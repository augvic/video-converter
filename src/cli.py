from .converter_task import ConverterTask

class Cli:
    
    def __init__(self, converter_task: ConverterTask) -> None:
        self.converter_task = converter_task
    
    def main(self) -> None:
        try:
            print("Conversor de Vídeos.")
            print("==================================================")
            video_input = input("Informe o caminho do vídeo que será convertido: ")
            response = self.converter_task.main(video_input)
            if response.success:
                print(response.message)
        except Exception as error:
            print(error)
