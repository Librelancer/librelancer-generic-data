# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	from _python_modules.common import directories
	from pathlib import Path
	
	def make():
		for key, value in directories.items():
			Path(value).mkdir(parents=True, exist_ok=True)
	
	# TODO: a function to make subdirectories when generating systems
	# TODO: a function to create subdirectories for archetypes?
	
