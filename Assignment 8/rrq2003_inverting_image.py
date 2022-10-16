"""Retrieves the size of a bmp image and crops the image
This script reads a bmp file and retrieves the size information and other
details. It then crops the image so that only the center is visible.

Submitted by Reyhan Quayum, rrq2003
"""
def retrieve_int(file_handle, num_bytes):
    num_bytes = bytearray(file_handle.read(num_bytes))
    num_bytes.reverse()
    num_int = 0
    for byte in num_bytes:
        num_int = num_int * 256 + byte
    return num_int

try:
    bmp_filename = input("Name of bmp file")
    bmp_file = open(bmp_filename, "br")
except FileNotFoundError:
    print("That filename was not found")
else:
    descriptor = bmp_file.read(2)
    file_size = retrieve_int(bmp_file, 4)
    unused_bytes = retrieve_int(bmp_file, 4)
    offset = retrieve_int(bmp_file, 4)
    header_size = retrieve_int(bmp_file, 4)
    image_width = retrieve_int(bmp_file, 4)
    image_height = retrieve_int(bmp_file, 4)
    color_planes = retrieve_int(bmp_file, 4)
    bits_per_pixel = retrieve_int(bmp_file, 2)
    bytes_per_pixel = bits_per_pixel // 8

    bmp_file.seek(0)

    header = bmp_file.read(offset)
    print(header)

    padding = -image_width * (bytes_per_pixel) % 4
    print(padding)

    initial_list = []
    for i in range(image_height):
        list2 = []
        for x in range(image_width):
            list2.append(bmp_file.read(bytes_per_pixel))
        initial_list.append(list2)
        if padding > 0:
            bmp_file.read(padding)

    inverted_filename = "inverted " + bmp_filename
    inverted_file = open(inverted_filename, 'bw')

    inverted_file.write(header)
    for i in range(image_height):
        for j in range(image_width):
            inverted_file.write(initial_list[-i][-j])
        if padding > 0:
            inverted_file.write(b'\x00' * padding)
    inverted_file.close()
    bmp_file.close()
