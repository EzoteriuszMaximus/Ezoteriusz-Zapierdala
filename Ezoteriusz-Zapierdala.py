ezoter = Actor('ezoteriusz')
ezoter.pos = 0, 398

WIDTH = 640
HEIGHT = 480

def draw():
    screen.clear()
    ezoter.draw()


def update():
    ezoter.left += 10

    if ezoter.left > WIDTH:
        ezoter.right = 0

def on_mouse_down(pos):
    if ezoter.collidepoint(pos):
        set_ezoter_hurt()
    else:
        sounds.typacanie.play()

def set_ezoter_hurt():
    ezoter.image = 'ezoteriusz_hurt'
    sounds.spadajszczawiu.play()
    clock.schedule_unique(set_ezoter_normal, 1.8)

def set_ezoter_normal():
    ezoter.image = 'ezoteriusz'






