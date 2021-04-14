from pathlib import Path

# ============================= FOR PRINTING ==================================
space = "    "
nl = "\n"
eq = " = "
divider = "------------------------"

# ================================= PATHS =====================================
# Main directory. Relative to "build_data.py" location. Do not use absolute.
# Do not change.
data_path = Path("DATA")

# Main .ini file. Relative to "build_data.py" location. Do not use absolute.
# Do not change.
librelancer_ini_path = Path("librelancer.ini")

# Subdirectores are within the data_path dy design. data_path must be included in list.
# Paths can be renamed. Keys must not change
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
ini_files = {
	"bodyparts" : directories["characters"].joinpath("bodyparts.ini"),
	"cameras" : directories["constants"].joinpath("cameras.ini"),
	"constants" : directories["constants"].joinpath("constants.ini"),
	"costumes" : directories["characters"].joinpath("costumes.ini"),
	"effect_shapes" : directories["effects"].joinpath("effect_shapes.ini"),
	"fonts" : directories["fonts"].joinpath("fonts.ini"),
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
