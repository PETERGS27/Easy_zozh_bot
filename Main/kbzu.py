from regkbzu import ves, rost, voz, ka, bc

def kalkbzu():
    if bc['pol'] == 'men':
        bmr = 10 * ves + 6.25 * rost - 5 * voz + 5
        kbmr = bmr * ka
        if bc['cel'] == 'phd':
            kal = kbmr * 0.9
            return kal
        elif bc['cel'] == 'nbv':
            kal = kbmr * 1.1
            return kal
    elif bc['pol'] == 'women':
        bmr = 10 * ves + 6.25 * rost - 5 * voz - 161
        kbmr = bmr * ka
        if bc['cel'] == 'phd':
            kal = kbmr * 0.9
            return kal
        elif bc['cel'] == 'nbv':
            kal = kbmr * 1.1
            return kal