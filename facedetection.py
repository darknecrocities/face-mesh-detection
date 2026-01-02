import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ===============================
# USER INFO
# ===============================
NAME = "Arron Kian Parejas"
GENDER = "Male"
AGE = "20"

# ===============================
# LOAD FACE LANDMARKER
# ===============================
base_options = python.BaseOptions(model_asset_path="face_landmarker.task")

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False,
    num_faces=1
)

detector = vision.FaceLandmarker.create_from_options(options)

# ===============================
# CAMERA
# ===============================
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_image)

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]

        xs = [int(lm.x * w) for lm in landmarks]
        ys = [int(lm.y * h) for lm in landmarks]

        x1, x2 = min(xs), max(xs)
        y1, y2 = min(ys), max(ys)

        # Bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw mesh points
        for x, y in zip(xs, ys):
            cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)

        # Info panel
        panel_x = min(x2 + 10, w - 270)
        panel_y = y1

        cv2.rectangle(frame, (panel_x, panel_y),
                      (panel_x + 260, panel_y + 140),
                      (30, 30, 30), -1)

        cv2.rectangle(frame, (panel_x, panel_y),
                      (panel_x + 260, panel_y + 140),
                      (0, 255, 255), 2)

        cv2.putText(frame, f"Name: {NAME}", (panel_x + 10, panel_y + 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.putText(frame, f"Gender: {GENDER}", (panel_x + 10, panel_y + 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.putText(frame, f"Age: {AGE}", (panel_x + 10, panel_y + 105),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Face Mesh (Python 3.12)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
