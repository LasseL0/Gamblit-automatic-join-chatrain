import pyautogui
import time

FIRST_IMAGE = 'join.png'
SECOND_IMAGE = 'join2.png'
CONFIDENCE = 0.6  # can change

def find_and_click(image, confidence=0.6):
    try:
        location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        if location is not None:
            print(f"found {image} location {location}, click.")
            pyautogui.click(location)
            return True
    except pyautogui.ImageNotFoundException:
        pass
    return False

def main():
    print("Bot running. Quit by pressing Ctrl+C")
    while True:
        if find_and_click(FIRST_IMAGE, CONFIDENCE):
            time.sleep(1)  # break bro
            if find_and_click(SECOND_IMAGE, CONFIDENCE):
                print("both clickked")
            else:
                print(f"not found brotha? wait for next rain or sum... or change better image{SECOND_IMAGE}.")
        else:
            print(f"not found brotha? wait for next rain or sum... or change better image{FIRST_IMAGE}.")
        time.sleep(0.5)  # break

if __name__ == "__main__":
    main()
