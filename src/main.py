from datetime import datetime
import piexif
import glob

# Set the format-flag number according to the following:
# 1. IMG_20141110_173728.jpg
# 2. Screenshot_2014-01-15-10-53-56.jpg
# 3. IMG-20131022-WA0003.jpg

format = 3

path = "C:/Users/Tobias/Desktop/Instagram"

for filename in glob.glob(path + '/*.jpg'): #assuming gif
    exif_dict = piexif.load(filename)
    match format:
        case 1:
            new_date = datetime(int(filename[-19:-15]), int(filename[-15:-13]), int(filename[-13:-11]), int(filename[-10:-8]), int(filename[-8:-6]), int(filename[-6:-4])).strftime("%Y:%m:%d %H:%M:%S")
        case 2:
            new_date = datetime(int(filename[-23:-19]), int(filename[-18:-16]), int(filename[-15:-13]), int(filename[-12:-10]), int(filename[-9:-7]), int(filename[-6:-4])).strftime("%Y:%m:%d %H:%M:%S")
        case 3:
            new_date = datetime(int(filename[-19:-15]), int(filename[-15:-13]), int(filename[-13:-11]), 12, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
        case _:
            continue

    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)