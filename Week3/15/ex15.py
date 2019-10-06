import math
import fileinput

def point_add(N_x, N_y, Q_x, Q_y, p):
    print("count")
    m = (Q_y - N_y) * pow((Q_x-N_x), p-2, p)
    ret_x = (m ** 2 - N_x - Q_x) % p
    ret_y = (m*(N_x - ret_x) - N_y) % p
    return ret_x, ret_y


def point_double(N_x, N_y, a, p):
    print("count")
    m = (3*(N_x ** 2)+a) * pow(2*N_y, p-2, p)   
    ret_x = (m ** 2 - N_x - N_x) % p
    ret_y = (m*(N_x - ret_x) - N_y) % p
    return ret_x, ret_y

if __name__ == '__main__':
    a = 10
    b = -21
    N = 41
    N_x = 3
    N_y = 6

    Q_x = 0
    Q_y = 0

    binary_multiplier = list(bin(57)[2:])

    for x in range(len(binary_multiplier), 0, -1):
        if binary_multiplier[x - 1] == '1':
            if (Q_x == 0 and Q_y == 0):
                Q_x = N_x
                Q_y = N_y
            else:
                Q_x, Q_y = point_add(N_x, N_y, Q_x, Q_y, N)
        N_x, N_y = point_double(N_x, N_y, a, N)

    print(Q_x, Q_y)

