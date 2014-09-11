import cv2
import numpy as np
#from matplotlib import pyplot as plt

img_rgb = cv2.imread('../testimages/search-images/sample_hindi_01.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('../testimages/search-images/hi-template.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print "x:",pt[0],"y:",pt[1],"width:",pt[0]+w,"height:",pt[1]+h
#cv2.imwrite('res.png',img_rgb)
cv2.imshow('image',img_rgb);
cv2.waitKey(0)
cv2.destroyAllWindows();
