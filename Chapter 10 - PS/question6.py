# Can you change the self-parameter inside a class to something else (say "ankit"). Try changing self to "slf" or "ankit" and see the effects.

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(ankit, starting, ending):
        print(f"Ticket is booked in train no: {ankit.trainNo} from {starting} to {ending}")

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time.")

    def getFare(self, starting, ending):
        print(f"Ticket fare in train no: {self.trainNo} from {starting} to {ending} is {randint(250, 3000)}")

t = Train(12457)
t.book("Banglore", "Delhi")
t.getStatus()
t.getFare("Banglore", "Delhi")

# It doesn't matter that what name we are using either it is "slf" or "ankit". But for maintaining the convention and the code looks good we use self instead of any other thing.
