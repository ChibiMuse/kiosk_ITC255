#items.py
#class definition of Items for kiosk program

class Items:
    def __init__(self, itemID, price, location):
        self.itemid = itemID
        self.price = price
        self.itemlocation = 0

    #other values
        self.RFID = "No RFID Assigned"
        self.itemavailability = False
        self.holdstatus = 0

    #methods
    def setRFID(self, scan):
        self.RFID = scan

    def getRFID(self):
        return self.RFID

    def setLocation(self, location):
        self.itemlocation = location

    def getLocation(self):
        return self.itemlocation

    def placeHold(self):
        self.holdstatus += 1

    def removeHold(self):
        if self.holdstatus <= 0:
            self.holdstatus = 0
        else:
            self.holdstatus -= 1

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setitemavailability(self, availability):
        self.itemavailability = availability

    def getItemAvailability(self):
        return self.itemavailability
