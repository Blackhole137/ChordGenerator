import copy

class Progression():
    def __init__(self):
        self.chord_template = None
        self.root = 0
        self.root_shifts = []
        self.progression = []
    def generate_progression(self):
        for shift in self.root_shifts:
            chord = copy.deepcopy(self.chord_template)
            chord.root = self.root + shift
            chord.generate_chord()
            self.progression.append(chord)
    def display_progression(self):
        for chord in self.progression:
            for note in chord.chord:
                print(note, end=' ')
            print('\n')
