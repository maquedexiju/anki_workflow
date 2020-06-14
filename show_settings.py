import sys
import json

arg = ' '.join(sys.argv[1:])

with open('config.json') as f:
    config = json.load(f)

params = {
    "items":[
        {
            "title": "Default Deck",
            "subtitle": config['default_deck'],
            "valid": False,
            "autocomplete": "Default Deck "
        },
        {
            "title": "AnkiConnect URL",
            "subtitle": config['base_url'],
            "valid": False,
            "autocomplete": "AnkiConnect URL "
        }
    ]
}

if arg.startswith('Default Deck'):

    title = {
        "title": "Set Default Deck to",
        "subtitle": arg[13:],
        "arg": 'anset',
        "valid": True
    }

    params['variables'] = {"settings": 'd' + arg[13:]}

elif arg.startswith('AnkiConnect URL'):

    title = {
        "title": "Set AnkiConnect URL to",
        "subtitle": arg[16:],
        "arg": 'anset',
        "valid": True
    }

    params['variables'] = {"settings": 'u' + arg[16:]}

else:

    title = {
        "title": "You can set the options listed below"
    }

  
params["items"].insert(0, title)
print(json.dumps(params))


    