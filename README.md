# FMRuleEngine
Fantastic Mind Rule Engine micro-service using Flask and Django backend

## Usage - Adding Rules
Rules can be added by defining them in the `rules.py` folder found inside the `scripts` folder. Rules added to the script can then be trigged by adding them to the `setup.py` script.

## Usage - Parsing calls
First run the application script by running `python app.py`. Once launched calls can by parsed via the url, For now this uses a GET method for testing. A POST method will be utilised for later versions. Once a call is parsed it will then return the results from parsing into the rule engine. It is hosted using Flask.

