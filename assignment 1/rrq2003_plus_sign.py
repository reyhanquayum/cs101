"""This program makes a BMP file with a plus sign of a specified color"""


import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_other_bitmap.bmp"
picture_file = open(filename,'wb')

size_thickness = 50 # Thickness for the lines in the actual plus sign
#Size information for the image
size_width = 550
size_height = 1000


# Header with information about the size of the file.
image_binary = bmp.header(size_width, size_height, colors.bytes_per_pix)

# ToDo: write the code to fill the data section in the space below

# Pixel by pixel color information starting from the bottom up and left
# to right. All rows are padded to a multiple of 4. For each pixel, colors
# are specified as follows: Blue channel, Green channel & then Red channel.
# The number of bytes in each line has to a multiple of 4. For padding,
# a special pad_byte is used.

image_binary = image_binary + (size_height//2 - size_thickness//2)*(colors.papaya_pix * ((size_width - size_thickness)//2) + colors.dark_red_pix * size_thickness + colors.papaya_pix * ((size_width - size_thickness)//2) + 2*bmp.pad_byte)
image_binary = image_binary + size_thickness*(colors.dark_red_pix*size_width + 2*bmp.pad_byte)
image_binary = image_binary + (size_height//2 - size_thickness//2)*(colors.papaya_pix * ((size_width - size_thickness)//2) + colors.dark_red_pix * size_thickness + colors.papaya_pix * ((size_width - size_thickness)//2) + 2*bmp.pad_byte)











# Do not edit after this point
picture_file.write(image_binary)
picture_file.close()

