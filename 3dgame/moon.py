from panda3d.core import PointLight,AmbientLight
from direct.showbase.ShowBase import ShowBase
from math import cos,sin
class moon(ShowBase):
    def __init__(self):
        super().__init__()
        self.cam.setPos(0,-30,0)
        self.set_background_color(0,0,0,1)

        self.moon = self.loader.loadModel("models/sphere")
        self.moon.setScale(3,3,3)
        self.moon.reparentTo(self.render)
        

        self.tex=self.loader.loadTexture("world.jpg")
        self.earth=self.loader.loadModel("models/sphere")
        self.earth.setTexture(self.tex)
        self.earth.setScale(5,5,5)
        self.earth.reparentTo(self.render)

        plight = PointLight("plight")
        plight.setColor((1,1,1,1))
        self.plnp=self.moon.attachNewNode(plight)
        self.earth.setLight(self.plnp)

        alight=AmbientLight("alight")
        alight.setColor((0.8,0.8,0.8,1))
        self.alnp = self.render.attachNewNode(alight)
        self.earth.setLight(self.alnp)

        self.angle=0
        self.speed=2  
        
        self.taskMgr.add(self.update,"update")  

    def update(self,task):
        
        ft= globalClock.getFrameTime()

        self.moon.setPos(cos(ft)*13,sin(ft)*14,cos(ft)*3)
        self.earth.setH(self.angle)
        self.angle += self.speed * 2
        
        return task.cont

moon=moon()
moon.run()