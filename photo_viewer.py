
# Import a standard Python interface with GUI(Graphical User Interface)
from tkinter import *
# Import Python private library that allows to add images to GUI
# In order to be able to use this library, you need to install it by typing 'pip install Pillow' on the terminal
from PIL import ImageTk, Image

# Create a clas that contains a linked list with pictures
class PhotoViewer:
    # Create a class that contains each picture name as a node
    class Picture:
        def __init__(self, picture_name):
            self.picture_name = picture_name
            self.next_picture = None
            self.prev_picture = None
          
    # Create a empty linked list
    def __init__(self):
        self.first_picture = None
        self.last_picture = None
    
    # Method that allows to add a new picture at the front of the list
    def add_picture_at_front(self, picture_name):
        new_picture = PhotoViewer.Picture(picture_name)
        # If list is empty, add new picture at the front of the list
        if self.first_picture == None:
            self.first_picture = new_picture
            self.last_picture = new_picture
        #Otherwise, replace old picture at the front of the list by the new picture
        else:
            self.first_picture.prev_picture = new_picture
            new_picture.next_picture = self.first_picture
            self.first_picture = new_picture

    # Method that allows to add a new picture at the end of the list
    def add_picture_at_end(self, picture_name):
        new_picture = PhotoViewer.Picture(picture_name)
        # If list is empty, add new picture at the front of the list
        if self.first_picture == None:
            self.first_picture = new_picture
            self.last_picture = new_picture
        #Otherwise, replace old picture at the end of the list by the new picture
        else:
            self.last_picture.next_picture = new_picture
            new_picture.prev_picture = self.last_picture
            self.last_picture = new_picture

    # Method that allows to add a new picture after another specific old picture
    def add_picture_after(self, add_after, picture_name):
        # Loop through the list, starting at the first picture
        current_picture = self.first_picture
        # Keep looping as longh as the current picture exists
        while current_picture is not None:
            # Check if current picture is equal to the old picture. If it's, add new picture after this old picture
            if current_picture.picture_name == add_after:
                # Check if current picture is equal to the last picture in the list
                if current_picture.picture_name == self.last_picture.picture_name:
                    self.add_picture_at_end(picture_name)   # Add new picture at the end of the list
                # Otherwise, add new picture after the old picture
                else:
                    new_picture = PhotoViewer.Picture(picture_name)
                    new_picture.prev_picture = current_picture
                    new_picture.next_picture = current_picture.next_picture
                    current_picture.next_picture.prev_picture = new_picture
                    current_picture.next_picture = new_picture
            
            # Go to next picture
            current_picture = current_picture.next_picture
    
    # Method that allows to delete a picture from the linked list at the front of the list
    def delete_picture_at_front(self):
        # If linked list only have one picture, delete this picture
        if self.first_picture == self.last_picture:
            self.first_picture = None
            self.last_picture = None
        # If linked list is not empty, delete picture at the front of the list
        elif self.first_picture is not None:
            self.first_picture.next_picture.prev_picture = None
            self.first_picture = self.first_picture.next_picture

    # Method that allows to delete a picture from the linked list at the end of the list
    def delete_picture_at_end(self):
        # If linked list only have one picture, delete this picture
        if self.first_picture == self.last_picture:
            self.first_picture = None
            self.last_picture = None
        # If last picture at the end of the linked list exits, delete this picture
        elif self.last_picture is not None:
            self.last_picture.prev_picture.next_picture = None
            self.last_picture = self.last_picture.prev_picture

    # Method that allows to delete a picture from the linked list at any place in the list or middle
    def delete_picture_in_middle(self, picture_name):
        # Loop through the list, starting at the first picture
        current_picture = self.first_picture
        # Keep looping as longh as the current picture exists
        while current_picture is not None:
            # Check if current picture is equal to the picture is supposed to be deleted. If it's, delete this picture
            if current_picture.picture_name == picture_name:
                # Check if picture is at the front of the list. If it's, delete this picture
                if current_picture.picture_name == self.first_picture.picture_name:
                    self.delete_picture_at_front()
                # Check if picture is at the end of the list. If it's, delete this picture    
                elif current_picture.picture_name == self.last_picture.picture_name:
                    self.delete_picture_at_end()
                # If current picture is different than the first picture, delete this picture
                elif current_picture.picture_name != self.first_picture.picture_name:
                    current_picture.next_picture.prev_picture = current_picture.prev_picture
                    current_picture.prev_picture.next_picture = current_picture.next_picture
                return
            # Go to next picture
            current_picture = current_picture.next_picture
        # If linked list is empty, print this message
        if current_picture == None:
            print("We're sorry but you can't delete the picture. The list is empty")

    # Method that allows to iterate through the linked list. Allow the user to use 'for' loop
    def __iter__(self):
        # Starting from the first student in the linked list, iterate through each picture in the list
        current_picture  = self.first_picture
        # As long as the end of the list is not reached, keep looping
        while current_picture is not None:
            # Return the name of the current picture
            yield current_picture.picture_name
            # Go to next picture
            current_picture = current_picture.next_picture

    # Method that allows to replace an old picture by a new picture
    def replace(self, old_picture, replacement_picture):
        # Loop through the list, starting at the first picture
        current_picture = self.first_picture
        # Keep looping as longh as the current picture exists
        while current_picture is not None:
            # Check if current picture is equal to the old picture. If it's, replace this old picture by new picture
            if current_picture.picture_name == old_picture:
                # Check if old picture is at the front of the list. If it's, replaced this olde picture by new picture
                if current_picture.picture_name == self.first_picture.picture_name:
                    self.delete_picture_at_front()
                    self.add_picture_at_front(replacement_picture)
                # Check if old picture is at the end of the list. If it's, replaced this olde picture by new picture
                elif current_picture.picture_name == self.last_picture.picture_name:
                    self.delete_picture_at_end()
                    self.add_picture_at_end(replacement_picture)
                # Otherwise, replace the old picture (wherever this is) by new picture
                else:
                    add_after = current_picture.prev_picture
                    self.delete_picture_in_middle(current_picture.picture_name)
                    self.add_picture_after(add_after.picture_name, replacement_picture)
                return 
            # Go to next picture 
            current_picture = current_picture.next_picture  

    # Method that allows to check if a picture is already in the linked list. If it's, return True
    def is_in_list(self, picture_name):
        # Loop through the list, starting at the first picture
        current_picture = self.first_picture
        # Keep looping as longh as the current picture exists
        while current_picture is not None:
            # Check if the picture is already in the linked list
            if current_picture.picture_name == picture_name:
                return True
            # Go to next picture
            current_picture = current_picture.next_picture
        # If picture is not in the linked list, return False
        return False

    # Method that allows to display the picture on the screen
    def display_photo_viewer(self):
        # Loop through the list, starting at the first picture
        current_picture = self.first_picture
        # Keep looping as longh as the current picture exists
        while current_picture is not None:
            photo_viewer = Tk()                     # Create a window to display picture
            photo_viewer.title("Photo Viewer")      # Add title to the console
            # Select picture to display
            picture_display = ImageTk.PhotoImage(Image.open(f"CSE_212/{current_picture.picture_name}.jpg"))
            # Display box with selected picture
            picture_label = Label(image=picture_display)
            picture_label.pack()
            # Create a button to display next picture
            next_button = Button(photo_viewer, text="Next Picture →", command=photo_viewer.destroy).pack()
            # Infinte loop to display window
            photo_viewer.mainloop()
            # Go to next picture
            current_picture = current_picture.next_picture
        # If linked list is empty, display the message
        else:
            print("Sorry, the list of picture is empty. There is nothing to display.")


