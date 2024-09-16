from manim import *
import random

class SimultaneousCoinFlip(Scene):
    def construct(self):
        # Create 10 people flipping coins
        people_and_coins = VGroup()  # group
        people = VGroup(*[Text(f"Person {i+1}").scale(0.6) for i in range(10)])
        coins = VGroup(*[Circle(radius=0.5, color=WHITE, fill_opacity=1).set_fill(BLUE, opacity=0.5) for i in range(10)])
        
        # combine people and coins
        for person, coin in zip(people, coins):
            # Create a vertical arrangement of person and their coin
            person_and_coin = VGroup(person, coin).arrange(DOWN, buff=0.5)
            people_and_coins.add(person_and_coin)  # Add to the main group
        
        #Grid it up
        people_and_coins.arrange_in_grid(rows=2, cols=5, buff=1.5).move_to(ORIGIN)

        # Add to the scene
        self.play(LaggedStart(*[Write(person) for person in people]))
        self.play(LaggedStart(*[Create(coin) for coin in coins]))

        # TExt for H T
        heads_texts = [Text("Heads").scale(0.5).set_color(GREEN) for _ in range(10)]
        tails_texts = [Text("Tails").scale(0.5).set_color(RED) for _ in range(10)]

        for i in range(10):
            heads_texts[i].next_to(coins[i], DOWN, buff=0.5)
            tails_texts[i].next_to(coins[i], DOWN, buff=0.5)

        heads_landed = [False] * 10

        # keep flipping
        while not all(heads_landed):  # Keep going until everyone has landed heads
            flip_animations = []
            result_animations = []  # To collect result text animations

            for i in range(10):
                if not heads_landed[i]:  # Only flip for people who haven't landed heads yet
                    flip_animations.append(coins[i].animate.rotate(PI, axis=UP))

            # Perform the flips simultaneously, with a run_time
            self.play(AnimationGroup(*flip_animations, lag_ratio=0), run_time=0.5)

            for i in range(10):
                if not heads_landed[i]:
                    result = random.choice(["Heads", "Tails"])
                    
                    if result == "Heads":
                        heads_landed[i] = True
                        result_animations.append(Write(heads_texts[i]))
                    else:
                        result_animations.append(Write(tails_texts[i])) 

            # display
            self.play(AnimationGroup(*result_animations, lag_ratio=0))

            fade_out_animations = [FadeOut(tails_texts[i]) for i in range(10) if not heads_landed[i]]
            if fade_out_animations:
                self.play(AnimationGroup(*fade_out_animations, lag_ratio=0))

        self.wait(2)
