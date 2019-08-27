import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    check, frame = cap.read()

    if check == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_gray = gray[y:y+h, x:x+w]
            face_color = gray[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(face_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(face_gray, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
                cv2.imwrite("Photo.jpg", frame)
        cv2.imshow('img', frame)
        print("Frames Per Second is: {}".format(cv2.CAP_PROP_FPS))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
