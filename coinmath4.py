from manim import *

class SolveExpectedValue2(Scene):
    def construct(self):
        # Original equation with the summation
        original_eq = MathTex(
            r"E(X) = \frac{1}{2} \sum_{k=0}^{\infty} k x^{k}"
        ).scale(1.2).move_to(UP * 0)
        
        # Final equation with the substitution
        substituted_eq = MathTex(
            r"E(X) = \frac{1}{2} \cdot \frac{x}{(1 - x)^2}"
        ).scale(1.2).move_to(UP * 0)
        
        # After substituting x = 1/2
        eq_with_substitution = MathTex(
            r"E(X) = \frac{1}{2} \cdot \frac{\frac{1}{2}}{\left(1 - \frac{1}{2}\right)^2}"
        ).scale(1.2).move_to(UP * 0)

        # Simplified step by step
        simplified_step1 = MathTex(
            r"E(X) = \frac{1}{2} \cdot \frac{\frac{1}{2}}{\left(\frac{1}{2}\right)^2}"
        ).scale(1.2).move_to(UP * 0)
        
        simplified_step2 = MathTex(
            r"E(X) = \frac{1}{2} \cdot \frac{\frac{1}{2}}{\frac{1}{4}}"
        ).scale(1.2).move_to(UP * 0)

        final_result = MathTex(
            r"E(X) = \frac{1}{2} \cdot 2 = 1"
        ).scale(1.2).move_to(UP * 0)

        # Step 1: Show the original equation
        self.play(Write(original_eq))
        self.wait(1)

        # Step 2: Transform into substituted equation (summation becomes x / (1 - x)^2)
        self.play(Transform(original_eq, substituted_eq))
        self.wait(1)

        # Step 3: Substitute x = 1/2
        self.play(Transform(original_eq, eq_with_substitution))
        self.wait(1)

        # Step 4: Simplify the equation step-by-step
        self.play(Transform(original_eq, simplified_step1))
        self.wait(1)

        self.play(Transform(original_eq, simplified_step2))
        self.wait(1)

        # Step 5: Show the final result
        self.play(Transform(original_eq, final_result))
        self.wait(2)

        # Optional: Fade out the final equation
        self.play(FadeOut(original_eq))
