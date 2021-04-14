# Run this script to generate all the .ini and .json data according to data
# in _python_editable_presets.
# In a command line run "python3 build_data.py" and that is all.

import _python_modules.common

import _python_modules.gen_directories
import _python_modules.gen_infocards_json
import _python_modules.gen_strings_json
import _python_modules.gen_librelancer_ini

# ============================ MAIN SEQUENCE =================================
_python_modules.gen_directories.make_directories()
_python_modules.gen_librelancer_ini.write_librelancer_ini()
_python_modules.gen_infocards_json.write_infocards()


# ============================ DEBUG OPTIONS =================================
# Uncomment to enable specific outputs. Should be after main sequence above.
# Prints generated data files to command line.

_python_modules.gen_infocards_json.print_infocards()
_python_modules.gen_librelancer_ini.print_librelancer_ini()
