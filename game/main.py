from map import Map
from helicopter import Helicopter
from clouds import Clouds
from pynput import keyboard
import time
import os

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
MAP_WIDTH, MAP_HEIGHT = 15, 15
TICK_SLEEP = 0.2
TREE_UPDATE = 500
CLOUDS_UPDATE = 250
FIRE_UPDATE = 100

field = Map(MAP_WIDTH, MAP_HEIGHT)
clouds = Clouds(MAP_WIDTH, MAP_HEIGHT)
helicopter = Helicopter(MAP_WIDTH, MAP_HEIGHT)
tick = 1


def process_key(key):
    button = key.char.lower()
    if button in MOVES.keys():
        move_x, move_y = MOVES[button][0], MOVES[button][1]
        helicopter.move(move_x, move_y)


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    cls()
    field.print_stat(helicopter)
    field.print_map(helicopter, clouds)
    helicopter.process_helicopter(field, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)
