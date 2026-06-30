# backend/hand_tracker.py

import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.hands.process(rgb)

        landmarks = []

        if results.multi_hand_landmarks:

            for hand in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, c = frame.shape

                for lm in hand.landmark:

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    landmarks.append((cx, cy))

        return frame, landmarks


if __name__ == "__main__":

    tracker = HandTracker()

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame, landmarks = tracker.find_hands(frame)

        cv2.imshow(
            "Hand Tracking",
            frame
        )

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    