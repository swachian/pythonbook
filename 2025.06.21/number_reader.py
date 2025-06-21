from pathlib import Path
import json

path = Path('numbers.json')
with open('numbers.json') as file:
    obj = json.load(file)
    print(obj)

obj = json.loads(path.read_text("UTF-8"))
print(obj)