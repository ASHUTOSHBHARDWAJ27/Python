from direct.showbase.ShowBase import ShowBase
from math import cos,sin
class panda(ShowBase):
    def __init__(self):
        super().__init__()
        self.cam.setPos(0,-30,0)
        self.panda=self.loader.loadModel("models/panda")
        self.panda.setScale(0.5,0.5,0.5)
        self.panda.setPos(0,50,0)
        self.panda.reparentTo(self.render)
        self.x=0
        self.angle=0
        self.speed=2  
        
        self.taskMgr.add(self.update,"update")  
    def update(self,task):
        
        dt= globalClock.getDt()
        self.panda.setPos(cos(self.x)*4,sin(self.x)*4,0)
        self.panda.setH(self.angle)
        
        self.angle += 5
        self.x += self.speed * dt
        return task.cont

panda=panda()
panda.run()