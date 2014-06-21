# -*- coding: utf-8 -*-
import  time

def isToday():
    t = time.localtime()
    dia = time.strftime("%A", t)
    if dia == 'Monday':
        return {'isMonday': True}
    elif dia == 'Tuesday':
        return {'isTuesday': True}
    elif dia == 'Wednesday':
        return {'isWednesday': True}
    elif dia == 'Thursday':
        return {'isThursday': True}
    elif dia == 'Friday':
        return {'isFriday': True}
    elif dia == 'Saturday':
        return {'isSaturday': True}
    elif dia == 'Sunday':
        return {'isSunday': True}
    else:
        return {'hola': 'hola'}
