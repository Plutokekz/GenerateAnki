from Anki import AnkeGenerator
from config import model, songang_korean_students_book_deck_id

words = ['보내다', '안녕하세요', '주세요', '죄송합니다', '고맙습니다', '네', '아니요', '아마도']
generator = AnkeGenerator(model, 'songang Korean Students Book', songang_korean_students_book_deck_id)
generator.generate_deck_from_word_file("words.txt")
