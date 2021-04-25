# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':

	import _python_modules.common as c
	
	# DO NOT EDIT THIS BLOCK, THE NAMES ARE HARDCODED.
	
	def make():
		global c
		
		# File name to directory, as specified in common.directories.
		c.link_overwrite("cursor.txm", "interface")
		c.link_overwrite("navmap.txm", "navmap")
