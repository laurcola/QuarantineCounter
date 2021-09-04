#DESKTOP NOTIFIER TO TELL THEE WHAT DAY OF QUARANTINE IT IS

#to do!
#export as .exe file
#make app run by itself when windows starts


import win10toast
from win10toast import ToastNotifier 
import datetime 
from datetime import date
from datetime import datetime

n = ToastNotifier()
quarantine_start = datetime(2020,3,13)
today = datetime.today()
day = today - quarantine_start

n.show_toast(f'Quarantine Day Count!',
           f'Congrats on staying alive during the pandemic! It has been {day} since the beginning of lockdown. Happy trails!', 
           icon_path='Kermit Looks at the Viewer (2).ico',
           duration=7)

