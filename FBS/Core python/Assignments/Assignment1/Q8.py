#write a program to convert days into years,weeks and days.

days = int(input("Enter number of days:")) # 800 days
years = days // 365  # 800 // 365 = 2 years
days = days % 365  # 2* 365 = 730 days used , 800 - 730 = 70 days remaining
weeks = days // 7  # 70 // 7 = 10 
days = days % 7    # 70 % 7 = 0 days
print("Years:",years)
print("Weeks:",weeks)
print("Days:",days)