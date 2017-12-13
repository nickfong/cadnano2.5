from PyQt5.QtGui import QFont
from cadnano.gui.views.styles import BLUE_STROKE, GRAY_STROKE, THE_FONT

# Slice Sizing
SLICE_HELIX_RADIUS = 15.
SLICE_HELIX_STROKE_WIDTH = 0.5
SLICE_HELIX_MOD_HILIGHT_WIDTH = 1
EMPTY_HELIX_STROKE_WIDTH = 0.25

# Z values
# bottom
ZSLICEHELIX = 40
ZSELECTION = 50
ZDESELECTOR = 60
ZWEDGEGIZMO = 100
ZPXIGROUP = 150
ZPARTITEM = 200
# top

# Part appearance
SLICE_FILL = "#f6f6f6"

DEFAULT_PEN_WIDTH = 0  # cosmetic
DEFAULT_ALPHA = 2
SELECTED_COLOR = '#ff0000'  # '#5a8bff'
SELECTED_PEN_WIDTH = 0  # cosmetic
SELECTED_ALPHA = 0


SLICE_NUM_FONT = QFont(THE_FONT, 10, QFont.Bold)
USE_TEXT_COLOR = "#ffffff"
SLICE_TEXT_COLOR = "#000000"

ACTIVE_STROKE = '#cccc00'
ACTIVE_GRID_DOT_COLOR = BLUE_STROKE
DEFAULT_GRID_DOT_COLOR = BLUE_STROKE

MULTI_VHI_HINT_COLOR = '#bfdfff'
SPA_START_HINT_COLOR = '#666666'

VHI_HINT_ACTIVE_STROKE = BLUE_STROKE
VHI_HINT_INACTIVE_STROKE = '#cccccc'

DOT_SIZE = 30
