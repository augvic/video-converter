from .convert_task import ConvertTask

class Cli:
    
    def __init__(self, convert_task: ConvertTask) -> None:
        self.convert_task = convert_task
    
    def main(self) -> None:
        try:
            print("📽️ Conversor de Vídeos.")
            print("==================================================")
            video_input = input("🟢 Informe o caminho do vídeo a ser convertido: ")
            format_output = input("🔵 Informe o formato de saída: ")
            print("==================================================")
            self.convert_task.main(video_input, format_output)
            print('✅ Convertido com sucesso. Se encontra na pasta "storage/videos", mesmo local deste programa.')
        except FileNotFoundError as error:
            print(error)
        except Exception:
            print("❌ Erro desconhecido ao processar. Verifique os logs.")
        finally:
            print("==================================================")
