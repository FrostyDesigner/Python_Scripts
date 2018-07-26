from typing import Any
from typing import Dict
from typing import Iterable

def keys_containing_value(d: Dict, needle: Any):
    def recursively_in(x: Any, n: Any):
        if isinstance(x, str) and isinstance(n, str):
            return n in x
        if type(x) is type(n):
            return x == n
        if isinstance(x, Iterable) and not isinstance(x, str):
            return any(recursively_in(item, n) for item in x)
    return [k for k, v in d.items() if recursively_in(v, needle)]


mydict = {
    'Joffrey': 15, #dead, Baratheon 
    'Tommen': 15, #dead, Baratheon 
    'Myrcella': 15, #dead, Baratheon 
    'Cersei': 'red', #Lannister
    'Jaime ': 'red', #Lannister
    'Tyrion': 'red', #Lannister
    'Daenerys': 'princess',
    'Viserys': 'prince',
    'Jorah': 'protector', 
    'Rob': 'prince', #dead, Stark
    'Sansa': 'the gray field is on fire', #Stark
    'Arya': ['smart', 'no name'], #Stark
    'Bran': 'shelly plays on the gray field', #Stark
    'Rickon': ['smart', 'dead'], #dead, Stark
    'Jon': ['intelligent', 'cuts the smart gray field grass', 'prince'], #Snow
}
needles = [
    15,
    'red',
    'princess',
    'prince',
    'gray field',
    'no name'
]
for needle in needles:
    print(keys_containing_value(mydict, needle))