from pyglet import resource

resource.path = ['./asset']
resource.reindex()


nick = dict(walk=resource.animation('nick_walk.gif'),
            shoot=resource.animation('nick_shoot.gif'),
            idle=resource.animation('nick_fury_stand.gif') 
)
background = resource.image('background.png')
stage2 = resource.image('Stage1-2.png')

kitten = resource.image("kitten.png")
scrlbg = resource.image("bg2Scrollable.jpg")
cross = resource.image("cross.png")

grass_down = resource.image("grass_down.png")
grass_up = resource.image("grass_up.png")

grossini = resource.image("grossini.png")