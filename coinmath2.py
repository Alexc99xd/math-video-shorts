from manim import *

class CoinFlipProbabilities(Scene):
    def construct(self):
        # Titles and Labels
        title = Text("Coin Flip Probabilities")
        title.scale(1).to_edge(UP)
        self.play(Write(title))
        
        # List of sequences and their probabilities
        sequences = ["H", "TH", "TTH", "TTTH", "TTTTH"]
        probabilities = [r"\frac{1}{2}", r"\frac{1}{4}", r"\frac{1}{8}", r"\frac{1}{16}", r"\frac{1}{32}"]
        
        # Display the sequences and their probabilities
        for i, (seq, prob) in enumerate(zip(sequences, probabilities)):
            # Sequence label
            sequence_text = Text(f"{seq}")
            sequence_text.shift(LEFT * 4 + DOWN * (i-2))
            sequence_text.scale(0.8)  # Scaling down

            # Probability as a fraction
            probability_text = MathTex(prob)
            probability_text.shift(RIGHT * 2 + DOWN * (i-2))
            probability_text.scale(0.8)  # Scaling down

            # Animation of showing both
            self.play(Write(sequence_text), Write(probability_text))
        
        self.wait(1)
