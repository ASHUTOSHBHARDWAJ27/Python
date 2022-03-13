or=cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eyedetector=cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')


while (True):
    ret,frame=cap.read()
    frame = cv2.cvtColor(frame,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detections = facedetector.detectMultiScale(gray , 1.3 , 5)
    if(len(detections)>0):
        (x,y,w,h) = detections[0]
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eyedetector.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        


    cv2.imshow('frame' , frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break