# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':

	# Modules
	import _python_modules.common as c
	from _python_modules.common import print_file, write_file

	# Main
	import _python_modules.data_files.librelancer_ini

	# JSON (TODO: keep expanding as new files are implemented)
	import _python_modules.data_files.infocards_json
	import _python_modules.data_files.strings_json

	# INI (TODO: keep expanding as new files are implemented)
	import _python_modules.data_files.base_missions_ini
	import _python_modules.data_files.cameras_ini
	import _python_modules.data_files.costumes_ini
	import _python_modules.data_files.constants_ini
	import _python_modules.data_files.bodyparts_ini
	import _python_modules.data_files.effect_shapes_ini
	import _python_modules.data_files.fonts_ini
	import _python_modules.data_files.hud_ini
	import _python_modules.data_files.infocardmap_ini
	import _python_modules.data_files.mouse_ini
	import _python_modules.data_files.navmap_ini
	import _python_modules.data_files.newcharacter_ini
	import _python_modules.data_files.rich_fonts_ini
	import _python_modules.data_files.shiparch_ini
	import _python_modules.data_files.solararch_ini
	import _python_modules.data_files.stararch_ini
	import _python_modules.data_files.universe_ini

	def make():
		# ============================ MAIN SEQUENCE =================================
		# Do not edit anything in this block in order to ensure all .ini and .json files
		# are generated properly and to their rightful destinations.

		# Main "librelancer.ini" generation.
		_python_modules.data_files.librelancer_ini.make()

		# INI data files generation.
		_python_modules.data_files.base_missions_ini.make() # TODO
		_python_modules.data_files.cameras_ini.make()
		_python_modules.data_files.costumes_ini.make() # TODO
		_python_modules.data_files.constants_ini.make() # TODO
		_python_modules.data_files.bodyparts_ini.make() # TODO
		_python_modules.data_files.effect_shapes_ini.make() # TODO
		_python_modules.data_files.fonts_ini.make() # TODO
		_python_modules.data_files.hud_ini.make() # TODO
		_python_modules.data_files.infocardmap_ini.make() # TODO
		_python_modules.data_files.mouse_ini.make() # TODO
		_python_modules.data_files.navmap_ini.make() # TODO
		_python_modules.data_files.newcharacter_ini.make() # TODO
		_python_modules.data_files.rich_fonts_ini.make() # TODO
		_python_modules.data_files.shiparch_ini.make() # TODO
		_python_modules.data_files.solararch_ini.make() # TODO
		_python_modules.data_files.stararch_ini.make() # TODO
		_python_modules.data_files.universe_ini.make() # TODO

		# JSON data files generation.
		_python_modules.data_files.strings_json.make() #TODO: make interface like infocards

		# Infocards are generated last, only after all the ini presets are done.
		_python_modules.data_files.infocards_json.make()


		# ============================ WRITING FILES =================================
		# DATA directories and "librelancer.ini"
		write_file(c.librelancer_ini_path, c.librelancer_ini_out)

		# JSON data files
		write_file(c.json_files["infocards"], c.infocards_json_out)
		write_file(c.json_files["strings"], c.strings_json_out)

		# INI data files
		write_file(c.ini_files["cameras"], c.cameras_ini_out)
		write_file(c.ini_files["costumes"], c.costumes_ini_out)
		write_file(c.ini_files["constants"], c.constants_ini_out)
		write_file(c.ini_files["fonts"], c.fonts_ini_out)
		write_file(c.ini_files["bodyparts"], c.bodyparts_ini_out)
		write_file(c.ini_files["effect_shapes"], c.effect_shapes_ini_out)
		write_file(c.ini_files["fonts"], c.fonts_ini_out)
		write_file(c.ini_files["HUD"], c.hud_ini_out)
		write_file(c.ini_files["infocardmap"], c.infocardmap_ini_out)
		write_file(c.ini_files["mbases"], c.base_missions_ini_out)
		write_file(c.ini_files["mouse"], c.mouse_ini_out)
		write_file(c.ini_files["navmap"], c.navmap_ini_out)
		write_file(c.ini_files["newcharacter"], c.newcharacter_ini_out)
		write_file(c.ini_files["rich_fonts"], c.rich_fonts_ini_out)
		write_file(c.ini_files["ships"], c.shiparch_ini_out)
		write_file(c.ini_files["solar"], c.solararch_ini_out)
		write_file(c.ini_files["stars"], c.stararch_ini_out)
		write_file(c.ini_files["universe"], c.universe_ini_out)
		# TODO all other

		# TODO: STUB FILES!!!!!
		write_file(c.ini_files["stub_navbar"], ";stub")

		# ============================ DEBUG OPTIONS =================================
		# Uncomment to enable specific outputs.
		# Prints generated data files to command line without writing the files.

		## DATA directories and "librelancer.ini"
		#print_file(c.librelancer_ini_path, c.librelancer_ini_out)

		## JSON data files
		#print_file(c.json_files["infocards"], c.infocards_json_out)
		#print_file(c.json_files["strings"], c.strings_json_out)

		## INI data files
		#print_file(c.ini_files["cameras"], c.cameras_ini_out)
		#print_file(c.ini_files["costumes"], c.costumes_ini_out)
		#print_file(c.ini_files["constants"], c.constants_ini_out)
		#print_file(c.ini_files["fonts"], c.fonts_ini_out)
		#print_file(c.ini_files["bodyparts"], c.bodyparts_ini_out)
		#print_file(c.ini_files["effect_shapes"], c.effect_shapes_ini_out)
		#print_file(c.ini_files["fonts"], c.fonts_ini_out)
		#print_file(c.ini_files["HUD"], c.hud_ini_out)
		#print_file(c.ini_files["infocardmap"], c.infocardmap_ini_out)
		#print_file(c.ini_files["mbases"], c.base_missions_ini_out)
		#print_file(c.ini_files["mouse"], c.mouse_ini_out)
		#print_file(c.ini_files["navmap"], c.navmap_ini_out)
		#print_file(c.ini_files["newcharacter"], c.newcharacter_ini_out)
		#print_file(c.ini_files["rich_fonts"], c.rich_fonts_ini_out)
		#print_file(c.ini_files["ships"], c.shiparch_ini_out)
		#print_file(c.ini_files["solar"], c.solararch_ini_out)
		#print_file(c.ini_files["stars"], c.stararch_ini_out)
		#print_file(c.ini_files["universe"], c.universe_ini_out)
		## TODO all other

		## TODO: STUB FILES!!!!!
		#print_file(c.ini_files["stub_navbar"], ";stub")

		# TODO: move to status_report, leave a trigger to common
		print(c.col.OKBLUE, "DATA FILES GENERATION FINISHED", c.col.ENDC)
