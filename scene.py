from manim import *
import random

class CreateCircle(Scene):
    def construct(self):

        # Text of person
        person = Text("Person").shift(UP*2)
        
        # Create a coin
        coin = Circle(radius=1, color=WHITE, fill_opacity=1).set_fill(BLUE, opacity=0.5)
        
        heads_text = Text("Heads").move_to(DOWN*1.5).set_color(GREEN)
        tails_text = Text("Tails").move_to(DOWN*1.5).set_color(RED)
        
        self.play(Write(person), Create(coin))
        
        while True:
            self.play(coin.animate.rotate(PI, axis=UP), run_time=0.5)
            self.play(coin.animate.rotate(PI, axis=UP), run_time=0.5)
            
            result = random.choice(["Heads", "Tails"])
            if result == "Heads":
                self.play(Write(heads_text))
                break
            else:
                self.play(Write(tails_text))
                self.play(FadeOut(tails_text)) 
            
        self.wait(2)