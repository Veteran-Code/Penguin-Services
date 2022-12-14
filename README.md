# Penguin-Services
[![Test Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-success)](https://github.com/jacob-h-barrow/Penguin-Services)
[![Security](https://img.shields.io/badge/Secure-True-informational)](https://github.com/jacob-h-barrow/Penguin-Services)
[![Platform](https://img.shields.io/badge/Platform-Ubuntu%2020%2B-critical)](https://github.com/jacob-h-barrow/Penguin-Services)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-critical)](https://github.com/jacob-h-barrow/Penguin-Services)
[![MIT License](https://img.shields.io/badge/License-MIT-lightgrey)](https://github.com/jacob-h-barrow/Penguin-Services/blob/main/Penguin-Services.png)

![Penguin-Services](https://user-images.githubusercontent.com/112576275/190166942-016ed0cc-e11c-4db5-8d09-40d5f894d6f1.png)

- Created By Jacob H Barrow

## Why Was It Created
- Every time I start a new project, it seems that I reuse a lot of the same tools.
- Ideally, this package would be a one-stop shop for all of my projects moving forward.

## Critical Installation
``` console
penguin@services:~$ sudo apt install net-tools
```

## Short Tutorial
``` python
>>> from PenguinServices import DateRangeGenerator, Find, Terminal, makeFolder, getDate, fileHasher, Identifiers, openFile, pathExists, verifyFolder
>>> # Linux alternatives are untested at the moment
>>> # Examples but not all shown
>>>
>>> forward = DateRangeGenerator(15, 1, 2022, count=78)
>>> backwards = DateRangeGenerator(15, 1, 2022, count=78, forward = False)
>>> 
>>> for day in forward:
>>>   print(day, end=", ")
>>>
>>> for day in backwards:
>>>   print(day, end=", ")
>>>
>>> # Runs faster than find across a user directory. Still need to work out the code for dirSearch. Once that is solved, the code should be as fast as find for all scenarios.
>>> # Experimental Option to make fileOptions provided by os.stat(path)
>>> flatFiles = Find("/home/fox/Desktop/", patterns = [r'^.*[.]py$'], patternThreshold = 100, ignoreHidden = True)
>>> flatFiles() # get a list of files that were found
>>>
>>> makeFolder("/home/fox/LOG_STORAGE/")
>>> pathExists("/home/fox/")
>>> verifyFolder("/home/fox")
>>> data = openFile("/home/fox/test.txt", splitLines = False)/
>>>
>>> # Terminal is experimental right now
>>> ## Will be used like this
>>> funcObjs = {idx: funcObj for idx, funcObj in enumerate([*funcObjs])}
>>> shell = Terminal(funcObjs, prompt = "Example@Linux$ ", errorMessage = "Not heard!")
>>> shell.start()
>>>
>>> # Experimental right now: Identifiers, Terminal
```

### GetFiles
- It's a replacement for find in Unix, but it will have more features
- This code snippet will be crucial for modernizing SELinux, the firewall project next month, etc.
- Still a prototype!!!

## When Will More Tools Be Available
- When I need a custom utility that is not available with this package it will be developed and uploaded.

## Frequency Of Development
- When my wife is at work I am developing. So close to six days a week!!

## Remember
- If you find this package helpful, follow mascots and join Dumbledore's Army!
