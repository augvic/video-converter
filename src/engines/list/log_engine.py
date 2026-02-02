import sys
from os import path, makedirs
from datetime import datetime

class LogEngine:
    
    def _make_output_dir(self, folder: str) -> str:
        if getattr(sys, "frozen", False):
            log_dir = path.abspath(path.join(path.dirname(sys.executable), "storage", "logs", folder))
        else:
            log_dir = path.abspath(path.join(path.dirname(__file__), "..", "..", "..", "storage", "logs", folder))
        makedirs(log_dir, exist_ok=True)
        return log_dir
    
    def _write_on_file(self, log_dir: str, type: str, text: str) -> None:
        with open(f"{log_dir}/{datetime.now().replace(microsecond=0).strftime("%d-%m-%Y")}_{type}.txt", "a", encoding="utf-8") as log:
            log.write(f"⌚ <{datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")}>\n" + text + "\n\n")
            log.flush()
    
    def write(self, folder: str, text: str, type: str) -> None:
        log_dir = self._make_output_dir(folder)
        self._write_on_file(log_dir, type, text)
