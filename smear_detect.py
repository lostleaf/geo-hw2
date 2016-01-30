import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

def main():
    file_names = glob.glob("../cam_3/*.jpg")[:500]
    img = cv2.imread(file_names[0])
    img_avg = np.zeros_like(img, dtype=np.float64)
    for name in file_names:
        img = cv2.imread(name)
        img_avg += img
    img_avg /= len(file_names)
    plt.imshow(cv2.cvtColor(img_avg.astype(np.uint8), cv2.COLOR_BGR2RGB))
    img_avg_gray = cv2.cvtColor(img_avg.astype(np.uint8), cv2.COLOR_BGR2GRAY)
    variance = np.zeros_like(img_avg_gray, dtype=np.float)
    for name in file_names:
        img = cv2.imread(name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float)
        variance += (img_gray - img_avg_gray) ** 2
    variance /= len(file_names)
    plt.imshow(variance, cmap="gray")
    plt.colorbar()
    plt.show()
    plt.imshow(variance<500, cmap="gray")
    plt.show()

if __name__ == '__main__':
    main()
