# Compile new gallery input
from bs4 import BeautifulSoup as bs
import os
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import ImageTk, Image


def open_picture():
    # Make gallery input html
    global filename
    filename = askopenfilename(initialdir="./images",
                               title="Select a File")
    # show an "Open" dialog box and return the path to the selected file
    # Create an object of tkinter ImageTk
    img = Image.open(filename)
    img = img.resize((400, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    can.delete('all')
    can.create_image(20, 20, anchor='nw', image=img)
    win.mainloop()


def add_gallery_input(filename):
    description = txt.get(1.0, "end-1c")
    local_filename = filename.split("/")[-1]
    # Open html to edit
    with open("index.html") as fp:
        soup = bs(fp, "html.parser")
    # Make tags and append to html
    gallery = soup.new_tag("div", **{'class': 'gallery'})
    link = soup.new_tag("a", href=local_filename, target="_blank")
    img = soup.new_tag("img", alt="", height="400", src=local_filename, width="600")
    desc = soup.new_tag("div", **{'class': 'desc'})
    desc.append(description)

    link.append(img)
    gallery.append(link)
    gallery.append(desc)
    content_tag = soup.find("div", {"class": "content"})
    content_tag.append(gallery)

    with open("index.html", "w") as outf:
        outf.write(str(soup.prettify()))
    os.rename('images/' + local_filename, local_filename)
    can.delete('all')
    can.create_text(200, 100, text="Gallery item \n appended to HTML", fill="black", font=('Helvetica 12 bold'))


def delete_gallery_input():
    global filename
    filename = askopenfilename(initialdir="./",
                               title="Select a File")
    local_filename = filename.split("/")[-1]
    with open("index.html") as fp:
        soup = bs(fp, "html.parser")
    divs = soup.findAll("div", {"class": "gallery"})
    images = soup.findAll('img')
    r=soup.find(src=local_filename)
    div2del = r.find_parent('div')
    div2del.decompose()
    with open("index.html", "w") as outf:
        outf.write(str(soup.prettify()))
    os.rename(local_filename, 'images/' + local_filename)
    can.delete('all')
    can.create_text(200, 100, text="Gallery item \n deleted from HTML", fill="black", font=('Helvetica 12 bold'))


def commit_changes():
    os.system('git pull')
    os.system('git commit')
    os.system('git push')


win = tk.Tk()  # creating the main window and storing the window object in 'win'
# We create the widgets here
win.title('Gallery input')  # setting title of the window
win.geometry("650x400")  # setting the size of the window

button_frame = tk.Frame(win)
button_frame.pack(side='left')
btn_choose_pic = tk.Button(button_frame, text="Choose \n picture", width=10, height=5, command=open_picture)
btn_choose_pic.pack(side='top')
btn_add_input = tk.Button(button_frame, text="Publish", width=10, height=5, command=lambda: add_gallery_input(filename))
btn_add_input.pack(side='top')
btn_del_input = tk.Button(button_frame, text="Delete", width=10, height=5, command=delete_gallery_input)
btn_del_input.pack(side='top')
btn_commit = tk.Button(button_frame, text="Save to Git", width=10, height=5, command=commit_changes)
btn_commit.pack(side='top')

display_frame = tk.Frame(win)
display_frame.pack(side='left')
can = tk.Canvas(display_frame, width=400, height=300)
can.pack(side='top')
txt = tk.Text(display_frame, height=5, width=45)
txt.pack(side='bottom')
txt.insert(tk.INSERT, "")

win.mainloop()  # running the loop that works as a trigger
