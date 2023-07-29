import time
import json
import importlib
import os
from utils.config import *
import src.Committees as Committees


def scan(sleep_time):
    while True:
        time.sleep(sleep_time)
        with open(os.path.join(ROOT, 'data/states.json', 'r+')) as f:
            states = json.load(f)
            if states['scan']['new']:
                importlib.reload(Committees)
                states['scan']['new'] = 0
                json.dump(states, f)
                    
            