"""
A simple Markov chain-powered text generator.

You can run this code with `python -X utf8 markov.py`.
"""

import os
import random

from pathlib import Path
from collections import defaultdict, Counter

script_dir = os.path.dirname(os.path.realpath(__file__))

corpus = Path(f'{script_dir}/input.txt').read_text().rstrip().split()
model = defaultdict(Counter)

def make_pairs(corpus):
  """A custom iterator for creating a pair of the nth and (n+1)th elements."""
  for i in range(len(corpus) - 1):
    yield (corpus[i], corpus[i + 1])

print('Training model...')
for word1, word2 in make_pairs(corpus):
  # TODO: Implement a configurable chain order (that is, allow having however
  #       many words as keys instead of only 1).
  model[word1].update([word2])

print('Sampling...')
state = random.choice(list(model))
out = [state]

# TODO: Implement the concept of a "stop word", which is a word with a
#       fullstop, question mark, or such other final punctuation character that
#       text generation will finish on.
for i in range(50):
  print(list(model[state]), model[state].values())
  # TODO: Fix the IndexError that occurs when the element at the end of corpus
  #       is reached, due to the fact that there are no words after it, and
  #       therefore no probability of a next word.
  choice = random.choices(list(model[state]), model[state].values())
  state = choice[0]

  out.extend(choice)

print(' '.join(out))
