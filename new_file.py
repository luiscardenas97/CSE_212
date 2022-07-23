
from tkinter import *
from PIL import ImageTk, Image

photo_viewer = Tk()
photo_viewer.title("Photo Viewer")

picture_display = ImageTk.PhotoImage(Image.open("CSE_212/fox.jpg"))

picture_label = Label(image=picture_display)
picture_label.pack()

exit_button = Button(photo_viewer, text="Exit", command=photo_viewer.quit)
exit_button.pack()

photo_viewer.mainloop()