import numpy as np
import glob
import matplotlib.pyplot as plt
from collections import deque

THRESHOLD1 = 200
THRESHOLD2 = 600

def bfs(variance, pos):
    CX = [1, 0, -1, 0]
    CY = [0, 1, 0, -1]
    s = set([(x, y) for x, y in pos])
    que = deque(pos)
    mask = np.zeros_like(variance, dtype=np.uint8)
    mask[variance < THRESHOLD1] = 255
    while len(que):
        x, y = que.popleft()
        for cx, cy in zip(CX, CY):
            nx, ny = x + cx, y + cy
            if variance[nx, ny] < THRESHOLD2 and (nx, ny) not in s:
                s.add((nx, ny)) 
                mask[nx, ny] = 255
                que.append((nx, ny))
    return mask

def main():
    vfile_names = glob.glob("*.npy")
    for idx, name in enumerate(vfile_names):
        variance = np.load(name)
        pos = np.c_[np.where(variance < THRESHOLD1)].tolist()
        mask = bfs(variance, pos)
        plt.subplot(231 + idx)
        plt.imshow(mask, cmap="gray")
        plt.title(name)
    plt.show()

if __name__ == "__main__":
    main()
