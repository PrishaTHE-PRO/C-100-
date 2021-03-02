class Car (object):
    def __init__ (self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start (self):
        print('started')

    def stop (self):
        print('stopped') 

    def accelerate (self):
        print('accelerate') 

    def change_gear (self):
        print('gear changed')   

audi=Car('A5','white','audi',200)  

print(audi.start())
print(audi.stop())
print(audi.accelerate())
print(audi.change_gear())