
class Printer_Queue:
    def __init__(self) -> None:
        self.printing_order = []
        self.max_size = 10

    def enqueue(self, file_name):
        if len(self.printing_order) <= self.max_size:
            self.printing_order.append(file_name)
        else:
            print("\nQueue is full. No more file can be added. Please enter 0 when the program ask you if you want to add more files")
    
    def dequeue(self):    
        return self.printing_order.pop(0)
    
    def len(self):
        return len(self.printing_order)

list_of_orders = Printer_Queue()

request = 1
exit_menu = "no"

while exit_menu == "no":
    print("Printing Menu: ")
    print("1) Add files to print")
    print("2) Proceed to print")
    print("3) Exit")
    operation = int(input("\nSelect operation: "))

    if operation == 1:
        while request == 1:
            file_name = input("\nPlease introduce the name of the file you want to print: ")
            list_of_orders.enqueue(file_name)
            request = int(input("\nDo you want to print another file? (Enter 1 for yes and 0 for no): "))

    elif operation == 2:
        print()
        while list_of_orders.len() != 0:
            served_print = list_of_orders.dequeue()

            for x in range(30000000):      #Simulate a clock for the printing time
                pass

            print(f'>>>The file called "{served_print}" was already printed')
    
    elif operation == 3:
        exit_menu = "yes"
    
    print()







