with open('C:/Users/ASUS/Desktop/FBS/Core python/Demos/File handling/demo.txt','w+') as fp:
    print('courser:',fp.tell())
    fp.write('this is first line')
    fp.seek(0,0)
    content = fp.read()
    print('content:',content)