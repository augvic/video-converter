from .engines.engines import Engines
from .convert_task import ConvertTask
from .cli import Cli

class VideoConverter:
    
    def __init__(self) -> None:
        self.engines = Engines()
        self.converter_task = ConvertTask(self.engines)
        self.cli = Cli(self.converter_task)
    
    def main(self) -> None:
        self.cli.main()
