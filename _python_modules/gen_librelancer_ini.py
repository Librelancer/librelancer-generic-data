# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	from _python_modules.common import librelancer_ini_path, data_path
	from _python_modules.common import ini_files, json_files
	from _python_modules.common import nl, eq, space, divider # for printing
	from pathlib import Path
	import os
	
	output = ""
	
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
	
	def make_librelancer_ini():
		global output
		output += freelancer_header + nl 
		output += data_path_name + eq + str(data_path) + nl
		output += nl + json_header + nl
		for key, value in json_files_rel.items():
			output += json_name + eq + str(value) + nl
		output += nl + data_header + nl
		for key, value in ini_files_rel.items():
			output += key + eq + str(value) + nl
		
	def write_librelancer_ini():
		global output
		make_librelancer_ini()
		f = open(librelancer_ini_path, "w")
		f.write(output)
		f.close()
		
	def print_librelancer_ini():
		global output
		print(divider)
		print(librelancer_ini_path)
		print(divider)
		print(output)
