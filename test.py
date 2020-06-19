#test.py
#testing file for Kiosk Program by Megan Smith

import unittest
import test
import datetime
import time
from items import Items
from scan import Scans

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Items(123, 5.00, 0)

    def test_itemstring(self):
        self.assertEqual(str(self.item), '123 price: $5.0 RFID:No RFID Assigned')

    def test_getRFID(self):
        self.assertEqual(self.item.getRFID(), 'No RFID Assigned')

    def test_setRFID(self):
        self.item.setRFID('FOO123BAR')
        self.assertEqual(self.item.getRFID(), 'FOO123BAR')

    def test_getAvailability(self):
        self.assertEqual(self.item.getItemAvailability(), False)

    def test_setAvailability(self):
        self.item.setItemAvailability(True)
        self.assertEqual(self.item.getItemAvailability(), True)

    def test_placeHold(self):
        self.item.placeHold()
        self.assertEqual(self.item.holdstatus, 1)

    def test_removeHold(self):
        self.item.removeHold()
        self.assertEqual(self.item.holdstatus, 0)

    def test_removeHoldZero(self):
        count = 0
        while (count < 3):
            self.item.removeHold()
            self.assertEqual(self.item.holdstatus, 0)
            count += 1
        self.assertEqual(self.item.holdstatus, 0)


class ScanTest(unittest.TestCase):
    def setUp(self):
        self.item = Items(456, 10.55, 0)
        self.scan = Scans()
        self.scandate = datetime.datetime.fromtimestamp(time.time())

    def test_scan(self):
        self.item.setRFID(self.scan.scan('SHRUB987'))
        self.assertEqual(self.item.RFID, 'SHRUB987')

    def test_datetime(self):
        self.item.setRFID(self.scan.scan('RABB17'))
        self.scandate = datetime.datetime.fromtimestamp(time.time())
        self.assertEqual(self.scan.date, self.scandate.ctime())
        

if __name__ == '__main__':
    unittest.main()
