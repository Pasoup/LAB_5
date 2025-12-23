import turtle as t

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width


    def showdisk(self):
        t.teleport(self.dxpos, self.dypos)
        t.begin_fill()
        t.back(self.dwidth / 2)
        for _ in range(2):
            t.forward(self.dwidth)
            t.left(90)
            t.forward(self.dheight)
            t.left(90)
        t.forward(self.dwidth / 2)
        t.end_fill()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        t.clear()
        t.teleport(self.dxpos, self.dypos)


sm = Disk("",100,20,80,140)
sm.showdisk()

sm.cleardisk()

t.done()