# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	from pathlib import Path

	# =========================== FOR PRINTING ================================
	space = "    "
	nl = "\n"
	eq = " = "
	divider = "------------------------"

	# ========================== GENERATED DATA ===============================
	# TODO Storing in common for future access in generation process.
	# Inner data (for generations)
	strings_list = []
	infocards_list = []
	
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
	}

	# Top-level json files.
	# Paths can be renamed. Keys must not change
	json_files = {
		"infocards" : directories["strings"].joinpath("infocards.json"),
		"strings" : directories["strings"].joinpath("strings.json"),
	}

	# Top-level ini files.
	# Paths can be renamed. Keys must not change
	# TODO: keep adding paths
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
		"navmap" : directories["navmap"].joinpath("navmap.ini"),
		"solar" : directories["solar"].joinpath("solararch.ini"),
		"stars" : directories["solar"].joinpath("stararch.ini"),
		"ships" : directories["ships"].joinpath("shiparch.ini"),
		"universe" : directories["universe"].joinpath("universe.ini"),
	}
	
	# =============================== WRITING =================================
	def write_file(file_path, contents):
		f = open(file_path, "w")
		f.write(contents)
		f.close()
		
	def print_file(file_path, contents):
		print(divider)
		print(file_path)
		print(divider)
		print(contents)
