# Run this script to generate all the .ini and .json data according to data
# in _python_editable_presets.
# In a command line run "python3 build_data.py" and that is all.

from os import system, name;
import _python_modules.common as c

# Clear term
if name == "nt": _ = system("clc")
else: _ = system("clear")

import _python_modules.create_directories
import _python_modules.create_datafiles
import _python_modules.create_hardlinks
import _python_modules.evaluate_presets

# ============================ MAIN SEQUENCE =================================
# Do not edit anything in this block in order to ensure all .ini and .json files
# are generated properly and to their rightful destinations.

# This call blanket-evaluates all the data in "_editable_data_presets"
# folder, including the modules there. Must preceed everything else.
print(c.divider)

_python_modules.evaluate_presets.make()
_python_modules.create_directories.make()
_python_modules.create_hardlinks.make()
_python_modules.create_datafiles.make()

# TODO warning and error messages should be popped here
# TODO: move to status_report, leave a trigger to common
# TODO make a "status_report" function that enacts messages
if not c.BUILD_ERROR: print(c.col.OKGREEN, "GAME DATA WAS BUILT", c.col.ENDC)
else: print(c.col.ERROR, "GAME DATA WAS NOT FULLY BUILT DUE TO PREVIOUS ERRORS", c.col.ENDC)
print(c.divider)
