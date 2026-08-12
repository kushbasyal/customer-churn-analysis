import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
sys.path.append(str(project_root / "scripts"))

'''
project_root = Path(__file__).resolve().parent.parent
→ Finds the project root by going up two folders from the current Python file.

sys.path.append(str(project_root / "scripts"))
→ Adds the scripts folder to Python's search path so we can import files from it.

In short:
Find project root → find scripts folder → tell Python to search there.

'''

from scripts.dataloader import load_data
from scripts.config_paths import raw_data_path

df = load_data(raw_data_path)

print(df.head())