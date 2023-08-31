import winreg
import os
from win10toast import ToastNotifier

cwd = os.getcwd()
variable_name = "TESSDATA_PREFIX"
variable_value = os.path.join(cwd, "Tesseract-OCR", "tessdata")

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, variable_name, 0, winreg.REG_SZ, variable_value)
winreg.CloseKey(key)

notif = ToastNotifier()
notif.show_toast("Activate OCR", "Successfully!!!!", "activate.ico")
