import exifread
# Open image file for reading (binary mode)
f = open("C:\\GitHub\\Images\\myCDKview.jpg", 'rb')

# Return Exif tags
tags = exifread.process_file(f)

print(tags)