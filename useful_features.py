from config import *
def prog(a, b, c, d):
    ''' Метод прогонки.
    '''
    M = len(d) - 1
    P = [0 for _ in range(M+1)]
    Q = [0 for _ in range(M+1)]
    u = [0 for _ in range(M+1)]

    P[0] = - c[0] / b[0]
    Q[0] = d[0] / b[0]

    for i in range(1, M+1):
        P[i] = - c[i]/(a[i] * P[i-1] + b[i])
        Q[i] = (d[i]-a[i]*Q[i-1])/(a[i]*P[i-1]+b[i])

    u[M] = Q[M]
    for i in range(M-1, -1, -1):
        u[i] = P[i] * u[i+1] + Q[i]

    return u
def grid(left, right, n):
    h = (right - left) / n
    return [left + h * i for i in range(n+1)]
def h(x_array):
    return (x_array[-1]-x_array[0])/(len(x_array)-1)
def tau(x_array):
    return q*h(x_array)/a_move
def diff_C(y_next, y_prev, x_next, x_prev):
    y_inter=[lagr(x_next[i], x_prev, y_prev) for i in range(len(y_next))]
    return max(map(abs, map(operator.sub, y_next, y_inter)))
def lagr(x, x_array, y_array):
    return lagrange_polynomial(x, select_nodes(x, x_array, y_array))
def lagrange_polynomial(x, points):
    size = len(points)
    result = 0
    for i in range(size):
        basic_pol = 1
        for j in range(size):
            if i == j:
                pass
            elif points[i][0] == points[j][0]:
                print("Bad data.")
                raise ValueError
            else:
                basic_pol *= (x - points[j][0]) / (points[i][0] - points[j][0])
        result += basic_pol * points[i][1]
    return result
def select_nodes(x, x_array, y_array):
    # ищем номер узла, предшествующего х
    for index in range(len(x_array)-1):
        if x_array[index] <= x < x_array[index+1]:
            prev_node = index
    if x <= x_array[0]:
        prev_node = 0
    if x >= x_array[-1]:
        prev_node = len(x_array) - 1
    interp_points = []
    # левая граница
    if prev_node < 3:
        for i in range(7):
            interp_points.append((x_array[i], y_array[i]))
    # правая граница
    elif prev_node >= len(x_array) - 3:
        for i in range(-7, 0):
            interp_points.append((x_array[i], y_array[i]))
    # общий случай
    else:
        for i in range(prev_node-3, prev_node+4):
            interp_points.append((x_array[i], y_array[i]))
    return interp_points
