# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import nl, eq, space # for printing
	
	def make():
		global c
		# TODO
		c.fonts_ini_out = """
[FontFiles]
file = FONTS/TitilliumWeb-Regular.ttf

; fonts.ini, at least a Normal entry is required
; This defines the default font for the user interface

[TrueType]
nickname = Normal
font = Titillium Web
"""


