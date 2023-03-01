
import numpy as np
from PIL import Image
import cv2 as cv
import os


root = u'D:\\tmp\\img'

labels = list(sorted(os.listdir(os.path.join(root, "masks"))))

for i in range(len(labels)):
    label_path = os.path.join(root, "masks", labels[i])
    label = cv.imread(label_path)
    B, G, R = cv.split(label)
    R = np.array(R)/10.0  #改为二值png
    R = R.astype(np.uint8)
    Image.fromarray(R).save('D:/tmp/img/8bit/' + labels[i])









