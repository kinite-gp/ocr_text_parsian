import pytesseract
from PIL import Image, ImageGrab
import cv2
import matplotlib.pyplot as plt
import pyperclip
import os
import win10toast
import winreg

notif = win10toast.ToastNotifier()


def add_to_path():
    cwd = os.getcwd()
    variable_name = "TESSDATA_PREFIX"
    variable_value = os.path.join(cwd, "Tesseract-OCR", "tessdata")

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, variable_name, 0, winreg.REG_SZ, variable_value)
    winreg.CloseKey(key)

    notif.show_toast("Parsian OCR", "Successfully added to environment variables!")

    file = open("env", 'w')
    file.close()


file_path = 'env'

if os.path.exists(file_path):
    pass
else:
    add_to_path()

pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"

image = ImageGrab.grabclipboard()
status = None

if image is None:
    status = False
else:
    save_path = "image.png"
    image.save(save_path)
    status = True

if status:
    image = cv2.imread("image.png", 0)
    plt.imshow(image, cmap='gray')
    pytesseract.get_languages()
    ocr_text = pytesseract.image_to_string(image, lang="fas")
    pyperclip.copy(ocr_text)
    notif.show_toast("Parsian OCR", "Text copy to clipboard!")
else:
    notif.show_toast("Parsian OCR", "Please try again!")
