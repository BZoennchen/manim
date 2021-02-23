from manim import *
import numpy as np


class TrigScene(Scene):
    def __init__(self,
                 x_min=-0.5,
                 x_max=np.pi * 2 + 0.5,
                 y_min=-1.5,
                 y_max=1.5,
                 x_ticks=[np.pi * 0.5, np.pi, 3.0 / 2.0 * np.pi, 2 * np.pi],
                 x_tick_labels=[MathTex("{1 \over 2} \pi"),
                                MathTex("\pi"), MathTex("{3 \over 2} \pi"), MathTex("2 \pi")],
                 y_ticks=[-1, 1],
                 y_tick_labels=[
                     MathTex("-1"), MathTex("1")],
                 x_axis_scale=1.5,
                 y_axis_scale=2,
                 axis_color=GRAY,
                 tick_labels_color=WHITE,
                 ** kwargs):
        super().__init__(**kwargs)
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.axis_color = axis_color
        self.tick_labels_color = tick_labels_color
        self.x_ticks = x_ticks
        self.x_tick_labels = x_tick_labels
        self.y_ticks = y_ticks
        self.y_tick_labels = y_tick_labels
        self.scale = 1
        self.x_axis_scale = x_axis_scale
        self.y_axis_scale = y_axis_scale
        self.origin_point = np.array(
            [-(self.x_max-self.x_min) / 2.0 * self.x_axis_scale, -0.5, 0])
        self.graph = VGroup()

    def show_axis(self, animate=False):
        x_start = np.array([self.x_min * self.x_axis_scale, 0, 0])
        x_end = np.array([self.x_max * self.x_axis_scale, 0, 0])

        y_start = np.array([0, self.y_min * self.y_axis_scale, 0])
        y_end = np.array([0, self.y_max * self.y_axis_scale, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)
        x_axis.set_color(self.axis_color)
        y_axis.set_color(self.axis_color)

        #x_axis.shift(self.origin_point * 0.5)
        x_axis.move_to(self.origin_point + x_axis.get_center())
        y_axis.move_to(self.origin_point + y_axis.get_center())

        #self.add(x_axis, y_axis)
        self.graph.add(x_axis, y_axis)
        self.add_x_ticks()
        self.add_x_labels()
        self.add_y_ticks()
        self.add_y_labels()
        self.graph.scale(self.scale)
        if animate:
            self.play(Write(self.graph))
        else:
            self.add(self.graph)

    def add_x_ticks(self):
        height = 0.15
        line = Line(np.array([0, -height, 0]), np.array([0, height, 0]))
        line.set_color(self.axis_color)

        for i in range(len(self.x_ticks)):
            copy = line.copy()
            copy.move_to(self.origin_point +
                         np.array([self.x_ticks[i] * self.x_axis_scale, 0, 0]))
            # self.add(copy)
            self.graph.add(copy)

    def add_y_ticks(self):
        width = 0.15
        line = Line(np.array([-width, 0, 0]), np.array([width, 0, 0]))
        line.set_color(self.axis_color)

        for i in range(len(self.y_ticks)):
            copy = line.copy()
            copy.move_to(self.origin_point +
                         np.array([0, self.y_ticks[i] * self.y_axis_scale, 0]))
            # self.add(copy)
            self.graph.add(copy)

    def add_x_labels(self):
        for i in range(len(self.x_tick_labels)):
            self.x_tick_labels[i].next_to(
                self.origin_point + np.array([self.x_ticks[i] * self.x_axis_scale, 0, 0]), DOWN)
            self.x_tick_labels[i].set_color(self.tick_labels_color)
            self.graph.add(self.x_tick_labels[i])

    def add_y_labels(self):
        for i in range(len(self.y_tick_labels)):
            self.y_tick_labels[i].next_to(
                self.origin_point + np.array([0, self.y_ticks[i] * self.y_axis_scale, 0]), LEFT)
            self.y_tick_labels[i].set_color(self.tick_labels_color)
            self.graph.add(self.y_tick_labels[i])

    def get_graph(self, func, color=None, x_min=None, x_max=None, **kwargs):
        if color is None:
            color = YELLOW
        if x_min is None:
            x_min = self.x_min
        if x_max is None:
            x_max = self.x_max

        def parameterized_function(alpha):
            x = interpolate(x_min, x_max, alpha)
            y = func(x)
            if not np.isfinite(y):
                y = self.y_max
            # return self.coords_to_point(x, y)
            return np.array([x * self.x_axis_scale, y * self.y_axis_scale, 0]) + self.origin_point

        graph = ParametricFunction(
            parameterized_function, color=color, **kwargs)
        graph.underlying_function = func
        # graph.move_to(self.origin_point)
        graph.scale(self.scale)
        return graph

    def coords_to_point(self, x, y):
        result = self.x_axis.number_to_point(x)[0] * RIGHT
        result += self.y_axis.number_to_point(y)[1] * UP
        return result

    # def func(self, t):
    #   return np.array((np.sin(2 * t), np.sin(3 * t), 0))
