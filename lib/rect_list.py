from manim import *
import numpy as np


class RectList(VMobject):
    def __init__(self, numbers, **kwargs):
        VMobject.__init__(self, **kwargs)
        self.group = VGroup()
        self.size = len(numbers)
        self.buf = 0.1
        self.scene_width = 12
        self.width = 0.9
        self.height = 3
        self.numbers = numbers
        self.rects = []

        if self.width * self.size > self.scene_width:
            self.width = (self.scene_width-self.buf*self.size) / self.size

        for j in range(self.size):
            number = numbers[j]
            rect = Rectangle(width=self.width, height=self.height*number)
            left_lower = np.array([-6, -2, 0])
            rect.move_to(np.array([j * (self.width + self.buf), 0, 0]) + left_lower,
                         aligned_edge=DOWN)
            self.group.add(rect)
            self.rects.append(rect)

    def swap(self, i, j):
        tmp = self.numbers[i]
        self.numbers[i] = self.numbers[j]
        self.numbers[j] = tmp

        tmp = self.rects[i]
        self.rects[i] = self.rects[j]
        self.rects[j] = tmp

    def get_value(self, i):
        return self.numbers[i]

    def get_rect(self, i):
        return self.rects[i]

    def get_rects(self):
        return self.group

    def size(self):
        return self.size
