from manim import *
import numpy as np

class Pulse(GraphScene):
    def __init__(self, **kwargs):
        super().__init__(
            x_min=0, 
            x_max=2*np.pi, 
            x_axis_width=2*np.pi,
            #include_tip=True,
            graph_origin=ORIGIN + LEFT * 4,
            y_min=-1.5,
            y_max=1.5,
            x_axis_config={"tick_frequency": 1.0/2.0 * np.pi, "decimal_number_config": {"num_decimal_places": 2}},
            x_labeled_nums=np.arange(0, 2*np.pi, 1.0/2.0*np.pi),
            y_labeled_nums=[-2.0,-1.0,0,1.0,2.0],
            **kwargs)

    def construct(self):
        n = 5
        scale = 0.7
        snsBlue = '#4c72b0'
        snsOrange = '#dd8452'
        sumColor = YELLOW
        funcColor = WHITE
        #self.play(Write(text))
        #self.add_x_labels()
        self.setup_axes(animate=True)

        sineSum1 = self.get_graph(
                fSine(1, 4.0/np.pi),
                color=sumColor,
                step_size=0.001)

        sine2 = self.get_graph(
                fSine(3,4.0/np.pi),
                color=funcColor,
                step_size=0.001)
        
        sineSum2 = self.get_graph(
                fSineSum(3,4.0/np.pi,2),
                color=sumColor,
                step_size=0.001)

        text=MathTex(r"f_", r"{1}", r"(x) = ", r"{4 \over \pi} \sum^{",r"{0}",r"}_{{k=1}}",r"{1 \over (2k - 1)} \sin((2k - 1) \cdot x)")
        text.set_color(sumColor)
        text.scale(scale)
        #text[1].set_color(RED)
        #text[3].set_color(RED)
        text.to_corner(UP)  
        self.play(Write(text))
        self.play(ShowCreation(sineSum1))
        self.wait(0.5)
        
        for i in range(2, n):
            textrep = MathTex(r"f_", "{"+str(i)+"}", r"(x) = ", r"{4 \over \pi} \sum^{","{"+str(i)+"}",r"}_{{k=1}}",r"{1 \over (2k - 1)} \sin\left((2k - 1) \cdot x\right)")
            textrep.set_color(sumColor)
            textrep.scale(scale)
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
                fSine(2*i+1,4.0/np.pi),
                color=funcColor,
                step_size=0.001)

            sineSum2 = self.get_graph(
                fSineSum(2*i+1,4.0/np.pi,2,False),
                color=sumColor,
                step_size=0.001)

class Saw(GraphScene):
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
        n = 10
        a = 2.0 / np.pi
        snsBlue = '#4c72b0'
        snsOrange = '#dd8452'
        sumColor = YELLOW
        funcColor = WHITE
        #self.play(Write(text))
        #self.add_x_labels()
        self.setup_axes(animate=True)

        sineSum1 = self.get_graph(
                fSine(1,a,0),
                color=sumColor,
                step_size=0.001)

        sine2 = self.get_graph(
                fSine(2,a,np.pi),
                color=funcColor,
                step_size=0.001)
        
        sineSum2 = self.get_graph(
                fSineSum(2,a,1,True),
                color=sumColor,
                step_size=0.001)

        text=MathTex(r"f_", r"{1}", r"(x) = ", r"{2 \over \pi} \sum^{",r"{1}",r"}_{{k=1}}",r"{(-1)^{(k-1)} \over k} \sin(k \cdot x)")
        text.set_color(sumColor)
        #text[1].set_color(RED)
        #text[3].set_color(RED)
        text.to_corner(UP)  
        self.play(Write(text))
        self.play(ShowCreation(sineSum1))
        self.wait(0.5)
        
        for i in range(2, n):
            textrep = MathTex(r"f_", "{"+str(i)+"}", r"(x) = ", r"{2 \over \pi} \sum^{","{"+str(i)+"}",r"}_{{k=1}}",r"{(-1)^{(k-1)} \over k} \sin(k \cdot x)")
            textrep.set_color(sumColor)
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
                fSine(i+1,a,(i % 2) * np.pi),
                color=funcColor,
                step_size=0.001)

            sineSum2 = self.get_graph(
                fSineSum(i+1,a,1,True),
                color=sumColor,
                step_size=0.001)

