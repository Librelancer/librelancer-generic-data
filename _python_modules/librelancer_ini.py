# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import librelancer_ini_path, data_path
	from _python_modules.common import ini_files, json_files
	from _python_modules.common import nl, eq, space, divider # for printing
	from pathlib import Path
	import os
	
	# Block headers
	freelancer_header = "[Freelancer]"
	json_header = "[JsonResources]"
	data_header = "[Data]"
	
	# The names that appear in the .ini
	data_path_name = "data path"
	json_name = "file"
	
	# Strip the "DATA/" part from the names in the .ini file
	json_files_rel = {}
	ini_files_rel = {}
	root = Path("DATA")
	for key, value in json_files.items():
		json_files_rel[key] = value.relative_to(root)
	for key, value in ini_files.items():
		ini_files_rel[key] = value.relative_to(root)
	
	def make():
		global c
		c.librelancer_ini_out += freelancer_header + nl 
		c.librelancer_ini_out += data_path_name + eq + str(data_path) + nl
		c.librelancer_ini_out += nl + json_header + nl
		for key, value in json_files_rel.items():
			c.librelancer_ini_out += json_name + eq + str(value) + nl
		c.librelancer_ini_out += nl + data_header + nl
		for key, value in ini_files_rel.items():
			c.librelancer_ini_out += key + eq + str(value) + nl
