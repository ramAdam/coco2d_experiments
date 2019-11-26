from cocos.sprite import Sprite
from loader.animations import grossini, palletBg


class Rectangle:
    def __init__(self, x, y):
        pass


class PalletItem(Sprite):
    def __init__(self, **kwargs):
        super().__init__(anchor = (0, 0), **kwargs)
        # self.anchor = (0, 0)

    def contains(self, x, y):
        if (x < self.x + self.width) and (x > self.x) and (y < self.y + self.height) and (y > self.y):
            return True
        return False
        

class Pallet:
    def __init__(self, x, y):
        # super().__init__(**kwargs)
        self.x = x
        self.y = y
        # self.layer = layer
        # self.layer.add(self)
        self.spr = PalletItem(image=grossini)
        self.writeX = self.x + 10
        self.writeY = self.y - self.spr.height
        

    def _addItems(self, layer, num):
        for i in range(num):
            spr = PalletItem(image=self.spr.image)
            spr.position = self.writeX, self.writeY
            spr.scale = 1.5
            layer.add(spr)
            self.writeY -= spr.height + 10
    
   
        