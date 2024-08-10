class LibraryItem:
    def __init__(self, title, availability=True):
        self.title = title
        self.availability = availability

    def get_details(self):
        return f"Title: {self.title}, Availability: {'Available' if self.availability else 'Not Available'}"

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, availability=True):
        super().__init__(title, availability)
        self.issue_number = issue_number

    def get_details(self):
        details = super().get_details()
        return f"{details}, Issue Number: {self.issue_number}"

class DVD(LibraryItem):
    def __init__(self, title, duration, availability=True):
        super().__init__(title, availability)
        self.duration = duration

    def get_details(self):
        details = super().get_details()
        return f"{details}, Duration: {self.duration} minutes"

# Creating objects 
magazine = Magazine("National Geographic", "2024-08")
dvd = DVD("Inception", 148)
#Calling methods for these objects
print(magazine.get_details())
print(dvd.get_details())




