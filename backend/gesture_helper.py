import cv2

def draw_help(frame):

    cv2.rectangle(frame, (5, 5), (300, 220), (40, 40, 40), -1)

    cv2.putText(frame, "GESTURE PANEL", (15, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, "OPEN PALM  -> Browser", (15, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, "FIST       -> Mute", (15, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, "VICTORY    -> Screenshot", (15, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, "THUMBS UP  -> Play/Pause", (15, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, "PINCH      -> Close Browser", (15, 180),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.putText(frame, "VOL UP/DN  -> Volume", (15, 210),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return frame
