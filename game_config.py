import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSET_DIR = "assets"
ASSET_FILES = [f for f in os.listdir(ASSET_DIR) if f[-3:].lower() == "png"]


assert len(ASSET_FILES) == 8