from PIL import ImageGrab, Image
from pynput import keyboard
import json, os, base64, requests, ctypes
from pyperclip import copy



def readJson() -> str:
    return json.loads(open("config.json", mode="r").read())["token"]

def ImageUpload(Image:str):
    if os.path.exists(Image):
        with open(Image, mode = "rb") as imageFile:
            payload = {
                "key": str(readJson()),
                "image": base64.b64encode(imageFile.read()),
            }
            url = requests.post("https://api.imgbb.com/1/upload", payload).json()["data"]["url"]
            return url


def on_press(key):
    image_name = "screenshot.png"

    if key == keyboard.Key.esc:

        img = ImageGrab.grabclipboard()
        if (isinstance(img, Image.Image)):
            img.save(image_name)
            image_url = (ImageUpload(Image=image_name))
            copy(f"[img]{image_url}[/img]")
            os.remove(image_name)
            ctypes.windll.user32.MessageBoxW(None, "Resim adresi kopyalandı","Sistem Bilgilendirme",0)
            


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


