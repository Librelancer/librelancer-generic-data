# Run this script to generate all the .ini and .json data according to data
# in _python_editable_presets.
# In a command line run "python3 build_data.py" and that is all.

import _python_modules.common as c
from _python_modules.common import print_file, write_file

# Main
import _python_modules.file.directories
import _python_modules.file.librelancer_ini

# JSON (TODO: keep expanding as new files are implemented)
import _python_modules.file.infocards_json
import _python_modules.file.strings_json

# INI (TODO: keep expanding as new files are implemented)
import _python_modules.file.base_missions_ini
import _python_modules.file.cameras_ini
import _python_modules.file.costumes_ini
import _python_modules.file.constants_ini
import _python_modules.file.bodyparts_ini
import _python_modules.file.effect_shapes_ini
import _python_modules.file.fonts_ini
import _python_modules.file.hud_ini
import _python_modules.file.infocardmap_ini
import _python_modules.file.mouse_ini
import _python_modules.file.navmap_ini
import _python_modules.file.newcharacter_ini
import _python_modules.file.rich_fonts_ini
import _python_modules.file.shiparch_ini
import _python_modules.file.solararch_ini
import _python_modules.file.stararch_ini
import _python_modules.file.universe_ini

# ============================ MAIN SEQUENCE =================================
# Do not edit anything in this block in order to ensure all .ini and .json files
# are generated properly and to their rightful destinations.

# DATA directories and "librelancer.ini"
# TODO: evaluate presets first, make a generated list of directories (systems)
# and pass it alongside with the main directoriest list to be built.
_python_modules.file.directories.make()
_python_modules.file.librelancer_ini.make()

# JSON data files
_python_modules.file.infocards_json.make()
_python_modules.file.strings_json.make()

# INI data files 
_python_modules.file.cameras_ini.make()
#_python_modules.file.fonts_ini.make() TODO
#_python_modules.file.rich_fonts_ini.make() TODO


# ============================ WRITING FILES =================================
# DATA directories and "librelancer.ini"
write_file(c.librelancer_ini_path, c.librelancer_ini_out)

# JSON data files
write_file(c.json_files["infocards"], c.infocards_json_out)
write_file(c.json_files["strings"], c.strings_json_out)

# INI data files
write_file(c.ini_files["cameras"], c.cameras_ini_out)
#write_file(c.ini_files["fonts"], c.fonts_ini_out) TODO
#write_file(c.ini_files["rich_fonts"], c.rich_fonts_ini_out) TODO
# TODO all other

# ============================ DEBUG OPTIONS =================================
# Uncomment to enable specific outputs.
# Prints generated data files to command line without writing the files.

# DATA directories and "librelancer.ini"
print_file(c.librelancer_ini_path, c.librelancer_ini_out)

# JSON data files
print_file(c.json_files["infocards"], c.infocards_json_out)
print_file(c.json_files["strings"], c.strings_json_out)

# INI data files
print_file(c.ini_files["cameras"], c.cameras_ini_out)
#print_file(c.ini_files["fonts"], c.fonts_ini_out)
#print_file(c.ini_files["rich_fonts"], c.rich_fonts_ini_out)
# TODO all other
