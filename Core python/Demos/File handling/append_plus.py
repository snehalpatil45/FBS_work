with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/File handling/demo.txt','a+') as fp:
    print('courser:',fp.tell())
    fp.seek(0,0)
    print('content:',fp.read())
    fp.write('\nThis is next line')
    fp.seek(0,0)
    print('content:',fp.read())