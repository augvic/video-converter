import sys
from pathlib import Path
from os import makedirs

from .engines.engines import Engines
from .convert_task import ConvertTask
from .cli import Cli

class VideoConverter:
    
    def __init__(self) -> None:
        if getattr(sys, "frozen", False):
            storage_path = Path(sys.executable).parent / "storage"
        else:
            storage_path = Path(__file__).resolve().parents[3] / "storage"
            makedirs(storage_path, exist_ok=True)
        self.engines = Engines()
        self.converter_task = ConvertTask(self.engines)
        self.cli = Cli(self.converter_task)
    
    def main(self) -> None:
        self.cli.main()
