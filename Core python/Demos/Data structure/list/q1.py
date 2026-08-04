loc = ['s1','s2','s3','s4','s5','s6']
dist = [1500,3700,5300,2900,2800,4300]
def p_calculation(source,destination,price):
    start = loc.index(source)
    end = loc.index(destination)
    total = 0
    while(start != end):
        total = total + dist[start]
        start = (start + 1) % 6
    km = total/1000
    cost = km * price
    print(f'Distance:{total} m')
    print(f'cost:{cost} rs')

source = input('Enter source(s1-s6):')
destination = input('Enter destination(s1-s6):')
price = int(input('Enter price per km:'))
p_calculation(source,destination,price)