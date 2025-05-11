from Instructor import Instructor
class Room:
    def __init__(self,number,seats,w,w,):
        self.number=number
        self.counts=seats
        self.wall=[]
        self.insr=None
    def enterroom(self,objectinsr):
        self.insr=objectinsr
        print('inst. enter Lec')
    def exsitromm(self):
        self.insr=None