import logging
import threading
import time
import json
import importlib
import os
from src.config import *
import src.Committees as Committees


class Scan:
    def __init__(self):
        self.sleep_time = 0
    
    def __call__(self, *args, **kwargs):
        while True:
            time.sleep(self.sleep_time)
            with open(os.path.join(ROOT, 'data/states.json', 'r+')) as f:
                states = json.load(f)
                self.sleep_time = states['scan']['time']
                if states['scan']['new']:
                    importlib.reload(Committees)
                    states['scan']['new'] = 0
                    json.dump(states, f)
                    
            