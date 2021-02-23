from manim import *
import numpy as np


class SwapAligned(Transform):
    def __init__(
        self, *mobjects: Mobject, path_arc: float = 90 * DEGREES, aligned_edge=ORANGE, **kwargs
    ) -> None:
        self.group = Group(*mobjects)
        self.aligned_edge = aligned_edge
        super().__init__(self.group, path_arc=path_arc, **kwargs)

    def create_target(self) -> Group:
        target = self.group.copy()
        cycled_targets = [target[-1], *target[:-1]]
        for m1, m2 in zip(cycled_targets, self.group):
            m1.move_to(m2, aligned_edge=self.aligned_edge)
        return target
