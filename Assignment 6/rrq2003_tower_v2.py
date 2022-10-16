"""This program makes a BMP file with a tower using specified colors


Template prepared by Mauricio Arias, ma6918
Submitted by Reyhan Quayum, rrq2003
"""


import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_bitmap.bmp"
picture_file = open(filename, 'wb')

# TODO 1: request the size information for the image
# Size information for the image: width and subunit height.
subunit_height = int(input("Give a single height for each of the rows (for example 100)"))
size_width = int(input("Give a value for the width of the tower (for example 200)"))
total_height = 10 * subunit_height

# Header with information about the size of the file.
image_binary = bmp.header(size_width, total_height, colors.bytes_per_pix)

# The number of levels is specified in this section
# TODO 2: write the code to fill the data section in the space below.
# Pixel by pixel color information starting from the bottom up and left
# to right. All rows are padded to a multiple of 4. For each pixel,
# colors are specified as follows: Blue channel, Green channel & then
# Red channel. Use ones available in the colors_BMP module.
# The number of bytes in each line has to be a multiple of 4. For
# padding, a special pad_byte is used.  The formula below is one of
# several possibilities.
padding = bmp.pad_byte * (- colors.bytes_per_pix * size_width % 4)
subunit_colors = [colors.light_cyan_pix, colors.salmon_pix, colors.dark_red_pix, colors.medium_violet_red_pix,
                  colors.dim_gray_pix, colors.alice_blue_pix, colors.forest_green_pix, colors.midnight_blue_pix,
                  colors.violet_pix, colors.dark_red_pix]
for color in subunit_colors:
    image_binary = image_binary + subunit_height * (color * size_width + padding)






# Do not edit after this point
picture_file.write(image_binary)
picture_file.close()