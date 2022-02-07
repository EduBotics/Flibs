from random import randint, randrange, random
from flib import Flib
from operator import itemgetter
from collections import namedtuple

NUM_STATES = 4
INPUT_ENVIRONMENT = "110110110"
FlibScore = namedtuple("FlibScore", ["flib", "score"])


def generate_allele_pair(states):
    output_allele = randint(0, 1)
    state_allele = randrange(0, states)
    return [output_allele, state_allele]


def generate_flib(states):
    chromosome = "".join(
        "".join(str(x) for x in generate_allele_pair(states))
        + "".join(str(x) for x in generate_allele_pair(states))
        for _ in range(states)
    )
    return Flib(chromosome)


def generate_soup():
    return [generate_flib(NUM_STATES) for _ in range(100)]


def evaluate_soup(primordial_soup):
    evaluation = sorted(
        [FlibScore(flib, flib.evaluate(INPUT_ENVIRONMENT)) for flib in primordial_soup],
        key=itemgetter(1),
        reverse=True,
    )
    return evaluation


def breed(evaluation, primordial_soup):
    ...


primordial_soup = generate_soup()
evaluation = evaluate_soup(primordial_soup)

if evaluation[0].score == len(INPUT_ENVIRONMENT):
    print(f"Perfect score from Flib {evaluation[0].flib} scoring {evaluation[0].score}")
    exit(0)

if random() > 0.2:
    breed(evaluation, primordial_soup)
