  
def reset_log(val):
    f=open("reset_log.txt", "r")
    cycles=f.read()
    f.close()
    f=open("reset_log.txt", "w")
    if val=='0' or cycles=='None':
        f.write('0')
        f.close()
    else:
        f.write(str(int(cycles)+int(val)))
        count=int(cycles)+int(val)
        print('Program has been reset '+str(int(cycles)+int(val))+' times')
        f.close()