class Tri(GraphScene):
    def __init__(self, **kwargs):
        super().__init__(
            x_min=0, 
            x_max=2*np.pi, 
            x_axis_width=2*np.pi,
            #include_tip=True,
            graph_origin=ORIGIN + LEFT * 4,
            y_min=-1.5,
            y_max=1.5,
            x_axis_config={"tick_frequency": 1.0/2.0 * np.pi, "decimal_number_config": {"num_decimal_places": 2}},
            x_labeled_nums=np.arange(0, 2*np.pi, 1.0/2.0*np.pi),
            y_labeled_nums=[-2.0,-1.0,0,1.0,2.0],
            **kwargs)

    def construct(self):
        n = 10
        scale = 0.7
        a = 8.0/(np.pi * np.pi)
        snsBlue = '#4c72b0'
        snsOrange = '#dd8452'
        sumColor = YELLOW
        funcColor = WHITE
        #self.play(Write(text))
        #self.add_x_labels()
        self.setup_axes(animate=True)

        sineSum1 = self.get_graph(
                fSineTri(1,a,0),
                color=sumColor,
                step_size=0.001)

        sine2 = self.get_graph(
                fSineTri(3,a,np.pi),
                color=funcColor,
                step_size=0.001)
        
        sineSum2 = self.get_graph(
                fSineSumTri(3,a,2),
                color=sumColor,
                step_size=0.001)

        text=MathTex(r"f_", r"{1}", r"(x) = ", r"\sum^{",r"{1}",r"}_{{k=1}}",r"{(-1)^{(k-1)} \over (2k - 1)^2} \sin((2k - 1) \cdot x)")
        text.scale(scale)
        text.set_color(sumColor)
        #text[1].set_color(RED)
        #text[3].set_color(RED)
        text.to_corner(UP)  
        self.play(Write(text))
        self.play(ShowCreation(sineSum1))
        self.wait(0.5)
        
        for i in range(2, n):
            textrep = MathTex(r"f_", "{"+str(i)+"}", r"(x) = ", r"\sum^{","{"+str(i)+"}",r"}_{{k=1}}",r"{(-1)^{k-1} \over (2k - 1)^2} \sin\left((2k - 1) \cdot x\right)")
            textrep.scale(scale)
            textrep.set_color(sumColor)
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
                fSineTri(2*i+1,a,(i % 2) * np.pi),
                color=funcColor,
                step_size=0.001)

            sineSum2 = self.get_graph(
                fSineSumTri(2*i+1,a,2),
                color=sumColor,
                step_size=0.001)

def fSineSum(k,a=1,step=1,phaseShift=False,phase=0):
    def sineSum(x):
        s = 0
        mPhase = phase
        for i in range(1,k+1,step):
            s = s + fSine(i,a,mPhase)(x)
            if mPhase == 0 and phaseShift:
                mPhase = np.pi
            else:
                mPhase = 0
        return s
    return sineSum

def fSine(k,a=1,phase=0):
    def sine(x):
        return a * 1.0 / k * np.sin(phase + k * x)
    return sine

def fSineSumTri(k,a=1,step=1):
    def sineSum(x):
        s = 0
        phase = 0
        for i in range(1,k+1,step):
            s = s + fSineTri(i,a,phase)(x)
            if phase == 0:
                phase = np.pi
            else:
                phase = 0
        return s
    return sineSum

def fSineTri(k,a=1,phase=0):
    def sine(x):
        return a * 1.0 / (k*k) * np.sin(phase + k * x)
    return sine

