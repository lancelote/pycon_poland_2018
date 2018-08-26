import numpy as np
import cv2

Y = 'ABCDEFGHIJKLMNOPQRST'


def is_square(cnt):
    if len(cnt) != 4:
        return False
    xs = []
    ys = []
    for i in cnt:
        for j in i:
            xs.append(j[0])
            ys.append(j[1])
    return max(xs) - min(xs) == max(ys) - min(ys)


def main():
    squares = []
    image = cv2.imread('level4.png')

    lower = np.array([0, 254, 0])
    upper = np.array([0, 255, 0])
    shape_mask = cv2.inRange(image, lower, upper)

    _, cnts, _ = cv2.findContours(
        shape_mask.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in cnts:
        if is_square(cnt):
            x = cnt[0][0]
            squares.append('%s%s' % (Y[int(x[1]/50)], int(x[0]/50) + 1))

    print(';'.join(squares))


if __name__ == '__main__':
    main()
