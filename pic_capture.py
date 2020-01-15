import numpy as np 
import cv2
# from qrcode import QRCode
'''
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''


'''

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


'''
# 1.creating a video object
video = cv2.VideoCapture(0) 
# 2. Variable
a = 0
# 3. While loop
while True:
    a = a + 1
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 8. image saving
showPic = cv2.imwrite("/home/fiftycentsjj/Downloads/filename.jpg",frame)
print(showPic)

# 9. image showing
img = cv2.imread("/home/fiftycentsjj/Downloads/filename.jpg")
cv2.imshow('image', img)
cv2.waitKey(0)

'''
# 10. qrcode showing

qrcode_pic = qrcode.make("/home/fiftycentsjj/Downloads/filename.jpg")

print(type(qrcode_pic))
print(qrcode_pic.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

qrcode.save('"/home/fiftycentsjj/Downloads/qrcode_test.png')

'''

# 11.. shutdown the camera
video.release()
cv2.destroyAllWindows
