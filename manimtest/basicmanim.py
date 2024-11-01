#!manim -qh
import manim as m

class FirstScene(m.Scene):
    def construct(self):
        square = m.Square(color = m.GREEN)
        circle = m.Circle(color = m.RED)
        self.play(m.Transform(square,circle))
        self.play(m.Transform(square,circle))
        ax = m.Axes()
        ax.add_coordinates()
        cu = lambda x:x**2
        
        self.play(m.FadeIn(ax),m.FadeIn(ax.plot(cu)))