def kalories(x):
    ves = int(x['ves'])
    rost = int(x['rost'])
    voz = int(x['voz'])
    ka = float(x['ka'])
    if x['pol'] == 'men':
        bmr = 10 * ves + 6.25 * rost - 5 * voz + 5
        kbmr = bmr * ka
        if x['cel'] == 'phd':
            kal = kbmr * 0.9
            return kal
        elif x['cel'] == 'nbv':
            kal = kbmr * 1.1
            return kal
    elif x['pol'] == 'women':
        bmr = 10 * ves + 6.25 * rost - 5 * voz - 161
        kbmr = bmr * ka
        if x['cel'] == 'phd':
            kal = kbmr * 0.9
            return kal
        elif x['cel'] == 'nbv':
            kal = kbmr * 1.1
            return kal

def belki(x):
    kal = x['kal']
    if x['cel'] == 'phd':
        bel = kal * 0.3
        return bel
    elif x['cel'] == 'nbv':
        bel = kal * 0.35
        return bel

def zhiri(x):
    kal = x['kal']
    if x['cel'] == 'phd':
        zhir = kal * 0.3
        return zhir
    elif x['cel'] == 'nbv':
        zhir = kal * 0.25
        return zhir

def uglevods(x):
    kal = int(x['kal'])
    bel = int(x['bel'])
    zhir = int(x['zhir'])
    ugli = kal - bel - zhir
    return ugli