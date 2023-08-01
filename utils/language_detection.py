import importlib


fasttext = langid = lstm_langid = None


def init(model: str) -> None:
    if model == "fasttext":
        global fasttext
        if fasttext is None:
            fasttext = importlib.import_module("fasttext_tools")
        
    elif model == "langid":
        global langid
        if langid is None:
            langid = importlib.import_module("langid")
        
    elif model == "lstm_langid":
        global lstm_langid
        if lstm_langid is None:
            lstm_langid = importlib.import_module("LanguageIdentifier")


def detect(text: str, model: str = "fasttext") -> str:
    init(model)
    
    if model == "fasttext":
        return fasttext.detect(text, low_memory=True)["lang"]
        
    elif model == "langid":
        return langid.classify(text)[0]
        
    elif model == "lstm_langid":
        return lstm_langid.predict(text)