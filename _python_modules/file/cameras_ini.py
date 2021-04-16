# ============================= REFERENCE =====================================
# JFLP will automatically calculate an appropriate value for the resolution.
# To override it, append '!' (e.g. "fovx = 70!").
# Some common values:

# Ratio  WinCamera  Other
# -----  ---------  ------
# 4:3	  54.432    70
# 16:10   63.361    80.077
# 16:9	  68.878    86.067

# ================================ CODE =======================================
# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import nl, eq, space # for printing
	from pathlib import Path
	import os
	
	# camera entry        |   block name   |   FOV   |   znear   |
	entries = {
		"win_camera"          : ("[WinCamera]", "54.432"),
		"cockpit_camera"      : ("[CockpitCamera]", "70"),
		"third_person_camera" : ("[ThirdPersonCamera]", "70"),
		"death_camera"        : ("[DeathCamera]", "70"),
		"turret_camera"       : ("[TurretCamera]", "70"),
		"rear_camera"         : ("[RearViewCamera]", "70"),
	}
	
	fovx_name = "fovx"
	
	def make():
		global c
		for key, value in entries.items():
			c.cameras_ini_out += value[0] + nl + fovx_name + eq + value[1] + nl*2

