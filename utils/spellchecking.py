import enchant


# stores already opened enchant.Dict
lang_dicts = dict()


def check(text: str, lang: str) -> bool:

    if lang in lang_dicts:
        return lang_dicts[lang].check(text)

    try:
        lang_dicts[lang] = enchant.Dict(lang)
    except:
        raise ValueError(f'No dictionary available for language \'{lang}\'')

    return lang_dicts[lang].check(text)
