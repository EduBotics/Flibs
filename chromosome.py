from random import choice, randrange


class Chromosome:
    def __init__(self, chromosome):
        self.chromosome = list(chromosome)
        self.chromosome_length = len(self.chromosome)
        self.states = int(len(chromosome) / 4)
        self.current_state = "0"

    def __str__(self):
        return "".join(self.chromosome)

    def __repr__(self):
        return f"Chromosome({str(self)})"

    def as_string(self):
        return str(self)

    def get_output(self, input_val):
        return self.get_table_entry(input_val)[0]

    def get_nextstate(self, input_val):
        return self.get_table_entry(input_val)[1]

    def get_table_entry(self, input_val):
        loc = int(self.current_state) * 4 + 2 * int(input_val)
        return self.chromosome[loc : loc + 2]

    def transition(self, input_val):
        output = self.get_output(input_val)
        next_state = self.get_nextstate(input_val)
        self.current_state = next_state
        return output

    def mutate(self):
        loc = randrange(0, self.chromosome_length)
        current = self.chromosome[loc]
        if loc % 2:
            # Odd loc is an output allele
            self.chromosome[loc] = str(~current & 1)  # Bit flip
        else:
            # Even loc is a state allele
            self.chromosome[loc] = choice([str(val) for val in range(self.states) if val != current])
