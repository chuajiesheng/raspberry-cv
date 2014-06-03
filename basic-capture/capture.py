import cv
import sys

def main():
	frame = cv.CaptureFromCAM(0)
	print 'Captured'
	img = cv.QueryFrame(frame)
	print 'Queried'
	cv.SaveImage("capture.png", img)
	print 'Saved'

if __name__ == "__main__":
    main()
