import json
from pathlib import Path

class Ipynb:
    """Class for work with ipynb-files."""
    
    def __init__(self, path_to_file: str | Path):
        self.path = Path(path_to_file)
        self.data: dict | None = None
        self.data_cells: list[dict] | None = None
        self.language: str | None = None

    def open(self) -> dict:
        """Open the file and parse JSON.
        
        Returns:
            dict: Parsed notebook content.
        """
        
        if self.data is None:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        return self.data

    def get_all_cells(self) -> list[dict]:
        """Get all ipynb file cells with markdown and code content.

        Returns:
            list[dict]: Parsed notebook cells.
        """

        if self.data_cells is None:
            self.data_cells = self.open().get("cells", [])
        return self.data_cells

    def get_language(self) -> str:
        """Get the language from ipynb metadata.

        Language is used for formatting in code cells.
        """
        
        if self.language is None:
            metadata = self.open().get("metadata", {})
            kernelspec = metadata.get("kernelspec", {})
            self.language = kernelspec.get("language", "python")
        return self.language
