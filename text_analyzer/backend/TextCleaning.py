import re
import emoji
import csv
import emot
from langdetect import detect
from string import punctuation
from typing import List



most_common_emoji = {
    "❣": "אהבה",
    "♥": "אהבה",
    "❤": "אהבה",
    "💔": "אהבה",
    "💖": "אהבה",
    "💕": "אהבה",
    "💗": "אהבה",
    "💚": "אהבה",
    "🥰": "אהבה",
    "😘": "אהבה",
    "😍": "אהבה",
    "🤩": "אהבה",
    "😻": "אהבה",

    "😀": "שמחה",
    "🙂": "שמחה",
    "😂": "שמחה",
    "🤣": "שמחה",
    "😊": "שמחה",

    "🔥": "אש",
    "👑": "כתר",
   
    "😭": "עצב",
    "😢": "עצב", 
    "🥺": "עצב",

   
    "🤢": "בחילה",
    "🤮": "בחילה",

    "♀": "סקס",
    "🖕": "סקס",
    
    "🤦": "פדיחה",
    "🙏": "תקוה",
    "👏": "כל הכבוד",

    "☠": "מוות",
    "🙎": "פדיחה",
    "😱": "נבהל",
}


def get_stopwords(path):
    results = []
    with open(path, 'r', encoding="utf8") as f:
      for row in csv.reader(f):
            results.append(row[0])
    return results


def rm_emoji(text: str, replace: bool = False) -> str:
    """ Removes emojis if 'replace' set to False, otherwise replaces emojis with their
    with their meaning.
    """
    if replace:
        return ''.join([ch if ch not in emoji.UNICODE_EMOJI else emoji.demojize(ch) for ch in text]).replace(':', ' ')
    else:
        return ''.join([ch if ch not in emoji.UNICODE_EMOJI else ' ' for ch in text])


def rm_punctuation(text: str, punctuation_marks: str = punctuation, replace: bool = False):
    rep = ' ' if replace else ''
    return ''.join([ch if ch not in punctuation_marks else rep for ch in text])


def rm_unicode_non_char(text: str) -> str:
    """ Removes all non-letters and non-whitespaces """
    return re.sub(r'[^א-ת\s]', '', text) 
    # return re.sub(r'[^\w\s]', '', text)


def rm_mentions(text: str, replace: bool = False) -> str:
    """ Removes mentions if 'replace' set to False, otherwise replaces them with tokens """
    tag = r'(@[\w_.-]+)'
    token = 'USER' if replace else ''
    return re.sub(tag, token, text)


def rm_hashtags(text: str, replace: bool = False) -> str:
    """ Removes hashtags if 'replace' set to False, otherwise replaces them with tokens """
    tag = r'(#[\w_.-]+)'
    token = 'HASHTAG' if replace else ''
    return re.sub(tag, token, text)


def rm_url_and_email(text: str, replace: bool = False) -> str:
    """ Removes hyperlinks and emails if 'replace' set to False, otherwise replaces them with tokens """
    url = r"(https?:\/\/[^ ]*)"
    url_token = 'LINK' if replace else ''
    email = r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)'
    url_email = 'EMAIL' if replace else ''
    text = re.sub(url, url_token, text)
    text = re.sub(email, url_email, text)
    return text


def rm_multiple_chars(text: str) -> str:
    """ Replace 3 or more consecutive letters by 2 letter.
    hellooooooooooo-> helloo
    """
    sequence_pattern = r"(.)\1\1+"
    seq_replace_pattern = r"\1\1"
    return re.sub(sequence_pattern, seq_replace_pattern, text)


def rm_stop_words(text: str) -> str:
    """ Removes stopwords """
    stopwords_path = "/home/riki/Study/Project/TextAnalyzer/text_analyzer/backend/stopwords.csv"
    stopwords = get_stopwords(stopwords_path)
    return ' '.join([word for word in text.split() if word not in stopwords])


def rm_short_words(text: str, min_len: int = 2) -> str:
    """ Removes words that shorter that min_len """
    return ' '.join([word for word in text.split() if len(word) >= min_len])


def rm_white_spaces(text: str) -> str:
    """ Removes all white spaces """
    return ' '.join(text.split())


def lng_detect(text):
    """ Returns the main language of the text """
    try:
        return detect(text)
    except:
        return None


def convert_emojis(text):
    """ Converting emojis into word, replace common emoji by meaning, and delete rare emoji """
    emoji_lst = emot.emoji(text).get('value', [])
    
    for emoji in emoji_lst:
        text = text.replace(emoji, ' ' + most_common_emoji.get(emoji, ''))
    return text