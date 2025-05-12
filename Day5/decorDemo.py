def notifiy(funname):
    def wrapper():
        f=open('notitg.txt','w')
        f.write(f'{funname} called')
        f.close()
        funname()
        print('hi notifiy')
@notifiy()
def test():
    print('test')
@notifiy()
def test():
    print('test')