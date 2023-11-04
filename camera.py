import time
from datetime import date
from picamera2 import Picamera2
import uploads3

today = date.today()

picam = Picamera2()
picam.start()
time.sleep(2)
filename = "img-" + today.strftime("%d-%m-%Y") + ".jpg"
picam.capture_file(filename)
picam.close()

uploads3.upload_file(filename, None)
