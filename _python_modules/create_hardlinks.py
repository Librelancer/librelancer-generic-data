# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	
	import _python_modules.common as c
	import _python_modules.assets_files.core_assets
	import _python_modules.assets_files.cmp_assets
	
	def make():
		_python_modules.assets_files.core_assets.make()
		_python_modules.assets_files.cmp_assets.make()
		
		# TODO: move to status_report, leave a trigger to common
		print(c.col.OKBLUE, "HARDLINKING ASSETS WAS FINISHED", c.col.ENDC)
		
