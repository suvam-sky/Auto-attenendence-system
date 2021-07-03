import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic/elon mask.png')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('ImagesBasic/elon mask test.png')
imgTest = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

cv2.imshow('elon musk',imgElon)
cv2.imshow('elon musk',imgTest)
cv2.waitKey(0)