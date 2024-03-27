import unittest
from unittest.mock import patch
from classes.louvre_museum_system import LouvreMuseumSystem
from classes.manage_catalog import ManageCatalog
from classes.manage_special_event import ManageSpecialEvent
from classes.visitor import Visitor
from classes.purchase_ticket import PurchaseTicket
from classes.manage_exhibition import ManageExhibition

class TestMuseumSystem(unittest.TestCase):
    def setUp(self):
        # Create instances of system components
        self.manage_catalog = ManageCatalog()
        self.manage_special_event = ManageSpecialEvent()
        self.purchase_ticket = PurchaseTicket()
        self.manage_exhibition = ManageExhibition()
        # Initialize the museum system
        self.museum_system = LouvreMuseumSystem()
        self.visitor = Visitor()

    def test_add_new_art_to_catalog(self):
        # Add new artwork to the catalog
        artwork_info = {
            "title": "Mona Lisa",
            "artist": "Leonardo da Vinci",
            "date_of_creation": "1503-1506",
            "historical_significance": "Iconic portrait",
            "location": "Room 6, Denon Wing"
        }
        self.manage_catalog.add_artwork(artwork_info)
        self.assertIn("Mona Lisa", self.manage_catalog.catalog.keys())

    def test_open_new_exhibition(self):
        # Open a new exhibition
        exhibition_info = {
            "title": "Ancient Egypt: The Great Discoveries",
            "location": "Egyptian Antiquities",
            "start_date": "2024-05-01",
            "end_date": "2024-05-02",
        }
        self.manage_exhibition.add_exhibition(exhibition_info)
        self.assertIn("Ancient Egypt: The Great Discoveries", self.manage_exhibition.catalog.keys())

    def test_purchase_tickets(self):
        with patch('builtins.input', side_effect=['1']):  # Simulate user input
            # Create an instance of PurchaseTicket
            purchase_ticket = PurchaseTicket()

            # Call the method to test and capture the choice made
            choice = purchase_ticket.show_pricing_menu()

            # Check that the choice matches the expected value
            self.assertEqual(choice, '1')

    def test_display_payment_receipts(self):
        # Simulate the display of payment receipts for purchasing tickets
        visitor = Visitor("visitor1", "password", "John Doe", 25, "American")
        visitor.purchase_ticket({"type": "standard", "price": 50})
        purchase_ticket = PurchaseTicket()
        receipt = purchase_ticket.view_ticket_prices()
        print(receipt)  # Check if the receipt is generated

if __name__ == '__main__':
    unittest.main()
