import genanki
from selenium import webdriver

songang_korean_students_book_deck_id = 1231979823374982316
hangul_model_id = 283473298476
download_dir = "F:\Python\PycharmProjects\GenerateAnki\AudioFiles"
model = genanki.Model(hangul_model_id, 'Hangul + Audio 한글',
                      fields=[
                          {'name': 'Question'},
                          {'name': 'Answer'},
                          {'name': 'Audio'},
                      ],
                      templates=[
                          {
                              'name': 'Card 1',
                              'qfmt': '{{Question}}',
                              'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{Audio}}',
                          },
                      ])

FIREFOX_PREFERENCES = {
    "dom.popup_maximum": 0,
    "browser.download.folderList": 2,
    "browser.download.panel.shown": False,
    "privacy.popups.showBrowserMessage": False,
    "browser.download.manager.showWhenStarting": False,
    "browser.helperApps.neverAsk.saveToDisk": ".mp3 audio/mpeg",
}
fx_profile = webdriver.FirefoxProfile()
fx_profile.default_preferences.update(FIREFOX_PREFERENCES)
fx_profile.set_preference("browser.download.dir", download_dir)
