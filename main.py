from browser import Browser
from config import model, test_deck_id, fx_profile
from Deck import Deck

words = ['보내다', '안녕하세요', '주세요', '죄송합니다', '고맙습니다', '네', '아니요', '아마도']
path_to_audio_files = "F:/Python/PycharmProjects/GenerateAnki/AudioFiles/"
long_audio_paths = []
browser = Browser(fx_profile)
browser.search_list_of_words(words)
browser.quit()

hangul = Deck(model, 'test', test_deck_id)

for word in words:
    hangul.add_note(word, "", f"[sound:pronunciation_ko_{word}.mp3]")
    long_audio_paths.append(path_to_audio_files + f"pronunciation_ko_{word}.mp3")

hangul.add_audio_paths(long_audio_paths)
hangul.deck_to_apkg("")
