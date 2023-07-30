import time
import json
import importlib
import os
from utils.config import *
import src.Committees as Committees


def scan():
    path = os.path.join(ROOT, 'data/states.json')
    while True:
        with open(path, 'r') as f:
            states = json.load(f)
        if states['scan']['new']:
            importlib.reload(Committees)
            states['scan']['new'] = 0
            with open(path, 'w') as f:
                json.dump(states, f, indent=4)
        time.sleep(3600)

                    
            