# backend/gesture_detector.py

class GestureDetector:

    def __init__(self):
        pass

    def get_finger_states(self, landmarks):

        if len(landmarks) < 21:
            return None

        fingers = []

        # Thumb
        fingers.append(
            1 if landmarks[4][0] > landmarks[3][0] else 0
        )

        # Index
        fingers.append(
            1 if landmarks[8][1] < landmarks[6][1] else 0
        )

        # Middle
        fingers.append(
            1 if landmarks[12][1] < landmarks[10][1] else 0
        )

        # Ring
        fingers.append(
            1 if landmarks[16][1] < landmarks[14][1] else 0
        )

        # Pinky
        fingers.append(
            1 if landmarks[20][1] < landmarks[18][1] else 0
        )

        return fingers

    def detect(self, landmarks):

        fingers = self.get_finger_states(
            landmarks
        )

        if not fingers:
            return "NO_HAND"

        # Open Palm
        if fingers == [1, 1, 1, 1, 1]:
            return "OPEN_PALM"

        # Fist
        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        # Victory
        if fingers == [0, 1, 1, 0, 0]:
            return "VICTORY"

        # Thumbs Up
        if fingers == [1, 0, 0, 0, 0]:
            return "THUMBS_UP"

        return "UNKNOWN"
    