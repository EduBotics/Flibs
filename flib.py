from chromosome import Chromosome


class Flib:
    def __init__(self, chromosome_string):
        self.chromosome = Chromosome(chromosome_string)

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
