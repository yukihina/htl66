init python:
    import math
    import time

    class AnimatedWave(renpy.Displayable):
        def __init__(self, child, wave_amplitude=10, wave_frequency=0.05, wave_speed=45, **properties):
            super(AnimatedWave, self).__init__(**properties)
            self.child = renpy.displayable(child)
            self.wave_amplitude = wave_amplitude
            self.wave_frequency = wave_frequency
            self.wave_speed = wave_speed
            self.start_time = time.time()  

        def render(self, width, height, st, at):
            current_time = time.time()
            self.st = (current_time - self.start_time) * self.wave_speed

            child_render = renpy.render(self.child, width, height, st, at)
            cwidth, cheight = int(child_render.get_size()[0]), int(child_render.get_size()[1])
            render = renpy.Render(cwidth, cheight)

            for x in range(cwidth):
                wave_offset = int(self.wave_amplitude * math.sin(self.st + x * self.wave_frequency))
                column = child_render.subsurface((x, 0, 1, cheight))
                render.blit(column, (x, wave_offset))

            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [self.child]