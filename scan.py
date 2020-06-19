#scan.py
#defines the scanning class for Kiosk program by Megan Smith
import datetime
import time

class Scans:
    def __init__(self):
        self.RFID = "NULL"
        self.date = "NULL"

    #returns RFID from reader and timestamp
    def scan(self, RFID):
        self.RFID = RFID
        d = datetime.datetime.fromtimestamp(time.time())
        self.date = d.ctime()
        return self.RFID



    
    
