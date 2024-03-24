class Player():
   
    
    def __init__(self,name,height,foot,speed,acc,con,sho,dri,pas):
        self.name=name
        self.height=height
        self.foot=foot
        self.speed=speed
        self.acceleration=acc
        self.control=con
        self.shooting=sho
        self.dri=dri
        self.passing=pas
        
        
        
    def show(self):
        print("name:",self.name,"height:",self.height,"foot:",self.foot,"speed",self.speed,"acceleration:",self.acceleration,
              "control:",self.control,"shooting:",self.shooting,"dribble:",self.dri,"passing:",self.passing)
    
        
playerX=Player("Lukaku","192","L","72","80","82","90","85","70")
playerX.show()       
players=Player("Messi","171","L","85","85","98","92","90","90")
players.show() 
 