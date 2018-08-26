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
    black_squares = []
    image = cv2.imread('level5_hacked.png')

    lower = np.array([0, 0, 0])
    upper = np.array([10, 10, 10])
    shape_mask = cv2.inRange(image, lower, upper)

    _, cnts, _ = cv2.findContours(
        shape_mask.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in cnts:
        if is_square(cnt):
            x = cnt[0][0]
            black_squares.append('%s%s' % (Y[int(x[1]/50)], int(x[0]/50) + 1))

    green_squares = []
    lower = np.array([0, 200, 0])
    upper = np.array([10, 255, 10])
    shape_mask = cv2.inRange(image, lower, upper)

    _, cnts, _ = cv2.findContours(
        shape_mask.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for cnt in cnts:
        if is_square(cnt):
            x = cnt[0][0]
            green_squares.append('%s%s' % (Y[int(x[1]/50)], int(x[0]/50) + 1))

    print(green_squares)
    print(black_squares)
    print(';'.join(green_squares + black_squares))


if __name__ == '__main__':
    main()

# T1;S7;R16;P3;O3;N17;L20;C10;A1;T18;T6;P15;N13;N16;M18;J17;J14;I3;D2 + T12
