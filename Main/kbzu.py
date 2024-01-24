import main

ves = int(main.body_config['ves'])
rost = int(main.body_config['rost'])
voz = int(main.body_config['voz'])
ka = float(main.body_config['ka'])

def kbzu():
    if main.body_config['pol'] == 'men':
        bmr = 10 * ves + 6.25 * rost - 5 * voz + 5
        kbmr = bmr * ka
        if main.body_config['cel'] == 'phd':
            kal = kbmr * 0.9
            main.body_config['kal'] = kal
        elif main.body_config['cel'] == 'nbv':
            kal = kbmr * 1.1
            main.body_config['kal'] = kal
    elif main.body_config['pol'] == 'women':
        bmr = 10 * ves + 6.25 * rost - 5 * voz - 161
        kbmr = bmr * ka
        if main.body_config['cel'] == 'phd':
            kal = kbmr * 0.9
            main.body_config['kal'] = kal
        elif main.body_config['cel'] == 'nbv':
            kal = kbmr * 1.1
            main.body_config['kal'] = kal