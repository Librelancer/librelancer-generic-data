# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	import _editable_data_presets.infocard_styles as s
	
	def make():
	
		# TODO make systems class, make systems_list object in common
	
	
		global c, s
		# TODO: text comes from the presets
		id1 = s.system_card("System 01", "A test system 1.").infocard_id
		id2 = s.system_card("System 02", "A test system 2.").infocard_id
		id3 = s.system_card("System 03", "A test system 3.").infocard_id


