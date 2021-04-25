# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':

	import _python_modules.common as c
	
	# DO NOT EDIT THIS BLOCK, THE NAMES ARE HARDCODED.
	
	def make():
		global c
		
		c.asset_list_cmp = c.scan_assets("*.cmp")
