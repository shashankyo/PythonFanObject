class Fan:
    def __init__(self,brand,cost,color):
        self.brand = brand
        self.cost = cost 
        self.color = color

    def start(self):
        print("fan starts") 

    def rotate(self):
        print("fan rotates") 


    def blowsair(self):
        print("fan blows air")

    f = Fan("usha",1500, "white")
    print(f.brand,f.cost,f.color)
    f.start()
    f.rotate()
    f.blowsair()
