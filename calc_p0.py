import math


def calc_p0(lamda, mu, c=1):

    # Runs through basic checks for validity and feasibility
    if is_valid(lamda, mu, c) is False:
        return math.nan
    if is_feasible(lamda, mu, c) is False:
        return math.inf

    # Prepares working value of lamda (wlamda) for the rest of the calculations
    if isinstance(lamda, tuple):
        wlamda = sum(lamda)
    else:
        wlamda = lamda

    r = wlamda / mu
    p = r / c

    if c > 1:

        list_for_p0 = []

        for n in range(0, c):
            term1 = (r ^ n) / math.factorial(n)
            list_for_p0.append(term1)

        term2 = (r ^ c) / (math.factorial(c) * (1 - p))

        p0 = 1 / (sum(list_for_p0) + term2)

    else:
        p0 = 1 - p

    return p0
