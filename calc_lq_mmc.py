import math


def calc_lq_mmc(lamda, mu, c=1):

    p0 = calc_p0(lamda, mu, c)

    if math.isinf(p0) or math.isnan(p0):
        return p0

    r = lamda / mu
    p = r / c

    if c > 1:
        lq_num = r ^ c * p * p0
        lq_denom = math.factorial(c) * (1 - p) ^ 2
    else:
        lq_num = lamda ^ 2
        lq_denom = mu * (mu - lamda)

    return lq_num / lq_denom
