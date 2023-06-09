WIDTH = 1280
HEIGHT = 780
CENTER = WIDTH / 2, HEIGHT / 2
FPS = 200

MIN_DECIBEL = -80
MAX_DECIBEL = 80

BASS = {"start": 50, "stop": 100, "count": 12}
HEAVY_AREA = {"start": 120, "stop": 250, "count": 40}
LOW_MIDS = {"start": 251, "stop": 2000, "count": 50}
HIGH_MIDS = {"start": 2001, "stop": 6000, "count": 20}

SPACE = 4
BAR_WIDTH = 12
BAR_MAX_HEIGHT = 250
BAR_HEIGHT = (HEIGHT / 2) - (BAR_MAX_HEIGHT / 2) + 30
LINE_WIDTH = 3

DEFAULT_COLOR = (222, 232, 214)
DEFAULT_COLOR_PINK = (229, 207, 215)
DEFAULT_COLOR_BLUE = (164, 178, 216)

GRAY = 170
DEFAULT_COLOR_GRAY = (GRAY, GRAY, GRAY)

DEFAULT_COLOR_SELECT = (71, 79, 77)

BAR_START = 570

X_START = BAR_START - 30
X_END = BAR_START + (BAR_WIDTH + SPACE) * 32 + 30 - SPACE
Y_START = Y_END = BAR_HEIGHT + BAR_MAX_HEIGHT + 20
LENGTH = X_END - X_START

PLAYBACK_BAR_MARGIN_TOP = 70

PLAYBACK_BAR_Y = Y_START + PLAYBACK_BAR_MARGIN_TOP

BAR_CIRCLE_SIZE = 14
BAR_CIRCLE_RADIUS = BAR_CIRCLE_SIZE / 2

SOUND_BAR_X_END = X_END
SOUND_BAR_LENGTH = 130
SOUND_BAR_X_START = SOUND_BAR_X_END - SOUND_BAR_LENGTH
SOUND_BAR_Y = Y_START + PLAYBACK_BAR_MARGIN_TOP / 2

DEFAULT_PLAYER_SETTING = {}

SEARCH_SURFACE_HEIGHT = 700
SEARCH_SURFACE_WIDTH = 950
SEARCH_SURFACE_X = (WIDTH / 2) - (SEARCH_SURFACE_WIDTH / 2)
SEARCH_SURFACE_Y = (HEIGHT / 2) - (SEARCH_SURFACE_HEIGHT / 2)

SEARCH_BAR_WIDTH = 620
SEARCH_BAR_HEIGHT = 85
SEARCH_BAR_CENTER = WIDTH / 2, HEIGHT / 2 - 130

SONG_NAME_Y = Y_START + PLAYBACK_BAR_MARGIN_TOP + 40

WORKING_LENGTH = 1500  # 1500 for 25:00
SHORT_BREAK_LENGTH = 300  # 300 for 5:00
LONG_BREAK_LENGTH = 900  # 900 for long break

TIME_LENGTH = {0: WORKING_LENGTH, 1: SHORT_BREAK_LENGTH, 2: LONG_BREAK_LENGTH}
TIMER_COLOR = {0: DEFAULT_COLOR, 1: DEFAULT_COLOR_PINK, 2: DEFAULT_COLOR_BLUE}
