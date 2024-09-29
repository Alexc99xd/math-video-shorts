from manim import *

class DerivationAnimation(Scene):
    def construct(self):
        # Step 1: Display the introduction text and formula
        intro_text = Text("Derivation of the Series:").scale(0.7)
        series_text = MathTex(r"\sum_{k=1}^{\infty} k x^k = \frac{x}{(1 - x)^2}")
        
        intro_text.to_edge(UP)
        series_text.next_to(intro_text, DOWN)

        self.play(Write(intro_text))
        self.play(Write(series_text))
        self.wait(2)

        # Step 2: Display the geometric series
        geom_series = MathTex(r"\sum_{k=0}^{\infty} x^k = \frac{1}{1 - x}")
        geom_series.next_to(series_text, DOWN)
        self.play(Write(geom_series))
        self.wait(2)

        # Update bottom text
        step_text = Text("Step 1: Start with the geometric series").scale(0.7)
        step_text.to_edge(DOWN)
        self.play(Write(step_text))

        # Move everything up to make room for the next step
        self.play(
            intro_text.animate.shift(UP * 1.5),
            series_text.animate.shift(UP * 1.5),
            geom_series.animate.shift(UP * 1.5),
            step_text.animate.shift(UP * 1.5)
        )

        # Step 3: Show the instruction to differentiate
        step_text_new = Text("Step 2: Differentiate with respect to x").scale(0.7)
        step_text_new.to_edge(DOWN)
        self.play(ReplacementTransform(step_text, step_text_new))

        # Show the derivative process
        geom_derivative = MathTex(
            r"\frac{d}{dx}\left(\sum_{k=0}^{\infty} x^k\right) = \frac{d}{dx}\left(\frac{1}{1 - x}\right)"
        )
        geom_derivative.next_to(geom_series, DOWN)
        self.play(Write(geom_derivative))
        self.wait(2)

        # Move everything up
        self.play(
            intro_text.animate.shift(UP * 1.5),
            series_text.animate.shift(UP * 1.5),
            geom_series.animate.shift(UP * 1.5),
            geom_derivative.animate.shift(UP * 1.5),
            step_text_new.animate.shift(UP * 1.5)
        )

        # Step 4: Show the result of differentiation
        step_text_new_2 = Text("Step 3: Apply the result of differentiation").scale(0.7)
        step_text_new_2.to_edge(DOWN)
        self.play(ReplacementTransform(step_text_new, step_text_new_2))

        differentiated_series = MathTex(
            r"\sum_{k=1}^{\infty} k x^{k-1} = \frac{1}{(1 - x)^2}"
        )
        differentiated_series.next_to(geom_derivative, DOWN)
        self.play(Write(differentiated_series))
        self.wait(2)

        # Move everything up again
        self.play(
            intro_text.animate.shift(UP * 1.5),
            series_text.animate.shift(UP * 1.5),
            geom_series.animate.shift(UP * 1.5),
            geom_derivative.animate.shift(UP * 1.5),
            differentiated_series.animate.shift(UP * 1.5),
            step_text_new_2.animate.shift(UP * 1.5)
        )

        # Step 5: Show instruction to multiply by x
        step_text_new_3 = Text("Step 4: Multiply both sides by x").scale(0.7)
        step_text_new_3.to_edge(DOWN)
        self.play(ReplacementTransform(step_text_new_2, step_text_new_3))

        # Show the result of multiplying by x
        multiplied_series = MathTex(
            r"x \sum_{k=1}^{\infty} k x^{k-1} = \frac{x}{(1 - x)^2}"
        )
        multiplied_series.next_to(differentiated_series, DOWN)
        self.play(Write(multiplied_series))
        self.wait(2)

        # Move everything up again
        self.play(
            intro_text.animate.shift(UP * 1.5),
            series_text.animate.shift(UP * 1.5),
            geom_series.animate.shift(UP * 1.5),
            geom_derivative.animate.shift(UP * 1.5),
            differentiated_series.animate.shift(UP * 1.5),
            multiplied_series.animate.shift(UP * 1.5),
            step_text_new_3.animate.shift(UP * 1.5)
        )

        # Step 6: Show the final formula
        step_text_new_4 = Text("Step 5: Final formula").scale(0.7)
        step_text_new_4.to_edge(DOWN)
        self.play(ReplacementTransform(step_text_new_3, step_text_new_4))

        final_formula = MathTex(r"\sum_{k=1}^{\infty} k x^k = \frac{x}{(1 - x)^2}")
        final_formula.next_to(multiplied_series, DOWN)
        self.play(Write(final_formula))
        self.wait(2)

        # End of animation
        self.play(FadeOut(final_formula), FadeOut(step_text_new_4))
