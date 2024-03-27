class Visitor():
    def __init__(self, username=None, password=None, name=None, age=None, nationality=None):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.tickets = []

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)