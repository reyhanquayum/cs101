"""Color definitions for bitmaps using byte arrays


Notice that the colors are defined using 3 bytes and that the order is 
Blue Green Red.
"""

# Only the basic definition is implemented: Blue, Green and Red.
# In particular, no alpha channel information is used.
# Notice that the information is encoded as hexadecimal numbers starting with \x.
# For example 255 is \xff and 0 is \x00. The three numbers are specified separately
# for clarity.
bytes_per_pix = 3

dark_red_pix = bytearray(b'\x00\x00\x8b')
brown_pix = bytearray(b'\x2a\x2a\xa5')
firebrick_pix = bytearray(b'\x22\x22\xb2')
crimson_pix = bytearray(b'\x3c\x14\xdc')
red_pix = bytearray(b'\x00\x00\xff')
tomato_pix = bytearray(b'\x47\x63\xff')
coral_pix = bytearray(b'\x50\x7f\xff')
indian_red_pix = bytearray(b'\x5c\x5c\xcd')
light_coral_pix = bytearray(b'\x80\x80\xf0')
dark_salmon_pix = bytearray(b'\x7a\x96\xe9')
salmon_pix = bytearray(b'\x72\x80\xfa')
light_salmon_pix = bytearray(b'\x7a\xa0\xff')
orange_red_pix = bytearray(b'\x00\x45\xff')
dark_orange_pix = bytearray(b'\x00\x8c\xff')
orange_pix = bytearray(b'\x00\xa5\xff')
gold_pix = bytearray(b'\x00\xd7\xff')
dark_golden_rod_pix = bytearray(b'\x0b\x86\xb8')
papaya_pix = bytearray(b'\x78\xc4\xf8')
lilac_pix = bytearray(b'\xf8\x78\xb6')
golden_rod_pix = bytearray(b'\x20\xa5\xda')
pale_golden_rod_pix = bytearray(b'\xaa\xe8\xee')
dark_khaki_pix = bytearray(b'\x6b\xb7\xbd')
khaki_pix = bytearray(b'\x8c\xe6\xf0')
olive_pix = bytearray(b'\x00\x80\x80')
yellow_pix = bytearray(b'\x00\xff\xff')
yellow_green_pix = bytearray(b'\x32\xcd\x9a')
dark_olive_green_pix = bytearray(b'\x2f\x6b\x55')
olive_drab_pix = bytearray(b'\x23\x8e\x6b')
lawn_green_pix = bytearray(b'\x00\xfc\x7c')
chart_reuse_pix = bytearray(b'\x00\xff\x7f')
green_yellow_pix = bytearray(b'\x2f\xff\xad')
dark_green_pix = bytearray(b'\x00\x64\x00')
green_pix = bytearray(b'\x00\x80\x00')
forest_green_pix = bytearray(b'\x22\x8b\x22')
lime_pix = bytearray(b'\x00\xff\x00')
lime_green_pix = bytearray(b'\x32\xcd\x32')
light_green_pix = bytearray(b'\x90\xee\x90')
pale_green_pix = bytearray(b'\x98\xfb\x98')
dark_sea_green_pix = bytearray(b'\x8f\xbc\x8f')
medium_spring_green_pix = bytearray(b'\x9a\xfa\x00')
spring_green_pix = bytearray(b'\x7f\xff\x00')
sea_green_pix = bytearray(b'\x57\x8b\x2e')
medium_aqua_marine_pix = bytearray(b'\xaa\xcd\x66')
medium_sea_green_pix = bytearray(b'\x71\xb3\x3c')
light_sea_green_pix = bytearray(b'\xaa\xb2\x20')
dark_slate_gray_pix = bytearray(b'\x4f\x4f\x2f')
teal_pix = bytearray(b'\x80\x80\x00')
dark_cyan_pix = bytearray(b'\x8b\x8b\x00')
aqua_pix = bytearray(b'\xff\xff\x00')
cyan_pix = bytearray(b'\xff\xff\x00')
light_cyan_pix = bytearray(b'\xff\xff\xe0')
dark_turquoise_pix = bytearray(b'\xd1\xce\x00')
turquoise_pix = bytearray(b'\xd0\xe0\x40')
medium_turquoise_pix = bytearray(b'\xcc\xd1\x48')
pale_turquoise_pix = bytearray(b'\xee\xee\xaf')
aqua_marine_pix = bytearray(b'\xd4\xff\x7f')
powder_blue_pix = bytearray(b'\xe6\xe0\xb0')
cadet_blue_pix = bytearray(b'\xa0\x9e\x5f')
steel_blue_pix = bytearray(b'\xb4\x82\x46')
corn_flower_blue_pix = bytearray(b'\xed\x95\x64')
deep_sky_blue_pix = bytearray(b'\xff\xbf\x00')
dodger_blue_pix = bytearray(b'\xff\x90\x1e')
light_blue_pix = bytearray(b'\xe6\xd8\xad')
sky_blue_pix = bytearray(b'\xeb\xce\x87')
light_sky_blue_pix = bytearray(b'\xfa\xce\x87')
midnight_blue_pix = bytearray(b'\x70\x19\x19')
navy_pix = bytearray(b'\x80\x00\x00')
dark_blue_pix = bytearray(b'\x8b\x00\x00')
medium_blue_pix = bytearray(b'\xcd\x00\x00')
blue_pix = bytearray(b'\xff\x00\x00')
royal_blue_pix = bytearray(b'\xe1\x69\x41')
blue_violet_pix = bytearray(b'\xe2\x2b\x8a')
indigo_pix = bytearray(b'\x82\x00\x4b')
dark_slate_blue_pix = bytearray(b'\x8b\x3d\x48')
slate_blue_pix = bytearray(b'\xcd\x5a\x6a')
medium_slate_blue_pix = bytearray(b'\xee\x68\x7b')
medium_purple_pix = bytearray(b'\xdb\x70\x93')
dark_magenta_pix = bytearray(b'\x8b\x00\x8b')
dark_violet_pix = bytearray(b'\xd3\x00\x94')
dark_orchid_pix = bytearray(b'\xcc\x32\x99')
medium_orchid_pix = bytearray(b'\xd3\x55\xba')
purple_pix = bytearray(b'\x80\x00\x80')
thistle_pix = bytearray(b'\xd8\xbf\xd8')
plum_pix = bytearray(b'\xdd\xa0\xdd')
violet_pix = bytearray(b'\xee\x82\xee')
fuchsia_pix = bytearray(b'\xff\x00\xff')
magenta_pix = bytearray(b'\xff\x00\xff')
orchid_pix = bytearray(b'\xd6\x70\xda')
medium_violet_red_pix = bytearray(b'\x85\x15\xc7')
pale_violet_red_pix = bytearray(b'\x93\x70\xdb')
deep_pink_pix = bytearray(b'\x93\x14\xff')
hot_pink_pix = bytearray(b'\xb4\x69\xff')
light_pink_pix = bytearray(b'\xc1\xb6\xff')
pink_pix = bytearray(b'\xcb\xc0\xff')
antique_white_pix = bytearray(b'\xd7\xeb\xfa')
beige_pix = bytearray(b'\xdc\xf5\xf5')
bisque_pix = bytearray(b'\xc4\xe4\xff')
blanched_almond_pix = bytearray(b'\xcd\xeb\xff')
wheat_pix = bytearray(b'\xb3\xde\xf5')
corn_silk_pix = bytearray(b'\xdc\xf8\xff')
lemon_chiffon_pix = bytearray(b'\xcd\xfa\xff')
light_golden_rod_yellow_pix = bytearray(b'\xd2\xfa\xfa')
light_yellow_pix = bytearray(b'\xe0\xff\xff')
saddle_brown_pix = bytearray(b'\x13\x45\x8b')
sienna_pix = bytearray(b'\x2d\x52\xa0')
chocolate_pix = bytearray(b'\x1e\x69\xd2')
peru_pix = bytearray(b'\x3f\x85\xcd')
sandy_brown_pix = bytearray(b'\x60\xa4\xf4')
burly_wood_pix = bytearray(b'\x87\xb8\xde')
tan_pix = bytearray(b'\x8c\xb4\xd2')
rosy_brown_pix = bytearray(b'\x8f\x8f\xbc')
moccasin_pix = bytearray(b'\xb5\xe4\xff')
navajo_white_pix = bytearray(b'\xad\xde\xff')
peach_puff_pix = bytearray(b'\xb9\xda\xff')
misty_rose_pix = bytearray(b'\xe1\xe4\xff')
lavender_blush_pix = bytearray(b'\xf5\xf0\xff')
linen_pix = bytearray(b'\xe6\xf0\xfa')
old_lace_pix = bytearray(b'\xe6\xf5\xfd')
papaya_whip_pix = bytearray(b'\xd5\xef\xff')
sea_shell_pix = bytearray(b'\xee\xf5\xff')
mint_cream_pix = bytearray(b'\xfa\xff\xf5')
slate_gray_pix = bytearray(b'\x90\x80\x70')
light_slate_gray_pix = bytearray(b'\x99\x88\x77')
light_steel_blue_pix = bytearray(b'\xde\xc4\xb0')
lavender_pix = bytearray(b'\xfa\xe6\xe6')
floral_white_pix = bytearray(b'\xf0\xfa\xff')
alice_blue_pix = bytearray(b'\xff\xf8\xf0')
ghost_white_pix = bytearray(b'\xff\xf8\xf8')
honeydew_pix = bytearray(b'\xf0\xff\xf0')
ivory_pix = bytearray(b'\xf0\xff\xff')
azure_pix = bytearray(b'\xff\xff\xf0')
snow_pix = bytearray(b'\xfa\xfa\xff')
black_pix = bytearray(b'\x00\x00\x00')
dim_grey_pix = bytearray(b'\x69\x69\x69')
dim_gray_pix = bytearray(b'\x69\x69\x69')
grey_pix = bytearray(b'\x80\x80\x80')
gray_pix = bytearray(b'\x80\x80\x80')
dark_grey_pix = bytearray(b'\xa9\xa9\xa9')
dark_gray_pix = bytearray(b'\xa9\xa9\xa9')
silver_pix = bytearray(b'\xc0\xc0\xc0')
light_grey_pix = bytearray(b'\xd3\xd3\xd3')
light_gray_pix = bytearray(b'\xd3\xd3\xd3')
gainsboro_pix = bytearray(b'\xdc\xdc\xdc')
white_smoke_pix = bytearray(b'\xf5\xf5\xf5')
white_pix = bytearray(b'\xff\xff\xff')