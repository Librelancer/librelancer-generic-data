# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	from pathlib import Path
	import os, fnmatch, shutil, sys

	# =========================== FOR PRINTING ================================
	space = "    "
	nl = "\n"
	eq = " = "
	divider = "---------------------------------------------------"
	class col: # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal 
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		ERROR = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	
	# =========================== GLOBAL DATA =================================
	# Do not change!
	BUILD_ERROR = False
	
	ERROR_MESSAGES = []
	WARNING_MESSAGES = []
	SUCCESS_MESSAGES = []
	
	GLOBAL_INFOCARD_ID = 0 # Start at 0 because first call to it will increment.
	GLOBAL_STRING_ID = 0 # Start at 0 because first call to it will increment.
	
	# ========================== GENERATED DATA ===============================
	# TODO Storing in common for future access in generation process.
	# Inner data (for generations)
	strings_list = []
	infocards_list = []
	
	systems_list = [] #TODO get it from _python_modules.evaluate_presets
	
	# Generated data
	infocards_json_out = ""
	strings_json_out = ""
	
	librelancer_ini_out = ""
	
	base_missions_ini_out = ""
	cameras_ini_out = ""
	costumes_ini_out = ""
	constants_ini_out = ""
	bodyparts_ini_out = ""
	effect_shapes_ini_out = ""
	fonts_ini_out = ""
	hud_ini_out = ""
	infocardmap_ini_out = ""
	mouse_ini_out = ""
	navmap_ini_out = ""
	newcharacter_ini_out = ""
	rich_fonts_ini_out = ""
	shiparch_ini_out = ""
	solararch_ini_out = ""
	stararch_ini_out = ""
	universe_ini_out = ""
	# =============================== ASSETS ==================================
	asset_list_txm = [] # Texture assets.
	asset_list_ttf = [] # Fonts.

	# =============================== PATHS ===================================
	# Main directory. Relative to "build_data.py" location. Do not use absolute.
	# Do not change.
	data_path = Path("DATA")

	# Main .ini file. Relative to "build_data.py" location. Do not use absolute.
	# Do not change.
	librelancer_ini_path = Path("librelancer.ini")

	# Subdirectores are within the data_path dy design. "data_path" must be in.
	# Paths can be renamed. Keys must not change
	# TODO: keep adding paths
	directories = {
		"data_path" : data_path,
		"characters" : data_path.joinpath("CHARACTERS"),
		"constants" : data_path.joinpath("CONSTANTS"),
		"effects" : data_path.joinpath("EFFECTS"),
		"fonts" : data_path.joinpath("FONTS"),
		"interface" : data_path.joinpath("INTERFACE"),
		"missions" : data_path.joinpath("MISSIONS"),
		"navmap" : data_path.joinpath("INTERFACE", "NAVMAP"),
		"ships" : data_path.joinpath("SHIPS"),
		"solar" : data_path.joinpath("SOLAR"),
		"strings" : data_path.joinpath("STRINGS"),
		"universe" : data_path.joinpath("UNIVERSE"),
		# TODO: STUB!!!
		"stub_interface_baseside" : data_path.joinpath("INTERFACE", "BASESIDE"),
	}

	# Top-level json files.
	# Paths can be renamed.
	#
	#
	#
	#			 Keys must not change! COMPATIBILITY!
	#
	#
	#
	json_files = {
		"infocards" : directories["strings"].joinpath("infocards.json"),
		"strings" : directories["strings"].joinpath("strings.json"),
	}

	# Top-level ini files.
	# Paths can be renamed.
	# TODO: keep adding paths
	#
	#
	#
	#			 Keys must not change! COMPATIBILITY!
	#
	#
	#
	ini_files = {
		"bodyparts" : directories["characters"].joinpath("bodyparts.ini"),
		"cameras" : directories["constants"].joinpath("cameras.ini"),
		"constants" : directories["constants"].joinpath("constants.ini"),
		"costumes" : directories["characters"].joinpath("costumes.ini"),
		"effect_shapes" : directories["effects"].joinpath("effect_shapes.ini"),
		"fonts" : directories["fonts"].joinpath("fonts.ini"),
		"rich_fonts" : directories["fonts"].joinpath("rich_fonts.ini"),
		"HUD" : directories["interface"].joinpath("hud.ini"),
		"infocardmap" : directories["interface"].joinpath("infocardmap.ini"),
		"mbases" : directories["missions"].joinpath("base_missions.ini"),
		"mouse" : directories["interface"].joinpath("mouse.ini"),
		"newcharacter" : directories["characters"].joinpath("newcharacter.ini"),
		"navmap" : directories["navmap"].joinpath("navmap.ini"),
		"solar" : directories["solar"].joinpath("solararch.ini"),
		"stars" : directories["solar"].joinpath("stararch.ini"),
		"ships" : directories["ships"].joinpath("shiparch.ini"),
		"universe" : directories["universe"].joinpath("universe.ini"),
		
		# TODO: STUB FILES!!! They have to be removed eventually.
		"stub_navbar" : directories["stub_interface_baseside"] \
			.joinpath("navbar.ini"),
		
	}
	
	# ========================= MENUS AND FUNCTIONS ===========================
	# TODO: add symlinking and a small menu
	def write_file(file_path, contents):
		f = open(file_path, "w")
		f.write(contents)
		f.close()
		
	def print_file(file_path, contents):
		print(divider)
		print(file_path)
		print(divider)
		print(contents)
	
	# Increments ID globally every time there is a call to infocard class
	def global_infocard_id():
		global GLOBAL_INFOCARD_ID
		GLOBAL_INFOCARD_ID += 1
		current_id = str(GLOBAL_INFOCARD_ID)
		return current_id
	
	# Increments ID globally every time there is a call to string class
	def global_string_id():
		global GLOBAL_STRING_ID
		GLOBAL_STRING_ID += 1
		current_id = str(GLOBAL_STRING_ID)
		return current_id
	
	def remove_target_files(filetype): # filetype is "*.ini", "*.json"
		for rootDir, subdirs, filenames in os.walk('.'):
			for filename in fnmatch.filter(filenames, filetype):
				try: os.remove(os.path.join(rootDir, filename))
				except OSError: pass # TODO Better printout
				
	def find_asset_file(filename_find): # Finds exact and only one file or panics
		global BUILD_ERROR
		namelist = []
		for rootDir, subdirs, filenames in os.walk('./_editable_assets'):
			if filename_find in filenames:
				namelist.append(os.path.join(rootDir, filename_find))
		if len(namelist) == 1: 
			return namelist[0]
		elif len(namelist) == 0:
			print(col.ERROR, "ERROR: NO ASSET FILE FOUND:", filename_find, col.ENDC)
			BUILD_ERROR = True
		else:
			print(col.ERROR, "ERROR: FOUND MORE THAN A SINGLE FILE WITH GIVEN NAME:", filename_find, col.ENDC)
			print(namelist)
			BUILD_ERROR = True
			
	def scan_assets(filetype): # Returns a list of files, may be empty
		namelist = []
		for rootDir, subdirs, filenames in os.walk('./_editable_assets'):
			for filename in fnmatch.filter(filenames, filetype):
				namelist.append(os.path.join(rootDir, filename))
		if len(namelist) == 0:
			print(col.WARNING, "Warning: no assets of type:", filetype, col.ENDC)
			# TODO collect all warning messages and print them separately
		return namelist
			
	def link_overwrite(source_name, target_dir):
		global BUILD_ERROR
		source = find_asset_file(source_name)
		target = os.path.join(directories[target_dir], source_name)
		try: os.remove(target)
		except OSError: pass #TODO better printout
		try: os.link(source, target)
		except TypeError: 
			print(col.ERROR, "ERROR: UNABLE TO HARDLINK A TARGET FILE:", target, col.ENDC)
			BUILD_ERROR = True
				
	def remove_target_directory(path): 
		shutil.rmtree(path, ignore_errors=True)
