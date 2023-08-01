# Keyphrase Generation Dataset

## Installation

To setup your environment, run:

	python3 -m pip install -r requirements.txt

## Metadata Harvesting

To collect the metadata from an OAI-PMH enabled server, use the script *extract.py* as follows:

	python3 extract.py URL OUTPUT_FILE
	
URL must be an url pointing to a OAI-PMH server. OUTPUT_FILE is a path to a jsonlines file where the data will be stored.
	
The default format used for harvesting is *oai_db* (Dublin Core). Every OAI-PMH server at minima provides the *oai_db* format.
However, the *description* tag provided in *oai_db* format does not differentiate between abstracts and other kinds of descriptions.
Therefore it is preferable to use another format such as *qdb* (Qualified Dublin Core) when possible.

A format can be specified by using the *-f* (or *--format*) parameter. Currently *extract.py* only provide support for *oai_db* and *qdb*.

	python3 extract.py --format qdb URL OUTPUT_FILE

## Processing and Language Detection

Next you need to process the data. This includes the automatic detection of the languages for the abstracts and keyphrases. To process a file, run:

	python3 process.py INPUT_FILE --output OUTPUT_FILE
	
INPUT_FILE is the jsonlines file created in the previous step. OUTPUT_FILE is another jsonlines file which will contain the language metadata.
If no OUTPUT_FILE is provided, the program will create one with a default name in the same repository as INPUT_FILE.

This script uses the *pyenchant* library to check the validity of a keyphrase for a given language. You need to have dictionary packages for each language installed on your system.
For example, *hunspell-fr* for french, *hunspell-de-de* for german or *hunspell-is* for icelandic. If no dictionary is available for a language, the script will default to using fasttext.