#kiosk.py
from items import *
from scan import *
import datetime

def main():
    print("This will create an item")
    newItem = Items(123, 5.00, 0)
    print(newItem.itemid)
    newItem.placeHold()
    print(newItem.holdstatus)
    newItem.removeHold()
    print(newItem.holdstatus)
    newItem.removeHold()
    print(newItem.holdstatus)
    print("Now to give item a new RFID")
    scanRFID = Scans()
    newItem.setRFID(scanRFID.scan("ABC12377Q"))
    print(newItem.RFID)
    print("Scan Happened at:",' ', scanRFID.date)


main()
