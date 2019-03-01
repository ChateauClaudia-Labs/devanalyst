# 
import devanalyst
from devanalyst.jupyter_nb_importer import NotebookFinder
import sys

# Run this so that all Jupyter notebooks in this package are imported as Python modules
sys.meta_path.append(NotebookFinder())