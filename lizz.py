import cv2

cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == 27:

        break

         #cv2.imwrite('captura_img.jpg',frame)

    if cv2.waitKey(1) == ord(' ') :
            cv2.imwrite('captura_img.jpg',frame)


cap.release()
cv2.destroyAllWindows()
