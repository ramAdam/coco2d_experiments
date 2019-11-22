import cocos 
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite
from loader.animations import grossini, palletBg
from pyglet.window import mouse

class HelloWorld(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.sprite = Sprite(grossini, anchor=(0, 0))
        self.palletbg = Sprite(palletBg, anchor=(0, 0))

        self.sprite.position = 320, 100
        self.palletbg.position = 320, 100
        
        self.sprite.scale = 3


        
        self.add(self.palletbg, z=0)
        self.add(self.sprite, z=1)
        self.spriteClicked = False
        
        
        self.schedule(self._update)


    def _update(self, dt):
        pass

    def mouse_on_sprite(self, x, y):
        if (x < self.sprite.x + self.sprite.width) and (x > self.sprite.x) and (y < self.sprite.y + self.sprite.height) and (y > self.sprite.y):
            return True
        return False

    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            if self.mouse_on_sprite(x, y):
                self.spriteClicked = True

    def on_mouse_release(self, x, y, button, modifiers):
        self.spriteClicked = False


    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button & mouse.LEFT and self.spriteClicked:
            self.sprite.x +=  dx
            self.sprite.y += dy

    def on_mouse_motion(self, x, y, dx, dy):
        cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_HAND)
            director.window.set_mouse_cursor(cursor)

        director.window.set_mouse_cursor(cursor)

if __name__ == "__main__":

    director.init(width=1020, height=720)
    director.window.pop_handlers()

    hello_layer = HelloWorld()

    
    main_scene = cocos.scene.Scene(hello_layer)

    cocos.director.director.run(main_scene)


