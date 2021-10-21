# Face-Detect-and-Lock

A small project which allows to detect by camera if someone is in front of the computer. If the program does not detect anything, it will lock the computer.

It takes 1 photo every 5 seconds and analyzes it.

## Test :
Approved and Tested on Windows Portable Computer

## Installation :
 - Install Python 3.7 or Higher
 - Install Pip for Python 3

### 1st Step :

Git clone the repo : 
```
git clone https://github.com/ImAnonFR/Face-Detect-and-Lock
```

### 2nd Step : 
Go in the repo and install requirements :
```
cd Face-Detect-and-Lock
pip3 install -r requirements.txt
```

### 3rd Step : 
Start the script and be safe !
```
python3 face_detect_and_lock.py
```

⚠ Verify your cam before ⚠

You can launch it with Windows for improve security and you can change the timer between picture by change the value of : ``` sleep(5) ``` at the end of the face_detect_and_lock.py

The value is in Second
