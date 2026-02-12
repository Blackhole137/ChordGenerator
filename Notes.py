class Note():
    def __init__(self, pitch=0):
        self.pitch = pitch
    def __str__(self):
        return str(self.pitch)

class RollingNote(Note):
    def __init__(self, pitch=0, length=1):
        super().__init__(pitch)
        self.length = length
    def __str__(self):
        return str(self.pitch) * self.length

class DraggingNote(Note):
    def __init__(self, pitch=0, length=1):
        super().__init__(pitch)
        self.length = length
    def __str__(self):
        return str(self.pitch) + '-' * (self.length - 1)
