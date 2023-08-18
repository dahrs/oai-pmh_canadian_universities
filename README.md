# OAI-PMH Canadian Universities Repositories Extractor

Our script requires the use of Python 3.7 or superior. 
In case of version error, try to replace the python command with python3.
e.g.

    python3 -m pip install -r requirements.txt

instead of

    python -m pip install -r requirements.txt 

---

## Installation

To setup your python environment, run:

	python -m pip install -r requirements.txt

---

## Metadata Harvesting

To collect the metadata from all Canadian OAI-PMH enabled servers, run the script *Extract_all_Canada.py* as follows:

	python Extract_all_Canada.py --out_path [PATH]
	
*\[PATH\]* must be path to the directory where we wish to save the dataset. 
By default *\[PATH\]* is set to the current path.
