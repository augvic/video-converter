from .engines.engines import Engines

class ConvertTask:
    
    def __init__(self, engines: Engines) -> None:
        self.engines = engines
    
    def main(self, input_path: str, format_output: str) -> None:
        try:
            self.engines.converter_engine.convert(input_path, format_output)
        except Exception as error:
            self.engines.log_engine.write("convert_task_logs", f"{error}", "errors")
            raise
