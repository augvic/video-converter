from .converter_engine import ConverterEngine
from .converter_task import ConverterTask
from .cli import Cli

class VideoConverter:
    
    def __init__(self) -> None:
        self.converter_engine = ConverterEngine()
        self.converter_task = ConverterTask(self.converter_engine)
        self.cli = Cli(self.converter_task)
    
    def main(self) -> None:
        self.cli.main()
