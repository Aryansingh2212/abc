from signal import signal,SIGTERM,SIGHUP,pause
from rpi_lcd import LCD
from datetime import datetime


from pytz import timezone 
lcd=LCD()
def safe_exit(signum,frame):
    exit(1)
ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S.%f')
try:
    signal(SIGTERM,safe_exit)
    signal(SIGHUP,safe_exit)
    lcd.text(datetime.now(timezone("Asia/Kolkata")).strftime('%H:%M:%S.%f'),1)
    lcd.text("Saturday",2)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    
