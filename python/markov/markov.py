#!/usr/bin/env python3

"""
A simple Markov chain-powered text generator.

You can run this code with `python -X utf8 markov.py`, or import it in another
file and use the Chain class directly.
"""

import random
import argparse

from pathlib import Path
from collections import defaultdict, Counter

# Characters that text generation should end on.
# TODO: Handle quotation marks and brackets.
STOP_CHARACTERS = (
    ".",
    "?",
    "!",
    "…",
    # This is *technically* not a character, but since no one actually uses
    # Unicode's ellipses character we have to include this.
    "...",
)


class Chain:
    """An nth-order Markov chain specialised for text generation given an input corpus."""

    def __init__(self, order):
        self.model = defaultdict(Counter)
        self.order = order

    def train(self, corpus):
        """Train the chain's model with the given input corpus."""
        # TODO: Write/use a more idiomatic iterator for this.
        for i in range(len(corpus)):
            # Do not record the last state/word in the corpus since it has no following
            # words.
            if i == len(corpus) - self.order:
                break

            key = " ".join(corpus[i : i + self.order])
            val = " ".join(corpus[i + self.order : i + 2 * self.order])

            self.model[key].update([val])

    def generate(self):
        """Generate a random string based upon the chain's current model."""
        state = random.choice(list(self.model))
        out = [state]

        for _ in range(50):
            choice = random.choices(list(self.model[state]), self.model[state].values())
            state = choice[0]

            out.extend(choice)

            if choice[0].endswith(STOP_CHARACTERS):
                break

        return " ".join(out)


def main():
    """Main executable entry point."""
    parser = argparse.ArgumentParser(
        description="Generate text from a corpus with a Markov chain."
    )
    parser.add_argument("corpus", type=str, help="The file path to the input text.")
    parser.add_argument(
        "-o",
        "--order",
        type=int,
        default=1,
        help="The order (amount of words to consider) of the Markov chain.",
    )

    args = parser.parse_args()

    chain = Chain(args.order)

    print("Training model...")
    chain.train(Path(args.corpus).read_text().rstrip().split())

    print("Generating text from model...")
    print(chain.generate())


if __name__ == "__main__":
    main()
