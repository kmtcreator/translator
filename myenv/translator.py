from googletrans import Translator
import datetime

def translate_burmese_to_english(burmese_words):
    translator = Translator()
    translation_log = []

    for word in burmese_words:
        translation = translator.translate(word, src='my', dest='en')
        translation_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "burmese_word": word,
            "english_translation": translation.text
        }
        translation_log.append(translation_entry)

    return translation_log

if __name__ == "__main__":
    burmese_words = ["မင်္ဂလာပါ", "သီချင်း", "ပြန်လည်သွားပါ"]

    log = translate_burmese_to_english(burmese_words)

    with open("translation_log.txt", "a", encoding="utf-8") as log_file:
        for entry in log:
            log_file.write(
                f"{entry['timestamp']} - Burmese: {entry['burmese_word']} -> English: {entry['english_translation']}\n"
            )
