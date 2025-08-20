import cv2
import mediapipe as mp
import pyautogui
import math

# Disable fail-safe
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

# Smooth movement variables
smooth_factor = 0.5
smooth_index_x, smooth_index_y = 0, 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                    # Smooth movement
                    smooth_index_x = smooth_factor * smooth_index_x + (1 - smooth_factor) * index_x
                    smooth_index_y = smooth_factor * smooth_index_y + (1 - smooth_factor) * index_y

                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # Check if index_x and index_y are defined
                    if 'index_x' in locals() and 'index_y' in locals():
                        distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)

                        # Click button if thumb and index finger are close
                        if distance < 50:
                            pyautogui.click()

    # Move cursor
    pyautogui.moveTo(smooth_index_x, smooth_index_y)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()