# Create a new picture list
photos_list = PhotoViewer()

exit_menu = "no"

# Create menu that allow user to perform different operations with the linked list
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

    # Add new picture at the beginning or end of the linked list
    if operation == 1:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to add to the list: ")
            picture_name_format = picture_name.lower()
            # Check if picture is already in the linked list. If it's, return message
            if photos_list.is_in_list(picture_name_format):
                print("\nPicture is already in the list. Please add another picture.")
            # Otherwise, add new picture
            else:
                order = int(input("\nDo you want to add pictures at the beginning or end of the list (Enter 1 for beginning or 0 for end)? "))
        
                if order == 1:
                    photos_list.add_picture_at_front(picture_name_format)
                else:
                    photos_list.add_picture_at_end(picture_name_format)
            
                request = int(input("\nDo you want to add another picture at the beginning or end of the list? (Enter 1 for yes and 0 for no): "))

    # Add new picture to the linked list after a specific old picture
    elif operation == 2:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to add to the list: ")
            picture_name_format = picture_name.lower()
            # Check if picture is already in the linked list. If it's, return message
            if photos_list.is_in_list(picture_name_format):
                print("\nPicture is already in the list. Please add another picture.")
            # Otherwise, add new picture
            else:
                previous_picture = input("\nPlease introduce the name of the picture after which you want to add the picture: ")
                previous_picture_format = previous_picture.lower()
                photos_list.add_picture_after(previous_picture_format, picture_name_format)

                request = int(input("\nDo you want to add another picture at the middle of the list? (Enter 1 for yes and 0 for no): "))

    # Delete picture from linked list
    elif operation == 3:
        while request == 1:
            picture_name = input("\nPlease introduce the name of the picture you want to delete from the list: ")
            picture_name_format = picture_name.lower()
            photos_list.delete_picture_in_middle(picture_name_format)

            request = int(input("\nDo you want to delete another picture from the list? (Enter 1 for yes and 0 for no): "))
    
    # Replace old picture in the linked list by a new picture
    elif operation == 4:
        while request == 1:
            
            replacement_picture = input("\nPlease introduce the name of new picture that will replace an old picture: ")
            replacement_picture_format = replacement_picture.lower()
            # Check if picture is already in the linked list. If it's, return message
            if photos_list.is_in_list(replacement_picture_format):
                print("\nPicture is already in the list. Please add another picture.")
            # Otherwise, replace old picture by the new picture
            else:
                replaced_picture = input("\nPlease introduce the name of the picture you want to replace from the list: ")
                replaced_picture_format = replaced_picture.lower()
                photos_list.replace(replaced_picture_format, replacement_picture_format)

                request = int(input("\nDo you want to replace another picture from the list? (Enter 1 for yes and 0 for no): "))
    
    # Display picture in the screen
    elif operation == 5:
        photos_list.display_photo_viewer()

    # Exit the menu
    elif operation == 6:
        exit_menu = "yes"
    
    print()


