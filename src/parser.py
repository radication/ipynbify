import json
from pathlib import Path

class Ipynb:
    """Class for work with ipynb-files."""
    
    def __init__(self, path_to_file: str | Path):
        self.path = Path(path_to_file)
        self.data = None

    def open(self) -> dict:
        """Open the file and parse JSON.
        
        Returns:
            dict: Parsed notebook content.
        """
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data