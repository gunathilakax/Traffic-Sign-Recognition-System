import cv2
import os
import time
import io
import json
import cv2
import numpy as np
import requests
import json
import pyperclip
import pyautogui


#HOW TO RUN? Step by Step Guide
# 1) First Open 'test4_full_code' in Pyscripter
# 2) Second Open Arduino IDE 'FullCode.ino'
# 3) Then press win + <- key to align, pyscripter to the left
# 4) Then press win + -> key to align, Arduino IDE to the left

#   STEP 3 AND 4 ARE VERY Impotent

# 5) If 25 requests has been expired, replace that code as following


path_save_the_ss = os.path.dirname(os.path.realpath(__file__))

def capture_screenshot():
    # Open webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Failed to open webcam")
        return

    # Read and display webcam preview for 3 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read from webcam")
            return
        cv2.imshow("Webcam Preview", frame)
        cv2.waitKey(1)

    # Capture screenshot after 3 seconds
    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"traffic_sign.jpg"
        filepath = os.path.join(rf'{path_save_the_ss}', filename)
        cv2.imwrite(filepath, frame)
        print(f"Screenshot captured and saved as '{filepath}'")

    # Close webcam
    cap.release()
    cv2.destroyAllWindows()






    #----------------Send to the OCR Space website Firstly ----------------------------
    image = r'traffic_sign.jpg'
    Api_key = "K89471999088957"


    img = cv2.imread(image) #image goes here

    # Ocr
    url_api = "https://api.ocr.space/parse/image"
    _, compressedimage = cv2.imencode(".jpg", img, [1, 90])
    file_bytes = io.BytesIO(compressedimage)

    result = requests.post(url_api,
                  files = {image: file_bytes},
                  data = {"apikey": Api_key,
                          "language": "eng"})



    result = result.content.decode()
    result = json.loads(result)


    parsed_results = result.get("ParsedResults")[0]
    text_detected = parsed_results.get("ParsedText")
    print(text_detected)


    #----------------Check whether it has "kmph" Text. Then only it sends to the server ----------------------------

    if(("km/h" in text_detected) or ("kmph" in text_detected)):
        print("This is a traffic sign")

        pyautogui.hotkey('alt', 'tab',)
        pyautogui.write('-1')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('alt', 'tab',)




        #----------------sends to the Rapid API server to identify the number (only 25 attempts)----------------------------
        url = "https://ocr43.p.rapidapi.com/v1/results"

        files = {"image": open(r"traffic_sign.jpg", "rb")}
        payload = { "url": "https://storage.googleapis.com/api4ai-static/samples/ocr-1.png" }
        headers = {
            "X-RapidAPI-Key": "5cda8d51e7mshd600748ed7e4f2fp18862djsn2fc7d7a1f32f",
            "X-RapidAPI-Host": "ocr43.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, files=files, headers=headers)

        print(response.json())


        #----------------sends to the Rapid API server to identify the number (only 25 attempts)----------------------------




        json_response = response.json()
        # Extracting numbers from the "text" field
        for result in json_response["results"]:
            for entity in result["entities"]:
                for obj in entity["objects"]:
                    for text_entity in obj["entities"]:
                        if text_entity["kind"] == "text":
                            text = text_entity["text"]
                            numbers = [word for word in text.split() if word.isdigit()]
                            print("Numbers:", numbers)


                            speed_limit = numbers[0]
                            pyperclip.copy(speed_limit)
                            pyautogui.hotkey('alt', 'tab',)
                            pyautogui.hotkey('ctrl', 'v', 'enter')










    else:
        capture_screenshot()


if __name__ == "__main__":
    capture_screenshot()
