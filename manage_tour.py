class ManageTour:
    def __init__(self):
        self.tour = {}

    def manage_tours(self):
        print("\nTour Management Menu:")
        print("1. Add Tour")
        print("2. Edit Tour")
        print("3. Remove Tour")
        print("4. View Tours")
        print("5. Exit Tour Management")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_tour()
            elif choice == "2":
                self.edit_tour()
            elif choice == "3":
                self.remove_tour()
            elif choice == "4":
                self.view_tours()
            elif choice == "5":
                print("Exiting tour management.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_tour(self):
        date = input("Enter the date of the tour: ")
        guide = input("Enter the name of the tour guide: ")
        group_size = input("Enter the group size for the tour: ")

        # Create a dictionary to represent the tour
        tour = {
            "date": date,
            "guide": guide,
            "group_size": group_size
        }

        # Add the tour to the list of tours
        self.tours.append(tour)
        print("Tour added successfully.")

    def edit_tour(self):
        date = input("Enter the date of the tour to edit: ")

        for tour in self.tours:
            if tour["date"] == date:
                # Display current information
                print("Current Information:")
                print(tour)

                # Prompt for new information
                guide = input("Enter new tour guide (leave blank to keep current): ")
                group_size = input("Enter new group size (leave blank to keep current): ")

                # Update tour information if new information provided
                if guide:
                    tour["guide"] = guide
                if group_size:
                    tour["group_size"] = group_size
                # Update additional details here

                print("Tour updated successfully.")
                return

        print("Tour not found.")

    def remove_tour(self):
        date = input("Enter the date of the tour to remove: ")

        for tour in self.tours:
            if tour["date"] == date:
                self.tours.remove(tour)
                print("Tour removed successfully.")
                return

        print("Tour not found.")

    def view_tours(self):
        if self.tours:
            print("\nTours:")
            for tour in self.tours:
                print("Date:", tour["date"])
                print("Guide:", tour["guide"])
                print("Group Size:", tour["group_size"])
                print("*********************************")
        else:
            print("No tours available.")
