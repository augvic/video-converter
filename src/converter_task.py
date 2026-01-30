from .converter_engine import ConverterEngine

class Response:
    
    def __init__(self, success: bool, message: str) -> None:
        self.success = success
        self.message = message

class ConverterTask:
    
    def __init__(self, converter_engine: ConverterEngine) -> None:
        self.converter_engine = converter_engine
    
    def main(self, input: str) -> Response:
        try:
            response = self.converter_engine.convert(input)
            return Response(success=True, message=response.message)
        except Exception as error:
            raise Exception(f"❌ Erro na tarefa de converter: {error}")
