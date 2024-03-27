import sys
from classes.louvre_museum_system import LouvreMuseumSystem
from classes.purchase_ticket import PurchaseTicket

def main():
    museum_system = LouvreMuseumSystem()  # Create an instance of LouvreMuseumSystem
    purchase_ticket = PurchaseTicket()

    while True:
        print("\nMain Menu:")
        print("1. Admin Login")
        print("2. Purchase Ticket")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            if museum_system.authenticate_user(username, password):
                museum_system.show_admin_menu()  # Show admin menu
        elif choice == "2":
            purchase_ticket.purchase_tickets()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
