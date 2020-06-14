import sys
import json

arg = ' '.join(sys.argv[1:])

with open('config.json') as f:
    config = json.load(f)

if arg.startswith('u'): 
    config['base_url'] = arg[1:]
elif arg.startswith('d'):
    config['default_deck'] = arg[1:]

with open('config.json', 'w') as f:
    json.dump(config, f)

print("Changed")


    