from random import randint, randrange, random
from flib import Flib
from operator import attrgetter
from collections import namedtuple
import time
import argparse


FlibScore = namedtuple("FlibScore", ["flib", "score"])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num-states", default=5, type=int)
    parser.add_argument("-i", "--input-environment", default="1010101110101011")
    return parser.parse_args()


class PrimordialSoup:
    def __init__(self, num_states, input_environment, soup_size=100):
        self.num_states = num_states
        self.input_environment = input_environment
        self.primordial_soup = []
        self.soup_size = soup_size

    @property
    def score(self):
        self.sort_soup()
        return self.primordial_soup[0].score

    def generate_allele_pair(self):
        output_allele = randint(0, 1)
        state_allele = randrange(0, self.num_states)
        return [output_allele, state_allele]

    def generate_flib(self):
        chromosome = "".join(
            "".join(str(x) for x in self.generate_allele_pair(self.num_states))
            + "".join(str(x) for x in self.generate_allele_pair(self.num_states))
            for _ in range(self.num_states)
        )
        return Flib(chromosome)

    def calc_flibscore(self, flib):
        return FlibScore(flib, flib.evaluate(self.input_environment))

    def sort_soup(self):
        self.primordial_soup = sorted(
            self.primordial_soup, key=attrgetter("score"), reverse=True
        )

    def generate_soup(self):
        self.primordial_soup = [
            self.calc_flibscore(self.generate_flib()) for _ in range(self.soup_size)
        ]
        self.sort_soup()

    def breed(self):
        self.sort_soup()
        best_flib = self.primordial_soup[0]
        mate_flib = self.primordial_soup[randrange(1, len(self.primordial_soup))]
        child = self.calc_flibscore(best_flib.flib.crossover(mate_flib.flib))
        if child.score > self.primordial_soup[-1].score:
            self.primordial_soup[-1] = child
        else:
            self.primordial_soup.append(child)
        print(
            f"Breeding {best_flib.flib} {best_flib.score} with {mate_flib.flib} {mate_flib.score} produced {child.flib} {child.score}"
        )

    def mutate(self):
        index = randrange(0, len(self.primordial_soup))
        self.primordial_soup[index].flib.mutate()
        self.primordial_soup[index] = self.calc_flibscore(
            self.primordial_soup[index].flib
        )


def main(num_states, input_environment):
    target_score = len(input_environment) - 1
    primordial_soup = PrimordialSoup(num_states, input_environment).generate_soup()

    tick = 0
    while primordial_soup.score != target_score:
        print(f"{tick}: best: {primordial_soup.score} / {target_score}")
        if random() > 0.2:
            primordial_soup.breed()
        primordial_soup.mutate()
        tick += 1
        time.sleep(0.2)

    print(
        f"Perfect score from Flib {primordial_soup[0].flib} scoring {primordial_soup[0].score}"
    )


if __name__ == "__main__":
    args = parse_args()
    main(args.num_states, args.input_environment)
