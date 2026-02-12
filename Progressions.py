import copy

class Progression():
    def __init__(self):
        self.chord_template = None
        self.root = 0
        self.root_shifts = []
        self.progression = []
    def generate_progression(self):
        self.progression = []
        for shift in self.root_shifts:
            chord = copy.deepcopy(self.chord_template)
            template_root = chord.root
            chord.root = template_root + self.root + shift
            chord.generate_chord()
            self.progression.append(chord)
    def __str__(self):
        result = []
        for chord in self.progression:
            chord_str = ' '.join(str(note) for note in chord.chord)
            result.append(chord_str)
        return '\n'.join(result)
