from .list.converter_engine import ConverterEngine
from .list.log_engine import LogEngine

class Engines:
    
    def __init__(self) -> None:
        self.converter_engine = ConverterEngine()
        self.log_engine = LogEngine()
