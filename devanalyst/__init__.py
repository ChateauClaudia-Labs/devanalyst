# ** WATCH OUT ** The '.' in front of 'jupyter_nb_importer' is necessary for this package to work. Otherwise
#                   the import will fail. Even though the '.' will give error messages if you run this 
#                   Python script "as is" (as opposed to as a package initializer), you can ignore those error messages.
#                   They will not happen when you actually import this package, and the absence of a '.' would instead
#                   prevent this package from being imported.
from .jupyter_nb_importer import NotebookFinder
import sys

# Run this so that all Jupyter notebooks in this package are imported as Python modules
sys.meta_path.append(NotebookFinder())