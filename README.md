# NLP Hebrew Analyzer Demo 
Development of a computational tool for identifying unusual discourse of children

This tool is an NLP project in Hebrew.

It is running on local Django server.

## Requirements

* Python 3.6 and above.
* Pip
* Pickeled classification model
* Google API key 
* Hebrew Parser Token

## Installation

1. Clone repo/ download the project.
2. Run: 
   ```
   pip install -r requirements.txt
   ```
3. Provide pickeld model and locate it under backend folder.

   Pay attention to call this model in the exact name: "model.sav"
   
   
## Running Demo from command line

1. Cd into the project folder
2. Run:
   ```
   python manage.py runserver
   ```
3. In the browser go to: http://127.0.0.1:8000/analyze/
4. Fill in the text bar a sentence in Hebrew
5. Press on "Process" 


## Tools In used

[Google Search API](https://serpapi.com/)

[Hebrew Parser](https://www.langndata.com/heb_parser/demo)


 ![alt-text](https://github.com/rikiNeustadt/Digi-Safe/blob/master/Demo.gif)
