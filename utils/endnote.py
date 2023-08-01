import builtins

from typing import TextIO, Iterator, Dict, Any, List


TAG_KEY_MAPPING: Dict[str, str] = {
    "%A": "author",
    "%B": "secondary title",
    "%C": "place published",
    "%D": "year",
    "%E": "secondary author",
    "%F": "label",
    "%G": "language",
    "%H": "translated author",
    "%I": "publisher",
    "%J": "journal name",
    "%K": "keywords",
    "%L": "call number",
    "%M": "accession number",
    "%N": "number",
    "%O": "alternate title",
    "%P": "pages",
    "%Q": "translated title",
    "%R": "doi",
    "%S": "tertiary title",
    "%T": "title",
    "%U": "url",
    "%V": "volume",
    "%W": "database provider",
    "%X": "abstract",
    "%Y": "tertiary author",
    "%Z": "notes",
    "%0": "reference type",
    "%1": "custom 1",
    "%2": "custom 2",
    "%3": "custom 3",
    "%4": "custom 4",
    "%6": "number of volumes",
    "%7": "edition",
    "%8": "date",
    "%9": "type of work",
    "%?": "subsidiary author",
    "%@": "isbn",
    "%!": "short title",
    "%#": "custom 5",
    "%$": "custom 6",
    "%]": "custom 7",
    "%&": "section",
    "%(": "original publication",
    "%)": "reprint edition",
    "%*": "reviewed item",
    "%+": "author address",
    "%^": "caption",
    "%>": "file attachments",
    "%<": "research notes",
    "%[": "access date",
    "%=": "custom 8",
    "%~": "name of database"
}

LIST_TYPE_TAGS: List[str] = [
    "%K"
]


class Reader():

    _file: TextIO

    def __init__(self, file: TextIO) -> None:
        self._file = file
        
    def read(self) -> Dict[str, Any]:
        line = self._file.readline()
        if line == "": return None
        
        entry = dict()
        
        while line != "\n" and line != "":
            key = line[:2]
            content = line[3:].strip()
            
            if key in LIST_TYPE_TAGS:
                content = content.split(', ')
                
            entry[TAG_KEY_MAPPING[key]] = content
            line = self._file.readline()
            
        return entry
        
    def __iter__(self) -> Iterator[Any]:
        while True:
            entry = self.read()
            if entry is None:
                break
            yield entry
            
    def close(self) -> None:
        self._file.close()
    
    
def open(path: str) -> Reader:
    return Reader(builtins.open(path, 'r'))