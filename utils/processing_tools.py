import jsonlines
import os
#import langdetect
import re
import ftlangdetect

from tqdm import tqdm

from typing import TextIO, List, Dict, Any, Callable

    
def clean_up_abstracts(abstracts: List[str]) -> List[str]:
    # removes line jumps and supernumerary spaces
    for i, abstract in enumerate(abstracts):
        abstracts[i] = re.sub("\s+", " ", abstract)
        
    # removes empty abstracts
    abstracts = [a for a in abstracts if len(a) != 0]
        
    return abstracts
    
def clean_up_keyphrases(keyphrases: List[str]) -> List[str]:
    new_keyphrases = []
    for kp in keyphrases:
        new_keyphrases += [k.strip() for k in kp.split('; ')]
    keyphrases = new_keyphrases
    
    # removes empty keyphrases
    keyphrases = [kp for kp in keyphrases if len(kp) != 0]
        
    return keyphrases
    
def basic_preprocessing(entry: Dict[str, Any]) -> Dict[str, Any]:
    entry["abstract"] = clean_up_abstracts(entry["abstract"])
    entry["keyphrases"] = clean_up_keyphrases(entry["keyphrases"])
    return entry
    
def detect_lang(text: str) -> str:
    #return langdetect.detect(k)
    return ftlangdetect.detect(text=text, low_memory=True)["lang"]
    
def process_file(input_file_path: str, output_file_path: str,
        preprocessing: Callable[[Dict[str, Any]], Dict[str, Any]] = None,
        postprocessing: Callable[[Dict[str, Any]], Dict[str, Any]] = None,
        input_filter: Callable[[Dict[str, Any]], bool] = None) -> None:

    print("Processing file: " + input_file_path)
    
    with jsonlines.open(output_file_path, 'w') as f_out:
        for entry in tqdm(jsonlines.open(input_file_path)):
            
            if preprocessing is not None: entry = preprocessing(entry)
            entry = basic_preprocessing(entry)
            
            if input_filter is not None and not input_filter(entry): continue
        
            try:
                keyphrases_lang = [detect_lang(k) for k in entry["keyphrases"]]
            except Exception as e:
                print("\nException while running language detection for keyphrases: " + str(entry["keyphrases"]))
                print(" -> " + str(e))
                print("Line skipped...")
                continue
                
            processed_entry = {"languages": []}
            
            for abstract in entry["abstract"]:
                try:
                    abstract_lang = detect_lang(abstract)
                    selected_kp = []
                    
                    for i, kp in enumerate(entry["keyphrases"]):
                        if re.search(re.escape(kp), abstract, re.IGNORECASE) is not None or keyphrases_lang[i] == abstract_lang:
                            selected_kp.append(kp)
                            
                    if len(selected_kp) > 0:
                        processed_entry["languages"].append({"lang": abstract_lang, "abstract": abstract, "keyphrases": selected_kp})
                except Exception as e:
                    short_abs = abstract if len(abstract) <= 50 else abstract[:47] + '...'
                    print("\nException while running language detection for abstract: " + short_abs)
                    print(' -> ' + str(e))
                    print("Abstract skipped...")
                    continue
            
            if len(processed_entry["languages"]) > 0:
                if postprocessing is not None: processed_entry = postprocessing(processed_entry)
                f_out.write(processed_entry)


def subject_to_domain(subject: [str, list]) -> str:
    subject = [subject] if type(subject) is str else subject
    domain = ''
    return domain
