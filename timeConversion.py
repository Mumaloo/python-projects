def timeConversion(s):
    hour = int(s[0:2]) 
    if hour == 12:
        if s[-2] == "A":
            hour = '0' + '0'
    elif s[-2] == "P": 
        hour = hour + 12
    if hour < 10:
        hour = '0' + str(hour)
    hour = str(hour)
    conv = s.replace(s[0:2], hour, 1)
    army = conv.rstrip(s[-2:])
    print army

print timeConversion('07:07:45PM')
print timeConversion('12:00:00AM')
print timeConversion('12:00:00PM')
print timeConversion('06:40:03AM')