from math import *

step = 30
list_v = [v for v in range(-210, 180 + step, step)]

a = 40708
e = 0.8320
i = 61.00
Rt = 6378
Ut = 398600
law = 0
Lw = 120
w = 270
t0 = 0


def V_peri(Ut, a, e):
    Vp = sqrt(2 * (((-1 * Ut) / (2 * a)) + (Ut / (a * (1 - e)))))
    return Vp


def V_apoa(Ut, a, e):
    Va = sqrt(2 * (((-1 * Ut) / (2 * a)) + (Ut / (a * (1 + e)))))
    return Va


def Exo1(Ut, Rt, a, e):
    print('\nRa=', a * (1 + e), 'km')
    print('\nRp=', a * (1 - e), 'km')
    print('\nT=', 2 * pi * sqrt(a ** 3 / Ut), 'sec')
    print('\nZa=', a * (1 + e) - Rt, 'km')
    print('\nZp=', a * (1 - e) - Rt, 'km')
    print('\nVitesse angulaire n = ', sqrt(Ut / a ** 3), 'rad/s')
    print('\nVp=', V_peri(Ut, a, e), 'km/s')
    print('\nVa=', V_apoa(Ut, a, e), 'km/s')
    print("\nRatio = ", V_peri(Ut, a, e) / V_apoa(Ut, a, e))


def la(w, v, i):
    return degrees(asin(sin(radians(w + v)) * sin(radians(i))))


def srch(sum):
    sum = abs(sum)
    borne_inf = -90
    borne_sup = borne_inf + 180

    while True:
        if sum > borne_inf and sum <= borne_sup:
            return borne_inf, borne_sup

        borne_inf = borne_sup
        borne_sup += 180

        if borne_sup > 1000:
            print("Error range")
            break


def l0(w,v,i):
    try:
        l_0 = degrees(asin(tan(radians(la(w, v, i)))/tan(radians(i))))
    except:
        r = tan(radians(la(w, v, i)))/tan(radians(i))
        if r > 1:
            l_0 = degrees(asin(tan(1)/tan(1)))
        elif tan(radians(la(w, v, i)))/tan(radians(i)) < 1:
            l_0 = degrees(-asin(tan(1)/tan(1)))
        print('Remarque > la colonne pour v = %f est potentiellement fausse sauf t et La'%v)
        print('La valeur de de tan(rad(la))/tan(rad(i)) = %f'%r)
    sum = w + v

    if sum > -90 and sum <= 90:
        return l_0

    elif sum < -90:
        sup, inf, cor = -srch(sum)[0] - w, -srch(sum)[1] - w, -srch(sum)[0] - 90
    else:
        inf, sup, cor = srch(sum)[0] - w, srch(sum)[1] - w, srch(sum)[1] - 90

    if cor % 360 == 0:
        return cor + l_0
    else:
        return cor - l_0


def f(e, v):
    try:
        f = asin((sqrt(1 - (e ** 2)) * sin(v)) / (1 + e * cos(v)))
    except:
        print('la colonne pour v = %f est fausse' % v)
    return f


def temps(a, e, i, Ut, v, tp):
    vc = acos(-e)
    t = "error"
    if i > 90:
        sens = -1
    else:
        sens = 1
    v = radians(v)
    if v <= vc and v > -vc:
        t = tp + sqrt((a ** 3) / Ut) * (f(e, v) - e * (sqrt(1 - (e ** 2)) * sin(v)) / (1 + e * cos(v)))
    if v > vc and v <= pi * 2 - vc:
        t = tp + sqrt((a ** 3) / Ut) * (sens * pi - f(e, v) - e * (sqrt(1 - (e ** 2)) * sin(v)) / (1 + e * cos(v)))
    if v <= -vc and v > -2 * pi + vc:
        t = tp + sqrt((a ** 3) / Ut) * (-sens * pi - f(e, v) - e * (sqrt(1 - (e ** 2)) * sin(v)) / (1 + e * cos(v)))
    for n in range(1, 200):
        if v <= -vc + 2 * pi * (n + 1) and v > -vc + 2 * pi * n:
            t = tp + sqrt((a ** 3) / Ut) * (
                        sens * (n + 1) * pi + ((-1) ** (n + 1)) * f(e, v) - e * (sqrt(1 - (e ** 2)) * sin(v)) / (
                            1 + e * cos(v)))
        if v <= vc - 2 * pi * n and v > vc - 2 * pi * (n + 1):
            t = tp + sqrt((a ** 3) / Ut) * (
                        sens * (-n - 1) * pi + ((-1) ** (n + 1)) * f(e, v) - e * (sqrt(1 - (e ** 2)) * sin(v)) / (
                            1 + e * cos(v)))
    return t


def main(a, e, i, Ut, w, Lw, t0, list_v):
    alpha = 360 / 86164
    list_t = []
    list_la = []
    list_l0 = []
    list_ls = []

    for v in list_v:
        list_t.append(round(temps(a, e, i, Ut, v, -temps(a, e, i, Ut, -w, 0))))
        list_la.append(round(la(w, v, i)))
        list_l0.append(round(l0(w, v, i)))

    for m in range(len(list_l0)):
        list_ls.append(round(Lw + list_l0[m] - alpha * (list_t[m] - t0)))
        if abs(list_ls[m]) > 360:
            list_ls[m] = round(list_ls[m] % 360)
        if list_ls[m] > 180:
            list_ls[m] = round(list_ls[m] - 360)
        elif list_ls[m] < -180:
            list_ls[m] = round(list_ls[m] + 360)

    print("t:", list_t)
    print("la:", list_la)
    print("l0:", list_l0)
    print("ls:", list_ls)


Exo1(Ut, Rt, a, e)
print("v:", list_v)
main(a, e, i, Ut, w, Lw, t0, list_v)