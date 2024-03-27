from classes.visitor import Visitor

class PurchaseTicket:
    ticket_pricing = {"standard": 50, "group_discount": 0.1}
    def purchase_tickets(self):
        print("\nTicket Purchase Menu:")
        print("1. Purchase Standard Ticket")
        print("2. Purchase Group Ticket")
        print("3. Exit Ticket Purchase")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.purchase_standard_ticket()
            elif choice == "2":
                self.purchase_group_ticket()
            elif choice == "3":
                print("Exiting ticket purchase.")
                break
            else:
                print("Invalid choice. Please try again.")

    def purchase_standard_ticket(self, visitor_info=None):
        if visitor_info is None:
            # Get visitor details
            username = input("Enter username: ")
            password = input("Enter password: ")
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            nationality = input("Enter your nationality: ")
        else:
            username = visitor_info.get("username")
            password = visitor_info.get("password")
            name = visitor_info.get("name")
            age = visitor_info.get("age")
            nationality = visitor_info.get("nationality")

        # Create a Visitor object
        visitor = Visitor(username, password, name, age, nationality)

        # Purchase ticket for the visitor
        ticket_price = self.calculate_ticket_price(age)
        if ticket_price is not None:
            print(f"Your ticket price is: {ticket_price} AED")
            visitor.purchase_ticket({"type": "standard", "price": ticket_price})
            print("Ticket purchased successfully.")
            self.show_pricing_menu()

    def purchase_group_ticket(self):
        # Get visitor details
        username = input("Enter username: ")
        password = input("Enter password: ")
        name = input("Enter your name: ")
        group_size = int(input("Enter the size of your group: "))
        nationality = input("Enter your nationality: ")

        # Create a Visitor object
        visitor = Visitor(username, password, name, None, nationality)

        # Purchase ticket for the visitor
        ticket_price = self.calculate_group_ticket_price(group_size)
        if ticket_price is not None:
            print(f"Total price for the group: {ticket_price} AED")
            visitor.purchase_ticket({"type": "group", "price": ticket_price})
            print("Group ticket purchased successfully.")
            self.show_pricing_menu()

    def show_pricing_menu(self, choice=None):
        # Display pricing menu
        print("\nPricing Menu:")
        print("1. View Ticket Prices")
        print("2. Exit Pricing Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.view_ticket_prices()
        elif choice == "2":
            print("Exiting pricing menu.")
        else:
            print("Invalid choice. Please try again.")

        return choice
    
    def calculate_ticket_price(self, age):
            standard_price = self.ticket_pricing.get("standard", 0)
            discount = 0

            if 18 <= age <= 60:
                # No discount for standard tickets
                ticket_price = standard_price
            elif age < 18 or age >= 60:
                # Free ticket for children below 18 and seniors above 60
                ticket_price = 0
            else:
                print("Invalid age for standard ticket purchase.")
                return None

            # Apply VAT
            ticket_price += ticket_price * 0.05

            return ticket_price

    def calculate_group_ticket_price(self, group_size):
        standard_price = self.ticket_pricing.get("standard", 0)
        discount_percentage = self.ticket_pricing.get("group_discount", 0)

        # Calculate total price for the group with discount
        ticket_price = (standard_price * group_size) * (1 - discount_percentage / 100)

        # Apply VAT
        ticket_price += ticket_price * 0.05

        return ticket_price

    def view_ticket_prices(self):
        print("\nTicket Prices:")
        print(f"Standard Ticket Price: {self.ticket_pricing['standard']} AED")
        print(f"Group Ticket Discount: {self.ticket_pricing['group_discount'] * 100}%")    