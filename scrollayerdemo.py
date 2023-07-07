import cocos
from cocos.director import director
from loader.animations import *
from cocos.sprite import Sprite
from cocos.layer import ScrollingManager, ScrollableLayer
from cocos.text import Label
from pyglet.window import key
import pyglet
import pdb


class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)

        vel_x = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 500 
        vel_y = (keyboard[key.UP] - keyboard[key.DOWN]) * 500 
        self.target.velocity = (vel_x, vel_y)
        scroller.set_focus(self.target.x, self.target.y)

class KittenLayer(cocos.layer.ScrollableLayer):
    
    def __init__(self, parallax):
        super().__init__(parallax)
        cat = Sprite(kitten)
        cat.velocity = (0, 0)

        cat.do(Mover())
        self.add(cat)
class BackgroundLayer(cocos.layer.ScrollableLayer):
    def __init__(self, parallax):
        super().__init__(parallax)
        bg = Sprite(scrlbg)
        grass_d = Sprite(grass_down)
        
        grs_u = Sprite(grass_up)

        grass_d.position = bg.width/2, bg.height/2
        grs_u.position = bg.width/2, bg.height/2


        self.px_width = bg.width
        self.px_height = bg.height

        self.add(grass_d, z=2)
        self.add(grs_u, z=1)

class CrossLayer(cocos.layer.ScrollableLayer):
    def __init__(self, parallax):
        super().__init__(parallax)
        crs = Sprite(cross)
        crs.position = 500, 500
        grs_up = Sprite(grass_up)
        grs_up.position = 500, 300

        self.add(crs)
        self.add(grs_up)


if __name__ == "__main__":
   
    global scroller
    director.init(width=1280, height=720, caption="parllax scroll demo")
    director.window.pop_handlers()
    
    scroller = ScrollingManager()

    bg = BackgroundLayer(.5)
    scroller.add(bg)

    fg = KittenLayer(1)
    scroller.add(fg)

    crossLayer = CrossLayer(parallax=1.5)
    scroller.add(crossLayer)



    keyboard = key.KeyStateHandler()
    director.window.push_handlers(keyboard)

    # def update(dt):
    #     scroller.fx += (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 150 * dt
    #     scroller.fy += (keyboard[key.DOWN] - keyboard[key.UP]) * 150 * dt
        # pdb.set_trace()
        # scroller.set_focus(k.x, k.y)

    scene = cocos.scene.Scene(scroller)
    # scene.schedule(update)
    director.run(scene)


