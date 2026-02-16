# convert the time entered in hh,min and sec into seconds.

hr = int(input("Enter Hour:"))
min = int(input("Enter minute:"))
sec = int(input("Enter second:"))
total_sec = (hr * 3600) + (min * 60) + sec
print("Total second:", total_sec)