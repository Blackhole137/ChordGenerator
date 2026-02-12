import tkinter as tk
from tkinter import ttk
from Progressions import Progression
from Chords import AlternatingChord


class Application:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Chord Generator")

        container = ttk.Frame(self.root, padding=12)
        container.grid(row=0, column=0, sticky="nsew")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        row = 0
        row = self.Templates(container, row)
        row = self.ChordSettings(container, row)
        row = self.ProgressionSettings(container, row)
        self.FinalControls(container, row)

    def run(self) -> None:
        self.root.mainloop()

    def Templates(self, parent: ttk.Frame, row: int) -> int:
        template_row = ttk.Frame(parent)
        template_row.grid(row=row, column=0, sticky="ew", pady=(0, 8))

        major_button = ttk.Button(template_row, text="Major", command=self.set_major_pattern)
        minor_button = ttk.Button(template_row, text="Minor", command=self.set_minor_pattern)

        major_button.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        minor_button.grid(row=0, column=1, sticky="ew", padx=(4, 0))

        template_row.columnconfigure(0, weight=1)
        template_row.columnconfigure(1, weight=1)

        return row + 1

    def set_major_pattern(self) -> None:
        self.chord_pattern_entry.delete(0, tk.END)
        self.chord_pattern_entry.insert(0, "4,3")

    def set_minor_pattern(self) -> None:
        self.chord_pattern_entry.delete(0, tk.END)
        self.chord_pattern_entry.insert(0, "3,4")

    def ChordSettings(self, parent: ttk.Frame, row: int) -> int:
        top_row = ttk.Frame(parent)
        top_row.grid(row=row, column=0, sticky="ew", pady=(0, 8))
        top_row.columnconfigure(0, weight=0)
        top_row.columnconfigure(1, weight=1)
        top_row.columnconfigure(2, weight=0)

        self.root_note_label = ttk.Label(top_row, text="Root note")
        self.root_note_entry = ttk.Spinbox(top_row, from_=0, to=11, width=5)
        self.root_note_entry.set(0)

        self.chord_pattern_label = ttk.Label(top_row, text="Chord pattern")
        self.chord_pattern_entry = ttk.Entry(top_row)

        self.iteration_label = ttk.Label(top_row, text="Iterations")
        self.iteration_entry = ttk.Spinbox(top_row, from_=1, to=16, width=5)
        self.iteration_entry.set(1)

        self.root_note_label.grid(row=0, column=0, sticky="w")
        self.chord_pattern_label.grid(row=0, column=1, sticky="w", padx=(8, 0))
        self.iteration_label.grid(row=0, column=2, sticky="w", padx=(8, 0))

        self.root_note_entry.grid(row=1, column=0, sticky="w")
        self.chord_pattern_entry.grid(row=1, column=1, sticky="ew", padx=(8, 0))
        self.iteration_entry.grid(row=1, column=2, sticky="w", padx=(8, 0))

        return row + 1

    def ProgressionSettings(self, parent: ttk.Frame, row: int) -> int:
        second_row = ttk.Frame(parent)
        second_row.grid(row=row, column=0, sticky="ew", pady=(0, 8))
        second_row.columnconfigure(0, weight=0)
        second_row.columnconfigure(1, weight=1)

        self.progression_root_label = ttk.Label(second_row, text="Progression root")
        self.progression_root_entry = ttk.Spinbox(second_row, from_=0, to=11, width=5)
        self.progression_root_entry.set(0)

        self.root_shifts_label = ttk.Label(second_row, text="Root shifts")
        self.root_shifts_entry = ttk.Entry(second_row)
        self.root_shifts_entry.insert(0, "0")

        self.progression_root_label.grid(row=0, column=0, sticky="w")
        self.root_shifts_label.grid(row=0, column=1, sticky="w", padx=(8, 0))

        self.progression_root_entry.grid(row=1, column=0, sticky="w")
        self.root_shifts_entry.grid(row=1, column=1, sticky="ew", padx=(8, 0))

        return row + 1

    def FinalControls(self, parent: ttk.Frame, row: int) -> None:
        self.generate_button = ttk.Button(parent, text="Generate", command=self.generate)
        self.output_box = tk.Text(parent, height=8, width=40, state="disabled")

        self.generate_button.grid(row=row, column=0, sticky="ew", pady=(0, 8))
        row += 1

        self.output_box.grid(row=row, column=0, sticky="nsew")
        parent.rowconfigure(row, weight=1)

    def generate(self) -> None:
        try:
            if hasattr(self, 'progression'):
                del self.progression
            
            root_note = int(self.root_note_entry.get())
            pattern = [int(x.strip()) for x in self.chord_pattern_entry.get().split(',')]
            iterations = int(self.iteration_entry.get())
            progression_root = int(self.progression_root_entry.get())
            root_shifts = [int(x.strip()) for x in self.root_shifts_entry.get().split(',')]

            self.progression = Progression()
            self.progression.root = progression_root
            self.progression.chord_template = AlternatingChord(root=root_note, pattern=pattern, iterations=iterations)
            self.progression.chord_template.generate_intervals()
            self.progression.chord_template.generate_chord()
            self.progression.root_shifts = root_shifts
            self.progression.generate_progression()

            output_text = str(self.progression)

            self.output_box.config(state="normal")
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert("1.0", output_text)
            self.output_box.config(state="disabled")
        except Exception as e:
            self.output_box.config(state="normal")
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert("1.0", f"Error: {str(e)}")
            self.output_box.config(state="disabled")
