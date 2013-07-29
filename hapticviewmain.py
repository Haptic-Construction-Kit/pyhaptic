# Test Button Program
# Checkout Line Example for possible visual rhythm based interface.
# To play with a bunch of kivy widgets live checkout:
# examples/demo/kivycatalog or examples/demo/showcase
# examples/widgets/tabbed_panel_showcase.py
# File Chooser
#

# Interface Ideas:
# Show 8 motors visually.  When you press on each one they will vibrate.
# Each motor has a series of pictures: off state, on state
# Show a sequencer visualization with the max measure length you can have.  Allow to record rhythm live and save as preset.

# Looks like I want togglebuttons in a group for the changing tabs

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
import serial
import glob
import os
import time

# Populate the text section with the info pulled from a query all statement.
# Find out which mode the atmel starts in - learning or active?
# Substitute "Spinner" with "DropDown" in the future.
# Needs Fixing: 
#   1.  Currently the Spinner actually requires you to press the button after selecting an option to update the
#   "text" field.  Is there an action other than on_release that I can use to trigger defining the current text.
#   2.  Altering or referencing variables within the kv. language from the python script can be a pain.  Maybe
#   convert the "Builder.load_string" stuff to python classes/objects instead and just don't use the kv language.
#   3. Find a cleaner way of generating the togglebuttons to define the rhythm.
#   4. Track state of toggle buttons
#   5. Provide user option to add an additional row of buttons to define a more intricate rhythym. 

Builder.load_string("""

<ControlLayout>:
    size_hint: 1, 1
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Home'
        GridLayout:
            cols: 2
            canvas:
                Rectangle:
                    pos: self.center_x, 5
                    size: 5, self.height - 10
                Rectangle:
                    pos: self.width/2, self.center_y + 15
                    size: self.width/2, 5
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: "Device Information"
                    bold: True
                    font_size: 22
                    markup: True
                Button:
                    text: 'Update!'
                    size_hint: (.55, .10)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    on_press: root.fieldUpdate(vers_label, motor_num_label, rhythm_label, magnitude_label)
                Label:
                    text: 'Version:'
                    bold: True
                Label:
                    id: vers_label
                    text: ''
                Label:
                    text: 'Number of Motors:'
                    bold: True
                Label:
                    id: motor_num_label
                    text: ''
                Label:
                    text: 'Rhythms:'
                    bold: True
                Label:
                    id: rhythm_label
                    text: ''
                Label:
                    text: 'Magnitudes:'
                    bold: True
                Label:
                    id: magnitude_label
                    text: ''
            FloatLayout:
                Label:
                    text: 'Select CommPort:'
                    pos_hint: {'center_x': .5, 'center_y': .95}
                    bold: True
                    font_size: 22   
                    markup: True
                Spinner:
                    text: root.commPort[0]
                    values: root.commPort[0], root.commPort[1], root.commPort[2]
                    size_hint: (.55, .10)
                    pos_hint: {'center_x': .5, 'center_y': .75}
                    on_release: root.commChoice = self.text
                Button:
                    text: 'Connect'
                    size_hint: (.95, .5)
                    pos_hint: {'center_x': .51, 'center_y': .26}
                    on_press: root.ser_connect(root.commChoice)

    TabbedPanelItem:
        text: 'Define Rhythm'
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Rectangle:
                    pos: 5, self.center_y + 175
                    size: self.width - 10, 5
                Rectangle:
                    pos: 5, self.center_y - 175
                    size: self.width - 10, 5
            Label:
                text: 'Midi-Like Interface'
                bold: True
                font_size: 22
            BoxLayout:
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    state: 'normal'
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
            BoxLayout:
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                ToggleButton:
                    size_hint: (1, .25)
                    pos_hint: {'center_x': .5, 'center_y': .5}
            Label:
                text: 'Each toggle button above represents 50ms of vibration time.'
            BoxLayout:
                Label:
                    text: 'Rhythm Name:'
                TextInput:
                    text: 'Enter rhythm name here.'
                    size_hint: (1, .5)
                    pos_hint: {'center_x': .5, 'center_y': .5}

    
    TabbedPanelItem:
        text: 'Help'
        RstDocument:
            text: '\\n'.join(("Reserve for Training", "-----------", "You are in the third tab."))
    
    TabbedPanelItem:
    	text: 'About'
    	Label:
    		text: 'Fourth tab content area'

<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Comm Port Select'
    Button:
        text: 'Connect!'
        on_press: root.dismiss()

""")

# Trying to implement a popup that asks to select your comm port and connect before going to main screen
# Would include this .kv syntax above:


# And the following class in the body:
class CustomPopup(Popup):
	pass

class ControlLayout(TabbedPanel):
    def __init__(self):
        TabbedPanel.__init__(self)
        self.commChoice = ""
        self.ser = ""
        self.enterCount = ['Enter', 0]
        self.qryData = []

    def show_popup(self):
        p = CustomPopup()
        p.open()

    def printMenu(self):
        time.sleep(2)
        while 1:
            line = self.ser.readline() 
            if len(line) > 1:
                print line
            else:
                break

    def ser_connect(self, commChoice):
        try:
            print commChoice
            self.ser = serial.Serial(commChoice, timeout=1)
            print "Connecting!"
        except:
            print "Failed to connect on ..."

        # Program expects enter/return hit 3 times to bring up initial menu options
        for x in range(4):
            self.ser.write(os.linesep)
            self.enterCount[1] += 1
            print self.enterCount
            time.sleep(2)
        
        #self.printMenu()
        self.qry_all()

    def qry_all(self):
        self.ser.write("4")
        time.sleep(2)
        self.ser.write("QRY ALL")
        self.ser.write(os.linesep)
        while 1:
            line = self.ser.readline() 
            #line = ser.read(20)
            if len(line) > 1:
                print line
                self.qryData.append(line)
            else:
                break
        print self.qryData

    def fieldUpdate(self, ver, motor, rhythm, mag):
        ver.text = self.qryData[10]
        motor.text = self.qryData[11]
        rhythm.text = self.qryData[12]
        mag.text = self.qryData[13] + self.qryData[14] + self.qryData[15] + self.qryData[16]

    # Need a way for the item list in the above kv spinner to be variable.
    if os.name == 'posix':
        commPort = glob.glob('/dev/tty.*')
        print "Printing current available comm ports.\n"
        for i in commPort:
            print i
    # Need to build in comm post scans for linux and windows.


class HapticControlApp(App):
    def build(self):
        return ControlLayout()


if __name__ == '__main__':
    HapticControlApp().run()