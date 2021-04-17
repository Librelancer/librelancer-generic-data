# This is not meant to be called directly, see "build_data.py" in root directory
if __name__ != '__main__':
	import _python_modules.common as c
	from _python_modules.common import nl, eq, space # for printing
	
	def make():
		global c
		# TODO
		c.navmap_ini_out = """
; Navmap configuration file
; Note: This file only works for Librelancer

; Use this section to load files required
[LibraryFiles]
file = INTERFACE/NAVMAP/navmap.txm

; Type of the icons
; Freelancer uses .3db files by default, we set to texture to use textures from our txm
; .3db, .txm
[IconType]
Type = texture

; Icons
; key = value
; nav_depot is required as that is the default icon we use
[Icons]
nav_depot = ICON_nav_depot

; Background
; This must always be a texture
; The texture should contain an 8x8 grid for the map grid to work properly
[Background]
texture = NAV_navmapbkgd
"""

