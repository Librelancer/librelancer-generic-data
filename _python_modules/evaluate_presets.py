# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':

	import _python_modules.common as c

	# TODO: systems presets from _editable_data_presets must be parsed here and
	# the data should be placed into _python_modules.common.<lsit>
	# After this, the symlinks will be made and data files generated.
	
	def make():
		
		# TODO: move to status_report, leave a trigger to common
		print(c.col.OKBLUE, "EVALUATING PRESETS IS FINISHED", c.col.ENDC)


