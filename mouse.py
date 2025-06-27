import cv2
import numpy as np
import mediapipe as mp
import autopy
import time
import math

wCam, hCam = 640, 480
frameR = 100
smoothening = 7

prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0

scrolling_mode = False
scroll_start_y = 0
scroll_threshold = 25

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

wScr, hScr = autopy.screen.size()

print("AI Mouse started.")
print("- Point with index finger to move.")
print("- Bring middle finger close to index to click.")
print("- Make a 'call me' sign (thumb and pinky up) to scroll.")
print("Press 'q' to quit.")

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        
        lm_list = []
        for id, lm in enumerate(hand_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append([id, cx, cy])

        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        if len(lm_list) != 0:
            x1, y1 = lm_list[8][1:]
            x2, y2 = lm_list[12][1:]
            x_thumb, y_thumb = lm_list[4][1:]
            x_pinky, y_pinky = lm_list[20][1:]
            wrist_y = lm_list[0][2]

            fingers = []
            tip_ids = [4, 8, 12, 16, 20]

            if lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1, 5):
                if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

            if fingers[1] == 1 and fingers[2] == 0:
                scrolling_mode = False
                screen_x = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                screen_y = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                
                curr_x = prev_x + (screen_x - prev_x) / smoothening
                curr_y = prev_y + (screen_y - prev_y) / smoothening

                autopy.mouse.move(curr_x, curr_y)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                prev_x, prev_y = curr_x, curr_y

            elif fingers[1] == 1 and fingers[2] == 1:
                scrolling_mode = False
                length = math.hypot(x2 - x1, y2 - y1)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

                if length < 40:
                    cv2.circle(img, (x1,y1), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
                    time.sleep(0.2)
            
            elif fingers[0] == 1 and fingers[4] == 1 and fingers[1] == 0 and fingers[2] == 0:
                cv2.putText(img, "SCROLLING", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                cv2.circle(img, (x_thumb, y_thumb), 15, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x_pinky, y_pinky), 15, (0, 0, 255), cv2.FILLED)

                if not scrolling_mode:
                    scrolling_mode = True
                    scroll_start_y = wrist_y
                
                delta_y = wrist_y - scroll_start_y

                if delta_y < -scroll_threshold:
                    autopy.mouse.scroll(1)
                    scroll_start_y = wrist_y

                elif delta_y > scroll_threshold:
                    autopy.mouse.scroll(-1)
                    scroll_start_y = wrist_y
            
            else:
                scrolling_mode = False

    cv2.imshow("AI Mouse", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Closing application...")
cap.release()
cv2.destroyAllWindows()