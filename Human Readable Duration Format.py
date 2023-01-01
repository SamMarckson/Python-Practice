"""
TITLE: Human Readable Duration Format
SOURCE: https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is
expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:
* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it
should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute
and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more
significant unit of time.

"""


def format_duration(seconds):

    if seconds == 0: #EXCESSÃO 1
        return 'now'

    years = seconds // 31536000         #31536000 é a qtd de segundos em 1 ano
    days = (seconds % 31536000) // 86400            #86400 é a qtd de segundos em 1 dia
    hour = ((seconds % 31536000) % 86400) // 3600
    #hour = seconds // 3600
    minutes = (((seconds % 31536000) % 86400) % 3600) // 60
    #minutes = (seconds % 3600) // 60
    secs = (((seconds % 31536000) % 86400) % 3600) % 60
    #secs = (secs % 3600) % 60

    cont = 0

    listaDoTempo = []
    listaDasStringsSing = ['year', 'day', 'hour', 'minute', 'second']
    listaDasStringsPlural = ['years', 'days', 'hours', 'minutes', 'seconds']
    listaFinal = []


    listaDoTempo.append(years)
    listaDoTempo.append(days)
    listaDoTempo.append(hour)
    listaDoTempo.append(minutes)
    listaDoTempo.append(secs)

    #print(listaDoTempo)

    for elemento in listaDoTempo[:]:
        if elemento != 0:
            cont += 1
        if cont == 2:
            break

    for i in range(0, len(listaDoTempo)):
        listaDoTempo[i] = str(listaDoTempo[i])
    # print(listaDoTempo)

    if cont == 2:
        for x in range(len(listaDoTempo)-1, -1, -1):
            if listaDoTempo[x] != '0':
                listaDoTempo[x] = 'and ' + listaDoTempo[x]
                break

    #print(f"LISTA DO TEMPO = {listaDoTempo}")

    for j in range(0, len(listaDoTempo)):
        if listaDoTempo[j] == '1':
            listaFinal.append(listaDoTempo[j] + " " + listaDasStringsSing[j])
        elif listaDoTempo[j] == 'and 1':
            listaFinal.append(listaDoTempo[j] + " " + listaDasStringsSing[j])
        elif listaDoTempo[j] != '0' and listaDoTempo[j] != '1' and listaDoTempo[j] != 'and':
            listaFinal.append(listaDoTempo[j] + " " + listaDasStringsPlural[j])

    # print(listaFinal)
    # print(len(listaFinal))
    # print(listaFinal[0])

    if len(listaFinal) > 1:
        for i in range(0, len(listaFinal)-2):
            listaFinal[i] += ','
    # print(listaFinal)


    listaFinal = " ".join(listaFinal)
    return listaFinal


#MAIN
#format_duration(62)
#format_duration(3662)
#format_duration(60)
#print(format_duration(120))
#print(format_duration(0))
# print(format_duration(132030240))
print(format_duration(253374061))