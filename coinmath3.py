from manim import *

class ShowEquations3(Scene):
    def construct(self):
        # Expected Value Equation
        expected_value = MathTex(
            r"E(X) = \, 0 \cdot P(H) \, + \, 1 \cdot P(TH) \, + \, 2 \cdot P(TTH) \, + \, 3 \cdot P(TTTH) \, + \, \cdots "
        ).scale(0.75).move_to(UP * 2.5)  # Increased upward shift

        # Infinite Series Equation
        infinite_series = MathTex(
            r"E(X) = 0 \cdot \frac{1}{2} + 1 \cdot \frac{1}{4} + 2 \cdot \frac{1}{8} + 3 \cdot \frac{1}{16} + \cdots"
        ).scale(0.75).next_to(expected_value, DOWN, buff=0.5)

        # First Summation Equation
        summation_eq = MathTex(
            r"\sum_{n=0}^{\infty} \frac{n}{2^{n+1}}"
        ).scale(0.75).next_to(infinite_series, DOWN, buff=0.5)

        # Second Summation Equation
        summation_eq2 = MathTex(
            r"\sum_{k=0}^{\infty} k x^{k+1}"
        ).scale(0.75).next_to(summation_eq, DOWN, buff=0.5)

        # Third Summation Equation
        summation_eq3 = MathTex(
            r"\frac{1}{2} \sum_{k=0}^{\infty} k x^{k}"
        ).scale(0.75).next_to(summation_eq2, DOWN, buff=0.5)

        # Display x = 1/2 on the side
        x_value = MathTex(r"where \quad  x = \frac{1}{2}").next_to(summation_eq3, RIGHT, buff=1)

        # Animation of the expected value
        self.play(Write(expected_value))
        self.wait(0)

        # Display the infinite series equation
        self.play(Write(infinite_series))
        self.wait(0)

        # Display the first summation equation
        self.play(Write(summation_eq))
        self.wait(0)

        # Display the second summation equation
        self.play(Write(summation_eq2))
        self.wait(0)

        # Display the third summation equation and x value
        self.play(Write(summation_eq3))
        self.play(Write(x_value))
        self.wait(2)
