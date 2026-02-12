from Notes import Note, RollingNote, DraggingNote
from Chords import Chord, AlternatingChord, Basictriad
from Progressions import Progression

if __name__ == "__main__":
    progression = Progression()
    progression.chord_template = Basictriad(root=0, iterations=2, is_major=True)
    progression.root_shifts = [0, 5, 7]
    progression.generate_progression()
    progression.display_progression()