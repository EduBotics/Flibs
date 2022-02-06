from chromosome import Chromosome
from random import randrange


class Flib:
    def __init__(self, chromosome_string):
        self.chromosome = Chromosome(chromosome_string)

    @property
    def chromosome_length(self):
        return self.chromosome.chromosome_length

    @property
    def chromosome_string(self):
        return self.chromosome.as_string()

    def evaluate(self, input_string):
        output_val = None
        score = 0
        for input_val in input_string:
            if output_val is not None:
                print(f"{output_val = } <=> {input_val = }")
                if output_val == input_val:
                    score += 1
            output_val = self.chromosome.transition(input_val)
        return score

    def mutate(self):
        self.chromosome.mutate()

    def crossover(self, mate_flib):
        left_cut = randrange(1, self.chromosome_length - 2)
        right_cut = randrange(left_cut + 1, self.chromosome_length - 1)
        child_chromosome = (
            self.chromosome_string[0:left_cut]
            + mate_flib.chromosome_string[left_cut:right_cut]
            + self.chromosome_string[right_cut:]
        )
        child = Flib(child_chromosome)
        return child
