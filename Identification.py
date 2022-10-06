import cv2
import numpy as np
import face_recognition

imgkj = face_recognition.load_image_file('ImagesBasic/KJ.jpg')
imgkj = cv2.cvtColor(imgkj,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('ImagesBasic/12.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgkj)[0]
encodekj = face_recognition.face_encodings(imgkj)[0]
cv2.rectangle(imgkj,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255),2)

faceLoctest = face_recognition.face_locations(imgtest)[0]
encodekjtest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255),2)

results = face_recognition.compare_faces([encodekj], encodekjtest)
faceDis = face_recognition.face_distance([encodekj], encodekjtest)
print(results, faceDis)
cv2.putText(imgtest, f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('KJ', imgkj)
cv2.imshow('KJ_test', imgtest)
cv2.waitKey(0)