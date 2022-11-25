# Nyu 

![nyu](https://img.shields.io/badge/%20%20-nyu--self-informational), The successor of Jarvis A.I    [![nyu-self](https://img.shields.io/github/issues/Noqturnally/nyu-self)](https://github.com/Noqturnally/nyu-self/pulls)


## Installation  

The following pips must be installed before using

```
> pip install SpeechRecognition
> pip install pyttsx3
> pip install wikipedia
> pip install ecapture
> pip install wolframalpha
> pip install comtypes
> pip install json 

```
Run the python file or generated exe `nyu-self.exe` or `nyu-main.py`
 
### What if i get ImportError : cannot import _ctypes from COMTYPES

This error pops up mostly because you are using a linux system, COMTYPES doesnt support linux

### I want to add more commands, How do i do that

```python
elif '<command to speak>' in statement:
   <command args>
```

As an example, I'm gonna use the open gmail command

```python
elif 'open gmail' in statement: >> speak statement in ''
    webbrowser.open_new_tab("gmail.com") >> the tab to open or specific commands
    speak("WOO your account is mine") >> speak this out  as output
    time.sleep(5) >> wait 5 sec
```

### Can i use this code for my bot? 

 No, sorry you can use the original Jarvis A.I + modify it.
