from django.shortcuts import render
import random

def index(request):
    sentence = ''
    fWords = ['Privet', 'Zrdavstvui', 'Dobriy den']
    sWords = [', spasibo chto napisali', ', blagodaru za predlojenie', ', horosho, chto vi mne napisali']
    tWords = [', no mne ne podhodit vashe predlojenie:)', ', no ya ne podhoju dlya etoi vakansii:(', ', no mne ne podhodyat uslovia:(']
    num = random.randint(0, 2)
    sentence+=fWords[num]
    num = random.randint(0, 2)
    sentence+=sWords[num]
    num = random.randint(0, 2)
    sentence+=tWords[num]
    return render(
        request,
        'index.html', {'num':sentence}
    )
    