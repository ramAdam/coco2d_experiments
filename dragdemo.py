import cocos 
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite
from loader.animations import grossini, palletBg
from pyglet.window import mouse

from editor.components import Pallet

import pdb

class PalletLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()
        self.sprite = Sprite(grossini, anchor=(0, 0))
       

        self.pallet = Pallet(x=800, y=700)
        self.pallet._addItems(self, 5)
                        
        
        self.spriteClicked = False
        
       
        self.schedule(self._update)
        

    def _update(self, dt):
        pass

    def mouse_on_sprite(self, x, y):
        for sprite in self.get_children():
            if sprite.contains(x, y):
                self.selectedSprite = sprite
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
            self.selectedSprite.x +=  dx
            self.selectedSprite.y += dy

    def on_mouse_motion(self, x, y, dx, dy):
        cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_DEFAULT)
        if self.mouse_on_sprite(x, y):
            cursor = director.window.get_system_mouse_cursor(director.window.CURSOR_HAND)
            director.window.set_mouse_cursor(cursor)

        director.window.set_mouse_cursor(cursor)

  
if __name__ == "__main__":

    director.init(width=1200, height=800)
    director.window.pop_handlers()

    hello_layer = PalletLayer()
    main_scene = cocos.scene.Scene(hello_layer)
    cocos.director.director.run(main_scene)

    



