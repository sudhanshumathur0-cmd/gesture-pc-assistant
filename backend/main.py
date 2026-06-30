import cv2

from hand_tracker import HandTracker
from gesture_detector import GestureDetector
from action_controller import ActionController
from gesture_helper import draw_help   # NEW ADD


tracker = HandTracker()
detector = GestureDetector()
controller = ActionController()

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # ---------------- HAND TRACKING ----------------
    frame, landmarks = tracker.find_hands(frame)

    # ---------------- GESTURE DETECTION ----------------
    gesture = detector.detect(landmarks)

    # ---------------- ACTION EXECUTION ----------------
    if gesture:
        controller.execute(gesture)

    # ---------------- TEXT DISPLAY ----------------
    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ---------------- HELP OVERLAY (NEW FEATURE) ----------------
    frame = draw_help(frame)

    # ---------------- SHOW WINDOW ----------------
    cv2.imshow("AI Gesture Assistant", frame)

    # ESC key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()