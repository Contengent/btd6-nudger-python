# Imports
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller

# simplify Controller()
mouse = Controller()

# I honestly don't remember what any of this does lol
def movie(key):
    def contral(kii, x, y):
        if key == kii:
            mouse.move(x, y)

    contral(Key.up, 0, -1)
    contral(Key.down, 0, 1)
    contral(Key.left, -1, 0)
    contral(Key.right, 1, 0)  

    if key == Key.delete: 
        return False

# Collect all event until released
with Listener(on_press = movie) as listener:
    listener.join()

