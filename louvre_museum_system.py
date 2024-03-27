from classes.manage_catalog import ManageCatalog
from classes.manage_tour import ManageTour
from classes.manage_special_event import ManageSpecialEvent
from classes.manage_ticket_pricing import ManageTicketPricing

class LouvreMuseumSystem:
    def __init__(self, manage_catalog=None):
        self.catalog = {} if manage_catalog is None else manage_catalog.catalog
        self.exhibitions = []
        self.tours = []
        self.events = []
        self.visitors = []
        self.manage_catalog = ManageCatalog()
        self.manage_tour = ManageTour()
        self.manage_special_event = ManageSpecialEvent()
        self.manage_ticket_pricing = ManageTicketPricing()


    def authenticate_user(self, username, password):
        # Hardcoded credentials for demonstration purposes
        valid_username_admin = "admin"
        valid_password_admin = "adminpass"

        # Check if provided credentials match the hardcoded credentials for admin
        if username == valid_username_admin and password == valid_password_admin:
            self.show_admin_menu()  # Show admin menu
            return True  # Authentication successful

        else:
            print("Invalid username or password. Please try again.")
            return False  # Authentication failed

    def show_admin_menu(self):
        while True:
            print("Welcome, Admin!")
            print("1. Manage Catalog")
            print("2. Manage Tours")
            print("3. Organize Special Events")
            print("4. Manage Tickets")
            print("5. Logout")

            # Example: Prompt for user input to select an option
            choice = input("Enter your choice: ")

            # Logic to handle admin menu choices
            if choice == "1":
                self.manage_catalog.manage_catalog_menu()
            elif choice == "2":
                self.manage_tour.manage_tours()
            elif choice == "3":
                self.manage_special_event.organize_special_events()
            elif choice == "4":
                self.manage_ticket_pricing.ticket_pricing()    
            elif choice == "5":
                print("Logout Successfully!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def manage_tickets(self):
        print("\nManage Tickets:")
        for visitor in self.visitors:
            print(f"\nVisitor: {visitor.name}")
            if visitor.tickets:
                for ticket in visitor.tickets:
                    print(f"Ticket Type: {ticket['type']}, Price: {ticket['price']} AED")
            else:
                print("No tickets purchased by this visitor.")     