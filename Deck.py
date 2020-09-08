import genanki


class Deck:

    def __init__(self, model, name, deck_id, description=""):
        self.name = name
        self.model = model
        self.deck_id = deck_id
        self.description = description
        self.deck = None
        self.package = None
        self._setup()

    def _setup(self):
        self.deck = genanki.Deck(self.deck_id, self.name, self.description)

    def add_note(self, question, answer, audio_file):
        self.deck.add_note(genanki.Note(model=self.model, fields=[question, answer, audio_file]))

    def add_audio_paths(self, paths):
        self.package = genanki.Package(self.deck)
        self.package.media_files = paths

    def deck_to_apkg(self, path):
        if self.package is None:
            raise ValueError('self.package is None')
        self.package.write_to_file(path + self.name + ".apkg")
