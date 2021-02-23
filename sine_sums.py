from manim import *
import numpy as np
from lib.tri_sum_scene import TrigSumScene

number_of_terms = 20


class Saw(TrigSumScene):
    def __init__(self, **kwargs):
        super().__init__(number_of_terms=number_of_terms, **kwargs)

    def construct(self):
        super().construct()


class Pulse(TrigSumScene):
    def __init__(self, **kwargs):
        super().__init__(number_of_terms=number_of_terms, **kwargs)

    def construct(self):
        super().construct()

    def get_func_at(self, index):
        return lambda x: (4.0 / np.pi) * (1.0 / (2*index - 1)) * np.sin((2*index-1) * x)

    def get_tex_at(self, index):
        return MathTex(r"f_{"+str(index)+"}(x) = {4 \over \pi} \sum^{"+str(index)+"}_{k=1}{1 \over (2k - 1)} \sin((2k - 1) \cdot x)")


class Tri(TrigSumScene):
    def __init__(self, **kwargs):
        super().__init__(number_of_terms=number_of_terms, **kwargs)

    def construct(self):
        super().construct()

    def get_func_at(self, index):
        return lambda x: 8.0 / (np.pi**2) * (((-1.0)**(index-1)) / (2*index - 1)**2) * np.sin((2*index-1) * x)

    def get_tex_at(self, index):
        return MathTex(r"f_{"+str(index)+"}(x) = {8 \over \pi^2} \sum^{"+str(index)+"}_{k=1}{(-1)^{k-1} \over (2k - 1)^2} \sin((2k - 1) \cdot x)")
