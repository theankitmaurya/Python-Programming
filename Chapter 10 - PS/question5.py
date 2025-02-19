# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, starting, ending):
        print(f"Ticket is booked in train no: {self.trainNo} from {starting} to {ending}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time.")

    def getFare(self, starting, ending):
        print(f"Ticket fare in train no: {self.trainNo} from {starting} to {ending} is {randint(250, 3000)}")

t = Train(12457)
t.book("Banglore", "Delhi")
t.getStatus()
t.getFare("Banglore", "Delhi")
