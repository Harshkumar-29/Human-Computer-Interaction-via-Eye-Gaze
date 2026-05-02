import cv2
import pyautogui
import time

# ================= INIT =================
cam = cv2.VideoCapture(1)


screen_w, screen_h = pyautogui.size()
pyautogui.FAILSAFE = False

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

prev_x, prev_y = 0, 0
smoothening = 6

last_click = 0
click_delay = 0.7

# ================= LOOP =================
while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cx = x + w // 2
        cy = y + h // 2

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

        # Cursor mapping
        screen_x = screen_w * cx / frame.shape[1]
        screen_y = screen_h * cy / frame.shape[0]

        # Smooth cursor
        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening

        pyautogui.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y

    cv2.imshow("Eye Mouse - Python 3.13 Compatible", frame)

    key = cv2.waitKey(1)

    # SPACE = click simulate
    if key == 32:
        if time.time() - last_click > click_delay:
            pyautogui.click()
            last_click = time.time()

    # ESC = exit
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
