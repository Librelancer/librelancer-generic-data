# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import nl, eq, space # for printing
	
	def make():
		global c
		# TODO
		c.rich_fonts_ini_out = """
[FontFiles]
file = FONTS/TitilliumWeb-Regular.ttf

[TrueType]
font = 0, Titillium Web, 20
font = 1, Titillium Web, 25
font = 2, Titillium Web, 30
font = 3, Titillium Web, 35

; Allow sourcing fonts from the "fonts" directory, where rich_fonts.ini is
; directly without installing those fonts.
"""

