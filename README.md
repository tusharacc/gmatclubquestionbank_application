# gmatclubquestionbank_application
The project uses Python, HTML &amp; Javascript to build a question bank for gmat SC &amp; CR section.

Below are the steps to execute the the application:
1. Execute the python scripts - 
  a.Execute questionslink.py. The python script will download 100 question for all the section and categorize based on complexity.
  b. Execute getquestionandanswer.py. The python script will read the link from file generated in previous step and create a JSON. This file needs to be manually modified.
2. In step 1.b, a json file is generated, section_complexity_question_detail.txt (such as CR_HIGH_question_detail). Copy the file content and create 
a cr_json.js or sc_json.js and paste the content. The variable name should be CRJSON_HIGH or CRJSON_LOW so on and so forth.
3. Fire up, index.html
