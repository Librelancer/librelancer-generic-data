# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import json_files
	from _python_modules.common import nl, eq, space, divider # for printing

	
# ========================== EDIT STRINGS HERE ================================
# TODO: automatically make a list from all the .ini refs.
	def make():
		global c
		c.strings_list.append(
			"String1",
		)
		
		strings_json_start = "{" + nl + space +'"filetype": "strings",'\
			+ nl + space + '"data": {' + nl
		strings_json_end = space + "}" + nl + "}"
		c.strings_json_out = ""

		c.strings_json_out += strings_json_start
		for i in range(len(c.strings_list)):
			c.strings_json_out += space*2 + '"'+str(i+1)+'" : "' + c.strings_list[i] + '",'
			c.strings_json_out += nl
		c.strings_json_out += strings_json_end

