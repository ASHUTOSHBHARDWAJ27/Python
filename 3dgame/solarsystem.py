from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight , AmbientLight
from direct.filter.CommonFilters import CommonFilters
from math import cos,sin
class solarsystem(ShowBase):
    def __init__(self):
        super().__init__()
        self.cam.setPos(0,-30,0)
        self.setBackgroundColor(0,0,0,1)

        self.sun=self.loader.loadModel("sphere")
        self.sun.setScale(4,4,4)
        self.sun.setColor(0.9,0.9,0,0)
        self.sun.reparentTo(self.render) 
        
        self.tex=self.loader.loadTexture("world.jpg")
        self.earth=self.loader.loadModel("models/sphere")
        self.earth.setTexture(self.tex)
        self.earth.setScale(1,1,1)
        # self.earth.setPos(0,50,0)
        self.earth.reparentTo(self.render)
              
        sunplight = PointLight("sunplight")
        sunplight.setColor((1,1,1,1))
        # sunplight.attenuation = (1, 1, 1)
        self.sunplnp = self.sun.attachNewNode(sunplight)
        self.earth.setLight(self.sunplnp)
        sunplight.setShadowCaster(True, 512, 512)
        render.setShaderAuto()

        sunalight = AmbientLight("sunalight")
        sunalight.setColor((0.9,0.9,0.9,1))
        self.sunalnp = self.sun.attachNewNode(sunalight)
        self.earth.setLight(self.sunalnp) 

        filters = CommonFilters(self.win, self.cam)
        filters.setBloom(size="large")
       
        self.x=0
        self.speed=1
        self.angle=0
    
        self.taskMgr.add(self.update,"update")

    def update(self,task):
        dt=globalClock.getDt()
        
        self.earth.setPos(cos(self.x)*8,sin(self.x)*4,cos(self.x)*2)
          
        self.earth.setH(self.angle)
        self.x += self.speed * dt

        self.angle +=2
        self.x += self.speed * dt
        return task.cont

solarsystem=solarsystem()
solarsystem.run()

