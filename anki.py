#! /usr/bin/python

import json
import urllib.request as ur
import sys
import re

with open('config.json') as f:
    config = json.load(f)

    base_url = config['base_url']
    default_deck = config['default_deck']

alfred_items = {"items": []}

def get_clipboard_img():

    from PIL import ImageGrab
    import base64
    from io import BytesIO

    img = ImageGrab.grabclipboard()
    if img != None:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")

        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    else:
        # alfred_items['items'].append({"title": "No image in clipboard"})
        return None


def anki_connect(params):

    params = json.dumps(params).encode('utf-8')
    update_request = ur.Request(base_url, params)
    try:
        response = ur.urlopen(update_request)
    except:
        alfred_items['items'].append({"title": "Network error"})

    result = json.loads(response.read())
    if result['error'] == None:
        return 'succeeded', result
    else:

        alfred_items['items'].append({"title": json.dumps(result)})
        return 'failed', result


def update_img(img_str):

    import time
    file_name = str(int(time.time())) + '.jpeg'

    params = {
        "action": "storeMediaFile",
        "version": 6,
        "params": {
            "filename": file_name,
            "data": img_str
        }
    }

    status, result = anki_connect(params)
    if status == "failed":
        alfred_items['items'].append({"title": "Uploading img failed"})

    return file_name


def add_note(front, back, deck = default_deck):

    params = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": []
            }
        }
    }

    status, result = anki_connect(params)
    if status == 'failed': alfred_items['items'].append({"title": "Adding note failed"})
    else: alfred_items['items'].append({"title": "Adding note succeeded"})

    return result


def anki_sync():

    params = {
        "action": "sync",
        "version": 6
    }

    status, result = anki_connect(params)
    if status == None: alfred_items['items'].append({"title": "Sychronizing failed"})
    else: alfred_items['items'].append({"title": "Sychronizing succeeded"})

    return result


if __name__ == '__main__':
    
    arg = ' '.join(sys.argv[1:])

    if arg == 'sync':

        anki_sync()
    
    else:

        # handle the clipboard
        if re.search(u'\{cb\}', arg) or re.search(u'「cb」', arg):

            img_str = get_clipboard_img()
            if img_str != None:
                clipboard_str = '<img src="%s">'%update_img(img_str)
            else:
                import pyperclip
                clipboard_str = pyperclip.paste()
            
            arg = re.sub(u'(?:\{cb\}|「cb」)', clipboard_str, arg)
        
        
        # handle the string

        ## choose the deck
        arg = arg.split("@@")
        if len(arg) > 1: deck = arg[1]
        else: deck = default_deck

        ## get the front and back
        arg = arg[0]
        if re.search('>>', arg): args = arg.split('>>')
        elif re.search('》》', arg): args = arg.split('》》')


        if len(args) <= 1:
            alfred_items['items'].append({"title": "Please seperate Front and Back using \"》》\" or \">>\""})

        else:

            ## add note
            add_note(args[0], args[1], deck)

    print(json.dumps(alfred_items))
