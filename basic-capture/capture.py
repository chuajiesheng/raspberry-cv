import cv
capture = cv.CaptureFromCAM(0)
img = cv.QueryFrame(capture)
cv.SaveImage("capture.png", img)
