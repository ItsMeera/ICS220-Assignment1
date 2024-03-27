class ManageSpecialEvent:
    def __init__(self):
        self.event = {}

    def organize_special_events(self):
        print("\nSpecial Events Management Menu:")
        print("1. Add Special Event")
        print("2. Edit Special Event")
        print("3. Remove Special Event")
        print("4. View Special Events")
        print("5. Exit Special Events Management")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_special_event()
            elif choice == "2":
                self.edit_special_event()
            elif choice == "3":
                self.remove_special_event()
            elif choice == "4":
                self.view_special_events()
            elif choice == "5":
                print("Exiting special events management.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_special_event(self):
        name = input("Enter the name of the special event: ")
        date = input("Enter the date of the special event: ")
        location = input("Enter the location of the special event: ")
        # Create a dictionary to represent the special event
        event = {
            "name": name,
            "date": date,
            "location": location
        }

        # Add the special event to the list of events
        self.events.append(event)
        print("Special event added successfully.")

    def edit_special_event(self):
        name = input("Enter the name of the special event to edit: ")

        for event in self.events:
            if event["name"] == name:
                # Display current information
                print("Current Information:")
                print(event)

                # Prompt for new information
                date = input("Enter new date of the special event (leave blank to keep current): ")
                location = input("Enter new location of the special event (leave blank to keep current): ")
                # Update special event information if new information provided
                if date:
                    event["date"] = date
                if location:
                    event["location"] = location

                print("Special event updated successfully.")
                return

        print("Special event not found.")

    def remove_special_event(self):
        name = input("Enter the name of the special event to remove: ")

        for event in self.events:
            if event["name"] == name:
                self.events.remove(event)
                print("Special event removed successfully.")
                return

        print("Special event not found.")

    def view_special_events(self):
        if self.events:
            print("\nSpecial Events:")
            for event in self.events:
                print("Name:", event["name"])
                print("Date:", event["date"])
                print("Location:", event["location"])
                print("*******************************")
        else:
            print("No special events available.")
