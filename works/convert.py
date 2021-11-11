# convert.py

def convert(filenames)

    # import module
    from pdf2image import convert_from_path
     
    for filename in filenames
    # Store Pdf with convert_from_path function
    images = convert_from_path(filename,poppler_path = 'C:/Users/zegla/Documents/Python/poppler-21.10.0/Library/bin')
    images[1].save(filename + '.jpg', 'JPEG')
