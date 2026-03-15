perc = int(input('Enter percentage:'))
if(perc >= 91 and perc <= 100):
    print('Grade: A')
elif(perc >= 76 and perc <= 90):
    print('Grade: B')
elif(perc >= 61 and perc <= 75):
    print('Grade: C')
elif(perc >= 41 and perc <= 60):
    print('Grade: D')
elif(perc >= 0 and perc <= 40):
    print('Grade: Fail')
else:
    print('Invalid percentage')