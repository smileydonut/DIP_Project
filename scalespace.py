import cv2
import numpy as np

def scalespace(grayframe,masksize):  #applying gaussian to generate scalespace

    for j in range (4):
        for i in range (0,5):

            mask = np.ones((masksize,masksize),np.float32)/(masksize)**2
            Gaussian = cv2.filter2D(grayframe,-1,mask)
            masksize = masksize +2;
            mask = np.ones((masksize, masksize), np.float32) / (masksize) ** 2
            if i == 1 and j == 1:
                cv2.imshow('blur2', Gaussian)
            if i == 1 and j == 2:
                cv2.imshow('blur3', Gaussian)
        dim_grayframe = np.shape(grayframe)
        dim_grayframe = dim_grayframe // 2;
        grayframe = cv2.resize(grayframe, dim_grayframe);




    return Gaussian





cap = cv2.VideoCapture('vid.MP4');



while(True):
    # Capture frames
    ret, frame = cap.read()
    if ret == False:
        break;

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    Blurred_frame = scalespace(grayframe, 3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


