import random

import genanki

from browser import Browser
from config import fx_profile


class AnkeGenerator:

    def __init__(self, model, deck_name, deck_id, path_to_audio_files="AudioFiles/"):
        self.path_to_audio_files = path_to_audio_files
        self.browser = Browser(fx_profile)
        self.deck = Deck(model, deck_name, deck_id)

    def generate_deck_from_word_file(self, path):
        words = {}
        with open(path, "r", encoding='utf-8') as file:
            for line in file.readlines():
                ko_word, tr_word = line.split(" ")
                words[ko_word.strip()] = tr_word.strip()
        self.generate_deck_from_word_dict(words)

    def generate_deck_from_word_dict(self, words: dict, deck_path=""):
        audio_file_paths, words_not_found = [], {}
        for ko_word, tr_word in words.items():
            res = self.browser.search_word(ko_word)
            if res == 200 or res == 201:
                audio_file_paths.append(self.path_to_audio_files + f"pronunciation_ko_{ko_word}.mp3")
                self.deck.add_note(ko_word, tr_word, f"[sound:pronunciation_ko_{ko_word}.mp3]")
            elif res == 404:
                words_not_found[ko_word] = "No Audio File found"
                sound = random.choice(['yooo.mp3', 'zugriff.mp3'])
                sound_path = self.path_to_audio_files + sound
                self.deck.add_note(ko_word, tr_word, f"[sound:{sound}]")
                if sound_path not in audio_file_paths:
                    audio_file_paths.append(sound_path)
        self.browser.quit()
        self.deck.add_audio_paths(audio_file_paths)
        self.deck.deck_to_apkg(deck_path)
        self.write_words_to_file(words_not_found)

    @classmethod
    def write_words_to_file(cls, words):
        with open("log.txt", "w", encoding='utf-8') as file:
            for ko_word, message in words.items():
                file.write(f"{ko_word} -> {message}\n")


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
