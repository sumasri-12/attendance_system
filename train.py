import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

faces = []
ids = []

for image in os.listdir(path):
    img_path = os.path.join(path, image)

    pil_img = Image.open(img_path).convert('L')
    img_numpy = np.array(pil_img, 'uint8')

    id = int(image.split(".")[1])

    faces.append(img_numpy)
    ids.append(id)

recognizer.train(faces, np.array(ids))
recognizer.save("trainer.yml")

print("Training Completed!")