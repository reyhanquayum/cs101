"""This program makes a BMP file with a tower using specified colors"""


import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_bitmap.bmp"
picture_file = open(filename,'wb')

# Size information for the image
size_width = 251
size_height = 500

# Header with information about the size of the file.
image_binary = bmp.header(size_width, size_height, colors.bytes_per_pix)

# The number of levels is specified in this section
number_of_colors = 4
base_pix = colors.papaya_pix
mid_low_pix = colors.dark_orchid_pix
mid_high_pix = colors.salmon_pix
top_pix = colors.brown_pix

# ToDo: write the code to fill the data section in the space below


# Pixel by pixel color information starting from the bottom up and left
# to right. All rows are padded to a multiple of 4. For each pixel, colors
# are specified as follows: Blue channel, Green channel & then Red channel.
# The number of bytes in each line has to a multiple of 4. For padding,
# a special pad_byte is used.
image_binary = image_binary + (size_height//number_of_colors)*(colors.papaya_pix * size_width + bmp.pad_byte * 3)
image_binary = image_binary + (size_height//number_of_colors)*(colors.dark_orchid_pix * size_width + bmp.pad_byte * 3)
image_binary = image_binary + (size_height//number_of_colors)*(colors.salmon_pix * size_width + bmp.pad_byte * 3)
image_binary = image_binary + (size_height//number_of_colors)*(colors.brown_pix * size_width + bmp.pad_byte * 3)






# Do not edit after this point
picture_file.write(image_binary)
picture_file.close()