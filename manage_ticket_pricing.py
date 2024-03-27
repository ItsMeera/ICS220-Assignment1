class ManageTicketPricing:

    def __init__(self):
        self.ticket_price = {
            "standard": 0,
            "group_discount": 0
        }
    def ticket_pricing(self):
        print("\nTicket Pricing Management Menu:")
        print("1. Set Ticket Prices")
        print("2. View Ticket Prices")
        print("3. Exit Ticket Pricing Management")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.set_ticket_prices()
            elif choice == "2":
                self.view_ticket_prices()
            elif choice == "3":
                print("Exiting ticket pricing management.")
                break
            else:
                print("Invalid choice. Please try again.")

    def set_ticket_prices(self):
        print("Set Ticket Prices:")
        print("1. Set Standard Ticket Price")
        print("2. Set Group Discount")
        print("3. Exit")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.set_standard_ticket_price()
            elif choice == "2":
                self.set_group_discount()
            elif choice == "3":
                print("Exiting ticket pricing setting.")
                break
            else:
                print("Invalid choice. Please try again.")

    def set_standard_ticket_price(self):
        price = float(input("Enter the standard ticket price: "))
        self.ticket_price["standard"] = price
        print("Standard ticket price set successfully.")

    def set_group_discount(self):
        discount_percentage = float(input("Enter the group discount percentage (e.g., 50 for 50%): "))
        self.ticket_price["group_discount"] = discount_percentage
        print("Group discount percentage set successfully.")

    def view_ticket_prices(self):
        print("\nTicket Prices:")
        print("Standard Ticket Price:", self.ticket_price.get("standard", "Not set"))
        print("Group Discount Percentage:", self.ticket_price.get("group_discount", "Not set"))