import numpy as np
import cv2

blur_levels = 5;
octave_levels = 4;
cap = cv2.VideoCapture(0);
while(cap.isOpened()):
    ret, frame = cap.read();
    if ret == False:
        break;

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    k = 2;
    sigma = 1;

    for j in range(octave_levels):
        #sigma starting point changes by a factor of sqrt(2) after every octave
        sigma = np.sqrt(2) * 2;
        for i in range(blur_levels):
            blurred_frame = cv2.GaussianBlur(frame, (5, 5), sigma);
            if i == 0 and j == 0:
                cv2.imshow('Level 1', blurred_frame);
            if i == 4 and j == 1:
                cv2.imshow('Level 4', blurred_frame);

            sigma = k * sigma;

        frame_dim = np.array(np.shape(frame));
        frame_dim = (frame_dim / 2).astype(np.uint32);
        frame = cv2.resize(frame, tuple(np.flip(frame_dim, 0)));

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();