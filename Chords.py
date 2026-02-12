import copy
from Notes import Note

class Chord():
    def __init__(self, root=0, intervals=[], chord=[], note=Note()):
        self.intervals = intervals
        self.chord = chord
        self.root = root
        self.note_template = note
    def generate_chord(self):
        rootnote = copy.deepcopy(self.note_template) 
        rootnote.pitch = self.root
        pitch = self.root
        self.chord = [rootnote]
        for i in self.intervals:
            pitch += i
            note = copy.deepcopy(self.note_template) 
            note.pitch = pitch
            self.chord.append(note)
    def generate_intervals(self):
        pass

class AlternatingChord(Chord):
    def __init__(self, root=0, pattern=[], iterations=1, note=Note()):
        super().__init__(root, note=note)
        self.pattern = pattern
        self.iterations = iterations
    def generate_intervals(self):
        self.intervals = []
        for i in range(self.iterations):
            for p in self.pattern:
                self.intervals.append(p)

class Basictriad(AlternatingChord):
    def __init__(self, root=0, iterations=1, is_major=True, note=Note()):
        super().__init__(root, pattern = [4, 3] if is_major else [3, 4], iterations=iterations, note=note)
        self.generate_intervals()
        self.generate_chord()
