class Instructor:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def writeonboard(self,markerobj):
        print(f'inser. {self.name} using marker {markerobj.color}')
