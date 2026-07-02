import cv2
import csv
import os
from datetime import datetime

# -------------------------------
# Check if trainer file exists
# -------------------------------
if not os.path.exists("trainer.yml"):
    print("Error: trainer.yml not found!")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# -------------------------------
# Load Haar Cascade
# -------------------------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -------------------------------
# Load student data
# -------------------------------
students = {}

if not os.path.exists("students.csv"):
    print("Error: students.csv not found!")
    exit()

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            students[int(row[0])] = row[1]

# -------------------------------
# Open Camera
# -------------------------------
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error: Unable to access camera!")
    exit()

marked = []

print("Attendance System Started...")
print("Press ENTER to exit.")

while True:

    ret, img = cam.read()

    if not ret:
        print("Failed to capture image.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        student_id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 60:

            name = students.get(student_id, "Unknown")

            if name != "Unknown":

                if student_id not in marked:

                    now = datetime.now()

                    date = now.strftime("%d-%m-%Y")
                    time = now.strftime("%H:%M:%S")

                    with open("attendance.csv", "a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            student_id,
                            name,
                            date,
                            time
                        ])

                    marked.append(student_id)

                text = f"{name}"

            else:
                text = "Unknown"

        else:
            text = "Unknown"

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            img,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

    cv2.imshow("Attendance System", img)

    # Press Enter to Exit
    if cv2.waitKey(1) == 13:
        break

cam.release()
cv2.destroyAllWindows()