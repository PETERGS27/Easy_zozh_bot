from main import body_config

ves = int(body_config['ves'])
rost = int(body_config['rost'])
voz = int(body_config['voz'])
ka = float(body_config['ka'])

def kbzu():
    if body_config['pol'] == 'men':
        bmr = 10 * ves + 6.25 * rost - 5 * voz + 5
        kbmr = bmr * ka
        if body_config['cel'] == 'phd':
            kal = kbmr * 0.9
        elif body_config['cel'] == 'nbv':
            kal = kbmr * 1.1
    elif body_config['pol'] == 'women':
        bmr = 10 * ves + 6.25 * rost - 5 * voz - 161
        kbmr = bmr * ka
        if body_config['cel'] == 'phd':
            kal = kbmr * 0.9
        elif body_config['cel'] == 'nbv':
            kal = kbmr * 1.1
    body_config['kal'] = kal