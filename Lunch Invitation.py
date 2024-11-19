def invitation():
    scientists = ['Darwin', 'Einstein', 'Newton']
    unavailable = 'Darwin'
    scientists.remove(unavailable)
    scientists.append('Doitch')
    scientists.insert(0, 'Kepler')
    scientists.insert(2, 'Hubble')
    scientists.insert(4, 'Kuri')

    def uninvited():
        for i in range(4):
            noninvited = scientists.pop()
            print(f'Sorry for canceling you invitation Mister {noninvited}')
    print(f'Sorry, but Mister {unavailable} wont be able to come')
    uninvited()
    for scientist in scientists:
        print(f'Good Morning,\n Mister {scientist.title()},I would like to invite you for a lunch'
              )
invitation()