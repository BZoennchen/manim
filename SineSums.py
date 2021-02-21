from manim import *
import numpy as np


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class Sines(GraphScene):
    def __init__(self, **kwargs):
        super().__init__(
            x_min=0, 
            x_max=2*np.pi, 
            x_axis_width=2*np.pi,
            #include_tip=True,
            graph_origin=ORIGIN + LEFT * 4,
            y_min=-2.5,
            y_max=2.5,
            x_axis_config={"tick_frequency": 1.0/2.0 * np.pi, "decimal_number_config": {"num_decimal_places": 2}},
            x_labeled_nums=np.arange(0, 2*np.pi, 1.0/2.0*np.pi),
            y_labeled_nums=[-2.0,-1.0,0,1.0,2.0],
            **kwargs)

    def construct(self):
        n = 20
        snsBlue = '#4c72b0'
        snsOrange = '#dd8452'
        #self.play(Write(text))
        #self.add_x_labels()
        self.setup_axes(animate=True)

        sineSum1 = self.get_graph(
                self.fSine(1),
                color=snsBlue,
                step_size=0.001)

        sine2 = self.get_graph(
                self.fSine(2),
                color=snsOrange,
                step_size=0.001)
        
        sineSum2 = self.get_graph(
                self.fSineSum(2),
                color=snsBlue,
                step_size=0.001)

        text=MathTex(r"f_", r"{1}", r"(x) = ", r"\sum^{",r"{1}",r"}_{{k=1}}",r"{1 \over k} \sin(k \cdot x).")
        text.set_color(snsBlue)
        #text[1].set_color(RED)
        #text[3].set_color(RED)
        text.to_corner(UP)  
        self.play(Write(text))
        self.play(ShowCreation(sineSum1))
        self.wait(0.5)
        
        for i in range(2, n):
            textrep = MathTex(r"f_", "{"+str(i)+"}", r"(x) = ", r"\sum^{","{"+str(i)+"}",r"}_{{k=1}}",r"{1 \over k} \sin(k \cdot x).")
            textrep.set_color(snsBlue)
            textrep.move_to(text)
            #textrep[1].set_color(RED)
            #textrep[3].set_color(RED)

            group = Group(sineSum1, sine2)
            self.play(ShowCreation(sine2))
            self.play(
                ReplacementTransform(group, sineSum2),
                ReplacementTransform(text, textrep))

                #ReplacementTransform(Group(text[1], text[3]), Group(textrep[1], textrep[3])))

            sineSum1 = sineSum2
            text = textrep

            sine2 = self.get_graph(
                self.fSine(i+1),
                color=snsOrange,
                step_size=0.001)

            sineSum2 = self.get_graph(
                self.fSineSum(i+1),
                color=snsBlue,
                step_size=0.001)

    def add_x_labels(self):
        x_labels = [
            MathTex("\\frac{1}{2}\pi"), MathTex("\pi"),
            MathTex("\\frac{3}{2}\pi"), MathTex("2\pi")
        ]

        #np.array([-1 + i, 0, 0])
        for i in range(len(x_labels)):
            # i dont unstand yet how the distance is computed
            x_labels[i].next_to(np.array(self.graph_origin + [2.25 * (i+1), 0, 0]), DOWN)
            self.add(x_labels[i])

    def fSineSum(self, k):
        def sineSum(x):
            s = 0
            for i in range(1,k+1):
                s = s + self.fSine(i)(x)
            return s
        return sineSum
            
    def fSine(self, k):
        def sine(x):
            return 1.0 / k * np.sin(k * x)
        return sine