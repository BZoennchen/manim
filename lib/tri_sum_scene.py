from manim import *
import numpy as np
from typing_extensions import runtime
from .tri_scene import TrigScene


class TrigSumScene(TrigScene):
    def __init__(self, number_of_terms=5, text_scale=0.7, wait_time=0.25, runtime=0.5, **kwargs):
        super().__init__(**kwargs)
        self.index = 1
        self.text_scale = text_scale
        self.number_of_terms = number_of_terms
        self.term_color = WHITE
        self.sum_color = YELLOW
        self.wait_time = wait_time
        self.runtime = runtime

    def construct(self):
        self.show_axis(animate=True)
        text = self.get_tex()
        self.play(Write(text))

        sumGraph = self.get_graph(self.get_func())
        sumGraph.set_color(self.sum_color)
        self.play(ShowCreation(sumGraph), runtime=self.runtime)

        for j in range(2, self.number_of_terms):
            self.next()
            termGraph = self.get_graph(self.get_func())
            termGraph.set_color(self.term_color)
            self.play(ShowCreation(termGraph), runtime=self.runtime)
            self.wait(self.wait_time)

            nextSumGraph = self.get_graph(self.get_sum_func())
            nextSumGraph.set_color(self.sum_color)
            nextText = self.get_tex()

            self.play(
                ReplacementTransform(
                    VGroup(sumGraph, termGraph), nextSumGraph),
                ReplacementTransform(text, nextText),
                runtime=self.runtime)
            self.wait(self.wait_time)

            sumGraph = nextSumGraph
            text = nextText

    def show_initial_graph(self):
        graph1 = self.get_graph(self.get_func())
        self.play(ShowCreation(graph1))
        self.wait(0.5)

    def get_tex_at(self, index):
        return MathTex(r"f_{"+str(index)+"}(x) = {2 \over \pi} \sum^{"+str(index)+"}_{k=1}{(-1)^{(k-1)} \over k} \sin(k \cdot x)")

    def get_tex(self):
        text = self.get_tex_at(self.index)
        text.to_corner(UP)
        text.scale(self.text_scale)
        text.set_color(self.sum_color)
        return text

    def get_func(self):
        return self.get_func_at(self.index)

    def get_func_at(self, index):
        return lambda x: (2.0 / np.pi) * (1.0 / index) * np.sin(index * x)

    def get_sum_func_at(self, index):
        def sum_func(x):
            s = 0
            for j in range(1, index+1):
                s = s + self.get_func_at(j)(x)
            return s
        return sum_func

    def get_sum_func(self):
        return self.get_sum_func_at(self.index)

    def next(self):
        self.index = self.index + 1
