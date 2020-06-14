# A Workflow to Add Anki Notes Quickly

## Other languages

* [中文](./README_CN.md)

## Features

* Add the notes using clipboard
* Custom your anki-connect server address
* Custom your default deck name

## Install

This workflow denpends on [anki-connect](https://github.com/FooSoft/anki-connect), you need to isntall anki-connect first.
You can follow the instruction from the Github, you need to keep the anki opened if you want to use anki-connect and this workflow.

After that, you can install this workflow in the release page, download and double click the anki.workflow to install.

If you want to use the clipboard features, you need to install this packages for your python interpreter

```shell
pip install Pillow
pip install pyperclip
```

## How to Use

Alfred is a great tool, and Anki is really helpful for memorizing.
Sometimes, you want to add a new note into Anki quickly. I take it an easy operation, which don't need complicated settings.
So this workflow only support the note of `Basic` type with simple grammar, I strongly suggest you to use this workflow with aText or some tools like this to to improve efficiency further.

```shell
# Add a new note into the default deck which need to be set by anset command first
an front>>back

# Add a new note into a custom deck
an front>>back@@deck

# Use the clipboard(image and text, but no format) with {cb} or 「cb」
an front>>「cb」@@deck
# or
an front>>{cb}
```

You can force the local data synchronize with the cloud use 

```shell
an sync
```

And you can set the default deck and anki-connect server address

```shell
# Set the default deck
anset Default Deck deck_name

# Set the anki-connect server address
anset AnkiConnect URL http://localhost:8765
```

## Trouble Shooting

Q: I've installed the Pillow and pyperclip, but the clipboard isn't working yet.
A: Please check the python interpreter you're using, in the workflow, I used the `/usr/bin/python`, you can change it in your workflow

Q: The Alfred debug information tells me that `UnboundLocalError: local variable 'response' referenced before assignment`
A: Please check whether your Anki is awaken, and set the environment mentioned in "Notes for Mac OS X Users" part of anki-connect [Github](https://github.com/FooSoft/anki-connect).