for i in range(1,10):
    for j in range(1,10):
        print ('{0:2>}{1:03x}  '.format("0x",i * j), end="")
    print('')
