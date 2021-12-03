# Append new report
from bs4 import BeautifulSoup as bs
import os

def app_gallery(filename):
    # Make gallery input html
    gallery_input = """<div class="gallery"><a target="_blank" href=" """ + filename + """ "><img src=" """+ filename +""" " alt="" width="600" height="400"></a></div>"""

    # Open html to edit
    with open("index.html") as fp:
        soup = bs(fp, "html.parser")
    # Make tag and append to html
    gallery = soup.new_tag("div",**{'class':'gallery'})
    #gallery.string=""" class="gallery" """
    link = soup.new_tag("a",href=filename,target="_blank")
    #link.string=""" href= " """ +filename+ """ " target="_blank" """
    img = soup.new_tag("img",alt="", height="400", src=filename.split('.pdf')[0] + ".jpg", width="600")
    #img.string=""" alt="" height="400" src=" """+filename+""" " width="600" """
    
    link.append(img)
    gallery.append(link)
    
    content_tag = soup.find("div", {"class": "content"})
    content_tag.append(gallery)
    
    with open("index.html", "w") as outf:
        outf.write(str(soup))

def convert(filename):
    # import module
    from pdf2image import convert_from_path
    # Store Pdf with convert_from_path function
    images = convert_from_path('non_converted/' + filename,poppler_path = 'C:/Users/zegla/Documents/Python/poppler-21.10.0/Library/bin')
    images[0].save(filename.split('.pdf')[0] + '.jpg', 'JPEG')

filenames = os.listdir("non_converted")

for filename in filenames:
    app_gallery(filename)
    convert(filename)
    os.rename('non_converted/' + filename, filename)
