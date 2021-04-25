# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.data_files.infocards_json import infocard, alignment, \
		text, paragraph
	
	# Add new infocard styles here. Each style is a method, which returns 
	# "infocard" class whenever it is called in the ini modules.
	# Formatting options define the style for everything that goes after them.
	# Valid contents for the "infocard" arguments are:
	#--------------------------------------------------------------------------
	# paragraph() - makes an empty new line, can be used between text blocks.
	#--------------------------------------------------------------------------
	# alignment("left" | "right" | "center") - aligns the text block.
	#--------------------------------------------------------------------------
	# text("Text string", **attributes) - the text block itself, with attributes
	#
	# **attributes:
	#	color = ("fuchsia" | "gray" | "blue" | "green" | "aqua" | "red" |
	#			 "yellow" | "white") - assign a color to a given text block.
	#	bold = ("true" | "false" | "default") - enable or disable style.
	#	underline = ("true" | "false" | "default") - enable or disable style.
	#	italic = ("true" | "false" | "default") - enable or disable style.
	#	font = ("n") - where n is an integer, referring to an ID in rich_fonts.
	#--------------------------------------------------------------------------
	
	# Add new styles here
	
	def system_card(sys_name, description):
		return infocard(
			alignment("center"),
			text(sys_name, color="aqua", bold="true", font="3"),
			paragraph(),
			alignment("left"),
			text(description, color="white", bold="false", font="0"),
		)

	def star_card(star_name, description):
		return infocard(
			alignment("center"),
			text(star_name, color="yellow", bold="true", font="3"),
			paragraph(),
			alignment("left"),
			text(description, color="white", bold="false", font="0"),
		)
