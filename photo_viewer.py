
from tkinter import *
from PIL import ImageTk, Image


class PhotoViewer:
    class Picture:
        def __init__(self, picture_name):
            self.picture_name = picture_name
            self.next_picture = None
            self.prev_picture = None
          
        
    def __init__(self):
        self.first_picture = None
        self.last_picture = None
    
    def add_picture_at_front(self, picture_name):
        new_picture = PhotoViewer.Picture(picture_name)

        if self.first_picture == None:
            self.first_picture = new_picture
            self.last_picture = new_picture
        
        else:
            self.first_picture.prev_picture = new_picture
            new_picture.next_picture = self.first_picture
            self.first_picture = new_picture

    def add_picture_at_end(self, picture_name):
        new_picture = PhotoViewer.Picture(picture_name)

        if self.first_picture == None:
            self.first_picture = new_picture
            self.last_picture = new_picture

        else:
            self.last_picture.next_picture = new_picture
            new_picture.prev_picture = self.last_picture
            self.last_picture = new_picture

    def add_picture_after(self, add_after, picture_name):
        current_picture = self.first_picture
        while current_picture is not None:
            if current_picture.picture_name == add_after:
                if current_picture.picture_name == self.last_picture.picture_name:
                    self.add_picture_at_end(picture_name)
                else:
                    new_picture = PhotoViewer.Picture(picture_name)
                    new_picture.prev_picture = current_picture
                    new_picture.next_picture = current_picture.next_picture
                    current_picture.next_picture.prev_picture = new_picture
                    current_picture.next_picture = new_picture
            current_picture = current_picture.next_picture
    
    def delete_picture_at_front(self):
        if self.first_picture == self.last_picture:
            self.first_picture = None
            self.last_picture = None
        
        elif self.first_picture is not None:
            self.first_picture.next_picture.prev_picture = None
            self.first_picture = self.first_picture.next_picture

    def delete_picture_at_end(self):
        if self.first_picture == self.last_picture:
            self.first_picture = None
            self.last_picture = None
        elif self.last_picture is not None:
            self.last_picture.prev_picture.next_picture = None
            self.last_picture = self.last_picture.prev_picture

    def delete_picture_in_middle(self, picture_name):
        current_picture = self.first_picture
        while current_picture is not None:
            if current_picture.picture_name == picture_name:
                if current_picture.picture_name == self.first_picture.picture_name:
                    self.delete_picture_at_front()
                elif current_picture.picture_name == self.last_picture.picture_name:
                    self.delete_picture_at_end()
                elif current_picture.picture_name != self.first_picture.picture_name:
                    current_picture.next_picture.prev_picture = current_picture.prev_picture
                    current_picture.prev_picture.next_picture = current_picture.next_picture
                return
            current_picture = current_picture.next_picture
        if current_picture == None:
            print("We're sorry but you delete the picture. The list is empty")

    def __iter__(self):
        current_picture  = self.first_picture
        while current_picture is not None:
            yield current_picture.picture_name
            current_picture = current_picture.next_picture

    def replace(self, old_picture, replacement_picture):
        current_picture = self.first_picture
        while current_picture is not None:
            if current_picture.picture_name == old_picture:
                if current_picture.picture_name == self.first_picture.picture_name:
                    self.delete_picture_at_front()
                    self.add_picture_at_front(replacement_picture)
                elif current_picture.picture_name == self.last_picture.picture_name:
                    self.delete_picture_at_end()
                    self.add_picture_at_end(replacement_picture)
                else:
                    add_after = current_picture.prev_picture
                    self.delete_picture_in_middle(current_picture.picture_name)
                    self.add_picture_after(add_after.picture_name, replacement_picture)
                return  
            current_picture = current_picture.next_picture  

    def is_in_list(self, picture_name):
        current_picture = self.first_picture
        while current_picture is not None:
            if current_picture.picture_name == picture_name:
                return True
            current_picture = current_picture.next_picture
        return False

    def display_photo_viewer(self):

        current_picture = self.first_picture
        while current_picture is not None:
            photo_viewer = Tk()
            photo_viewer.title("Photo Viewer")

            picture_display = ImageTk.PhotoImage(Image.open(f"CSE_212/{current_picture.picture_name}.jpg"))

            picture_label = Label(image=picture_display)
            picture_label.pack()

            next_button = Button(photo_viewer, text="Next Picture →", command=photo_viewer.destroy).pack()
            
            photo_viewer.mainloop()
            current_picture = current_picture.next_picture

        else:
            print("Sorry, the list of picture is empty. There is nothing to display.")



photos_list = PhotoViewer()

exit_menu = "no"

while exit_menu == "no":
    request = 1
    print("Photo Viewer Menu: ")
    print("1) Add picture at beginning or end of the list")
    print("2) Add picture after an specific picture")
    print("3) Delete picture from list")
    print('4) Replace picture by another picture')
    print("5) Display picture in the Photo Viewer")
    print("6) Exit")
    operation = int(input("\nSelect operation: "))

    if operation == 1:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to add to the list: ")
            picture_name_format = picture_name.lower()
            if photos_list.is_in_list(picture_name_format):
                print("\nPicture is already in the list. Please add another picture.")
            else:
                order = int(input("\nDo you want to add pictures at the beginning or end of the list (Enter 1 for beginning or 0 for end)? "))
        
                if order == 1:
                    photos_list.add_picture_at_front(picture_name_format)
                else:
                    photos_list.add_picture_at_end(picture_name_format)
            
                request = int(input("\nDo you want to add another picture at the beginning or end of the list? (Enter 1 for yes and 0 for no): "))

    elif operation == 2:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to add to the list: ")
            picture_name_format = picture_name.lower()
            if photos_list.is_in_list(picture_name_format):
                print("\nPicture is already in the list. Please add another picture.")
            else:
                previous_picture = input("\nPlease introduce the name of the picture after which you want to add the picture: ")
                previous_picture_format = previous_picture.lower()
                photos_list.add_picture_after(previous_picture_format, picture_name_format)

                request = int(input("\nDo you want to add another picture at the middle of the list? (Enter 1 for yes and 0 for no): "))

    elif operation == 3:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to delete from the list: ")
            picture_name_format = picture_name.lower()
            photos_list.delete_picture_in_middle(picture_name_format)

            request = int(input("\nDo you want to delete another picture from the list? (Enter 1 for yes and 0 for no): "))
    
    elif operation == 4:
        while request == 1:
            
            replacement_picture = input("\nPlease introduce the name of new picture that will replace an old picture: ")
            replacement_picture_format = replacement_picture.lower()

            if photos_list.is_in_list(replacement_picture_format):
                print("\nPicture is already in the list. Please add another picture.")
            else:
                replaced_picture = input("\nPlease introduce the name of the picture you want to replace from the list: ")
                replaced_picture_format = replaced_picture.lower()
                photos_list.replace(replaced_picture_format, replacement_picture_format)

                request = int(input("\nDo you want to replace another picture from the list? (Enter 1 for yes and 0 for no): "))
    
    elif operation == 5:
        photos_list.display_photo_viewer()

    elif operation == 6:
        exit_menu = "yes"
    
    print()


