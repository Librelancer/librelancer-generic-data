# Example XML schema, source: https://wiki.librelancer.net/rdl
# ================================= EXAMPLE ===================================
# <?xml version="1.0" encoding="UTF-16"?>
# <RDL>
#     <PUSH/>
#     <TRA color="green", bold="true"/>
#     <TEXT>Welcome to the Librelancer infocard example XML!</TEXT>
#     <PARA/>
#     <TEXT>This is the second paragraph</TEXT>
#     <POP/>
# </RDL>
#
# In .json it must go with escape \ character before " characters in strings
# this script does everything and gives the output infocards.json
#
# ================================ ELEMENTS ===================================
# PUSH - should be present at start of RDL
# POP  - should be present at the end of RDL
# TEXT - Adds the text between <TEXT> and </TEXT> to the rich text
#        with the current attributes.
# JUST - Changes the text alignment, in format <JUST LOC="alignment"/>
#        where accepted values are LEFT, RIGHT, CENTER
# PARA - Paragraph, adds a line break. Similar to HTML <p>
# TRA  - Text Render Attributes, use this to change the font style,
#        text colors etc. This comes in two forms, packed and unpacked.
#
# ============================== TRA UNPACKED =================================
# This is a more standard form, where the TRA tag has data
# in individual attributes. Those attributes are:
# -----------------------------------------------------------------------------
# AttrName  |                     Accepted Values
# -----------------------------------------------------------------------------
# COLOR     | fuchsia, gray, blue, green, aqua, red, yellow, white 
#           | OR #FFF, #FFFFFF hex colors
# -----------------------------------------------------------------------------
# BOLD      | TRUE, FALSE, DEFAULT
# -----------------------------------------------------------------------------
# ITALIC    | TRUE, FALSE, DEFAULT
# -----------------------------------------------------------------------------
# UNDERLINE | TRUE, FALSE, DEFAULT
# -----------------------------------------------------------------------------
# FONT      | Numeric font index
#           | Font index for both forms refers to the [TrueType]
#           | section in rich_fonts.ini. An example entry being:
#           |     [TrueType]
#           |     font = 0, Arial, 22
#           |     font = 1, Times New Roman, 35
# -----------------------------------------------------------------------------
# =========================== ADD FONTS IDS HERE ==============================
# Yes, they are strings.
allowed_font_ids = {
	"1" : '\\"1\\"',
#	"2" : '\\"2\\"',
#	"3" : '\\"3\\"',
}

# ============================ DO NOT EDIT BELOW ==============================
allowed_args = ["color", "bold", "italic", "underline", "font"]
allowed_options = {
	"true"    : '\\"true\\"',
	"false"   : '\\"false\\"',
	"default" : '\\"default\\"',
}
allowed_alignment = {
	"left"    : '\\"left\\"',
	"right"   : '\\"right\\"',
	"center"  : '\\"center\\"',
}
allowed_colors = {
	"green"   : '\\"green\\"',
	"fuchsia" : '\\"fuchsia\\"',
	"gray"    : '\\"gray\\"',
	"blue"    : '\\"blue\\"',
	"green"   : '\\"green\\"',
	"aqua"    : '\\"aqua\\"',
	"red"     : '\\"red\\"',
	"yellow"  : '\\"yellow\\"',
	"white"   : '\\"white\\"',
}

block_end = "/>"
infocard_start = "<?xml version=\\\"1.0\\\" encoding=\\\"UTF-16\\\"?><RDL><PUSH/>"
infocard_end = "<POP/></RDL>"
text_start = "<TEXT>"
text_end = "</TEXT>"
tra_start = "<TRA"
just_start = "<JUST loc="
divider = "------------------------"

class infocard():
	string = ""
	
	def __init__(self, *args):
		self.string += infocard_start
		for i in range(len(args)):
			self.string += args[i].string
		self.string += infocard_end
		#print(self.string)

class paragraph():
	string = "<PARA/>"

class alignment():
	string = ""
	
	def __init__(self, option):
		self.string += just_start + allowed_alignment[option] + block_end

class text():
	tras = ""
	string = ""
	
	def __init__(self, text, **kwargs):
		# Check for TRAs.
		if kwargs:
			self.tras += tra_start
			for key, value in kwargs.items():
				if key not in allowed_args:
					print("WRONG ATTRIBUTE at text block:", text)
					print("Attribute:", key)
					print("Value:", value)
					exit()
				if key == "color":
					self.tras += " " + key + "=" + allowed_colors[value]
				elif key == "bold":
					self.tras += " " + key + "=" + allowed_options[value]
				elif key == "italic":
					self.tras += " " + key + "=" + allowed_options[value]
				elif key == "underline":
					self.tras += " " + key + "=" + allowed_options[value]
				elif key == "font":
					self.tras += " " + key + "=" + allowed_font_ids[value]
			self.tras += block_end
		# If no TRAs passed, just proceed without it.
		self.string = self.tras + text_start + text + text_end

# ========================== EDIT INFOCARDS HERE ==============================
cards = [
infocard(
	alignment("center"),
	text("Lorem ipsum", color="blue", bold="true", font="1"),
	paragraph(),
	alignment("left"),
	text("sit amet"),
	),
	
infocard(
	alignment("center"),
	text("Lorem ipsum", color="blue", bold="true"),
	),
	
infocard(
	alignment("center"),
	text("sit amet", color="white", bold="false"),
	),
]

# =========================== CODE FOR PRINTING ===============================
for i in range(len(cards)):
	print(divider)
	print("Infocard", i+1, ":")
	print(cards[i].string)
	print()
	
#TODO: .json writer
