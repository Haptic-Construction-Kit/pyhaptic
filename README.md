pyhaptic
========

Multi-platform GUI interface for haptic controllers written in Python for the open Haptic-Construction-Kit.

Requires Python, and pyserial
Command line only right now, GUI in development

Inclue pyhaptic.py and create a HapticInterface object.

Theres a small test program (test_pyhaptic.py) included to show usage examples

Install
Linux:
sudo apt-get install python pip
sudo pip install pyserial

Windows:
http://www.python.org/download/releases/
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyserial

To run:
double click test_pyhaptic.py or run
python test_pyhaptic.py

To Use:
You're provided a list of COM ports we can see. If your device isnt listed it isn't plugged in or the drivers are not installed
type which device you wish to use

For now theres simply function0 through function9 which you can alter and trigger with the inputs of 0 -9 on the keyboard
