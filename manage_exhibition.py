class ManageExhibition:
    def __init__(self, title=None, location=None, start_date=None, end_date=None):
        self.title = title
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.catalog = {}  # Initialize the catalog as an empty dictionary
    
    def add_exhibition(self, exhibition_info=None):
        if exhibition_info is None:
            title = input("Enter title of the exhibition: ")
            date = input("Enter date of the exhibition: ")
            location = input("Enter location of the exhibition: ")
            start_date = input("Enter start date of the exhibition: ")
            end_date = input("Enter end date of the exhibition: ")

            # Create a dictionary to represent the exhibition
            exhibition_info = {
                "title": title,
                "date": date,
                "location": location,
                "start_date" : start_date,
                "end_date" : end_date,
            }

        # Add the exhibition to the catalog
        self.catalog[exhibition_info['title']] = exhibition_info
        print("Exhibition added to catalog.")

    def edit_exhibition(self):
        title = input("Enter title of the exhibition to edit: ")

        if title in self.catalog:
            # Display current information
            print("Current Information:")
            print(self.catalog[title])

            # Prompt for new information
            date = input("Enter new date of the exhibition (leave blank to keep current): ")
            location = input("Enter new location of the exhibition (leave blank to keep current): ")

            # Update exhibition information if new information provided
            if date:
                self.catalog[title]["date"] = date
            if location:
                self.catalog[title]["location"] = location

            print("Exhibition updated successfully.")
        else:
            print("Exhibition not found in catalog.")

    def remove_exhibition(self):
        title = input("Enter title of the exhibition to remove: ")

        if title in self.catalog:
            del self.catalog[title]
            print("Exhibition removed from catalog.")
        else:
            print("Exhibition not found in catalog.")
