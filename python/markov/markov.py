#!/usr/bin/env python3

"""
A simple Markov chain-powered text generator.

You can run this code with `python -X utf8 markov.py`, or import it in another
file and use the Chain class directly.
"""

import json
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
        self._model = defaultdict(Counter)
        self._order = order

    def train(self, corpus):
        """Train the chain's model with the given input corpus."""
        # TODO: Write/use a more idiomatic iterator for this.
        for i in range(len(corpus)):
            # Do not record the last state/word in the corpus since it has no following
            # words.
            if i == len(corpus) - self._order:
                break

            key = " ".join(corpus[i : i + self._order])
            val = " ".join(corpus[i + self._order : i + 2 * self._order])

            self._model[key].update([val])

    def generate(self):
        """Generate a random string based upon the chain's current model."""
        state = random.choice(list(self._model))
        out = [state]

        for _ in range(50):
            choice = random.choices(
                list(self._model[state]), self._model[state].values()
            )
            state = choice[0]

            out.extend(choice)

            if choice[0].endswith(STOP_CHARACTERS):
                break

        return " ".join(out)

    def serialize(self):
        """Serialise the chain's model to JSON."""
        return json.dumps(self._model)

    def deserialize(self, serialized):
        """
        Deserialise the a model from JSON and load it.

        This *replaces* the preexisting model in memory instead of merging with it.
        """
        self._model = defaultdict(Counter, json.loads(serialized))

        # Wrap every key back into a Counter since defaultdict won't automatically do this.
        for key, val in self._model.items():
            self._model[key] = Counter(val)


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
