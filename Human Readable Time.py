"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format
(HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    hour = seconds // 3600
    hourList = [hour]
    minutes = (seconds % 3600) // 60
    minutesList = [minutes]
    sec = (seconds % 3600) % 60
    secList = [sec]

    if hourList[0] < 10:
        hourList.insert(0,0)
    for i in range(0, len(hourList)):
        hourList[i] = str(hourList[i])
    hourList = "".join(hourList)

    if minutesList[0] < 10:
        minutesList.insert(0,0)
    for i in range(0, len(minutesList)):
        minutesList[i] = str(minutesList[i])
    minutesList = "".join(minutesList)

    if secList[0] < 10:
        secList.insert(0,0)
    for i in range(0, len(secList)):
        secList[i] = str(secList[i])
    secList = "".join(secList)

    return hourList + ":" + minutesList + ":" + secList


#MAIN
print(make_readable(5))