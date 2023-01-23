from math import cos, sin

import numpy as np

from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class Sigmoid(Scene):
    def construct(self):
        axes = Axes(
            (-10, 10, 1),
            (0, 1.5, 0.5),
            x_axis_config={"numbers_to_include": np.arange(-10, 11, 2)},
            y_axis_config={"numbers_to_include": np.arange(0, 1.5, 0.5)},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def sig(z):
            return 1 / (1 + np.exp(-z))

        def d_sig(z):
            return sig(z) * (1 - sig(z))

        sigmoid = axes.plot(sig, color=BLUE)
        sigmoid_label = MathTex(r"\sigma(z)=\frac{1}{1+e^{-z}}", color=BLUE).to_corner(UL)
        d_sigmoid = axes.plot(d_sig, color=RED)
        d_sigmoid_label = (
            MathTex(r"\frac{d}{dz}\sigma=\sigma(z)(1 - \sigma(z))", color=RED)
            .to_corner(UL)
            .shift(DOWN)
        )

        self.play(Create(axes), Create(labels))
        self.play(Write(sigmoid), Write(sigmoid_label), run_time=1)
        self.play(Write(d_sigmoid), Write(d_sigmoid_label), run_time=1)
        self.wait(1)

        self.play(
            Unwrite(sigmoid),
            Unwrite(sigmoid_label),
            Unwrite(labels),
            Unwrite(axes),
            Unwrite(d_sigmoid),
            Unwrite(d_sigmoid_label),
            run_time=1,
        )
