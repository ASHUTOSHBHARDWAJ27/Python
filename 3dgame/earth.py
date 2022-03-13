from direct.showbase.ShowBase import ShowBase

class earth(ShowBase):
    def __init__(self):
        super().__init__()
        self.cam.setPos(0,-30,0)
        self.set_background_color(0,0,0,1)
    
        self.tex=self.loader.loadTexture("world.jpg")
        self.earth=self.loader.loadModel("models/sphere")
        self.earth.setTexture(self.tex)
        self.earth.setScale(5,5,5)
        self.earth.reparentTo(self.render)

        self.angle=0
        self.speed=2  
        
        self.taskMgr.add(self.update,"update")  

    def update(self,task):
        
        ft= globalClock.getFrameTime()
        self.earth.setH(self.angle)
        self.angle += self.speed * 1
        
        return task.cont

earth=earth()
earth.run()