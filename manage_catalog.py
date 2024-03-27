

class ManageCatalog:
    def __init__(self, manage_catalog=None):
        self.catalog = {} if manage_catalog is None else manage_catalog.catalog
    
    def manage_catalog_menu(self):
        while True:
            print("\nCatalog Management Menu:")
            print("1. Add Artwork/Artifact")
            print("2. Edit Artwork/Artifact")
            print("3. Remove Artwork/Artifact")
            print("4. Add Exhibition")
            print("5. Edit Exhibition")
            print("6. Remove Exhibition")
            print("7. View Catalog")
            print("8. Exit Catalog Management")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_artwork()
            elif choice == "2":
                self.edit_artwork()
            elif choice == "3":
                self.remove_artwork()
            elif choice == "4":
                self.add_exhibition()
            elif choice == "5":
                self.edit_exhibition()
            elif choice == "6":
                self.remove_exhibition()
            elif choice == "7":
                self.view_catalog()
            elif choice == "8":
                print("Exiting catalog management.")
                break
            else:
                print("Invalid choice. Please try again.")
        
    def add_artwork(self, artwork_info=None):
        if artwork_info is None:
            title = input("Enter title of artwork/artifact: ")
            artist = input("Enter artist's name: ")
            date_of_creation = input("Enter date of creation: ")
            historical_significance = input("Enter historical significance: ")
            location = input("Enter exhibition location (permanent galleries, exhibition halls, outdoor spaces): ")

            # Create a dictionary to represent the artwork/artifact
            artwork_info = {
                "title": title,
                "artist": artist,
                "date_of_creation": date_of_creation,
                "historical_significance": historical_significance,
                "location": location
            }

        # Add the artwork/artifact to the catalog
        self.catalog[artwork_info['title']] = artwork_info
        print("Artwork/artifact added to catalog.")

    def edit_artwork(self):
        title = input("Enter title of artwork/artifact to edit: ")

        if title in self.catalog:
            # Display current information
            print("Current Information:")
            print(self.catalog[title])

            # Prompt for new information
            artist = input("Enter new artist's name (leave blank to keep current): ")
            date_of_creation = input("Enter new date of creation (leave blank to keep current): ")
            historical_significance = input("Enter new historical significance (leave blank to keep current): ")
            location = input("Enter new exhibition location (permanent galleries, exhibition halls, outdoor spaces) "
                             "(leave blank to keep current): ")

            # Update artwork information if new information provided
            if artist:
                self.catalog[title]["artist"] = artist
            if date_of_creation:
                self.catalog[title]["date_of_creation"] = date_of_creation
            if historical_significance:
                self.catalog[title]["historical_significance"] = historical_significance
            if location:
                self.catalog[title]["location"] = location

            print("Artwork/artifact updated successfully.")
        else:
            print("Artwork/artifact not found in catalog.")

    def remove_artwork(self):
        title = input("Enter title of artwork/artifact to remove: ")

        if title in self.catalog:
            del self.catalog[title]
            print("Artwork/artifact removed from catalog.")
        else:
            print("Artwork/artifact not found in catalog.")

    def view_catalog(self):
        if self.catalog:
            print("\nCatalog:")
            for title, item in self.catalog.items():
                print(f"Title: {title}")
                if "artist" in item:
                    print("Type: Artwork/Artifact")
                    for key, value in item.items():
                        print(f"{key.capitalize()}: {value}")
                elif "date" in item:
                    print("Type: Exhibition")
                    for key, value in item.items():
                        print(f"{key.capitalize()}: {value}")
                print()
        else:
            print("Catalog is empty.")

