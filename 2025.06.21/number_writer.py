from pathlib import Path
import json

obj = {}
numbers = [2, 3, 5, 7, 11, 13]
obj['numbers'] = numbers
obj['status'] = 'success'


path = Path('numbers.json')
contents = json.dumps(obj)
path.write_text(contents)