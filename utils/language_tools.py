import re
import string
import enchant
import ftlangdetect
from unidecode import unidecode


# stores already opened enchant.Dict
lang_dicts = dict()


def get_or_load_dict(lang: str) -> enchant.Dict:
    if lang not in lang_dicts:
            lang_dicts[lang] = enchant.Dict(lang)

    return lang_dicts[lang]


def check(text: str, lang: str) -> bool:
    try:
        return get_or_load_dict(lang).check(text)
    except enchant.errors.DictNotFoundError:
        # return False
        raise enchant.errors.DictNotFoundError
    except Exception as e:
        print("Warning: Exception raised during spellchecking:\n\t" + str(e))
        return False


def detect(text: str) -> str:
    return ftlangdetect.detect(text, low_memory=True)["lang"]

    
def is_valid_token(token: str, abstract: str, lang: str) -> bool:
    if token == '':
        return True

    if re.search(re.escape(simplify_str_to_ascii(token.lower())),
                 simplify_str_to_ascii(abstract.lower()), re.IGNORECASE) is not None:
        return True
        
    if check(token, lang):
        return True
        
    return False


def is_valid_keyphrase(keyphrase: str, abstract: str, lang: str) -> bool:
    for token in re.split(r'\s+', keyphrase):
        if not is_valid_token(token.strip(string.punctuation), abstract, lang):
            break
    else:
        return True
    
    pred = ftlangdetect.detect(keyphrase, low_memory=True)

    return pred["lang"] == lang and pred["score"] > 0.6


def uniformize_lang_en_fr(lang_l: [str, list]) -> [None, str]:
    if len(lang_l) == 0:
        return None
    lang_l = [lang_l] if type(lang_l) is str else lang_l
    n2u = {"english": "en", "anglais": "en", "en": "en", "en_": "en", "engl": "en", "angl": "en",
           "french": "fr", "fran": "fr", "fr": "fr", "fr_": "fr", "fre": "fr", "fra": "fr", "fr": "fr"}
    uniform = "other"
    for nn, uu in n2u.items():
        for lang in lang_l:
            if nn in lang.lower()[:len(nn)]:
                uniform = uu
                break
    return uniform


def simplify_str_to_ascii(string: str) -> str:
    return unidecode(string)
