import pytesseract
from PIL import ImageGrab
import cv2
import pyperclip
from win10toast import ToastNotifier
import keyboard
from time import sleep

pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"
notif = ToastNotifier()
notif.show_toast("Start OCR 'fa'", "select with 'start+shift+s\nOCR with 'alt+shift+f'","icon.ico")


def ocr():
    image = ImageGrab.grabclipboard()

    if image is None:
        status = False
        notif.show_toast("Image not found", "please select with 'start+shift+s'","icon.ico", duration=3)
    else:
        save_path = "image.png"
        image.save(save_path)
        status = True

    if status:
        image = cv2.imread("image.png", 0)
        pytesseract.get_languages()
        ocr_text = pytesseract.image_to_string(image, lang="fas")
        pyperclip.copy(ocr_text)
        notif.show_toast("OCR successfully!", "Can sea in clipboard with 'ctrl+v' or 'start+v'","icon.ico", duration=3)


while True:
    logic = keyboard.is_pressed("alt") and keyboard.is_pressed("shift") and keyboard.is_pressed("f")

    if logic:
        ocr()
        sleep(5)
