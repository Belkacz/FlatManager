# FlatManager
FlatManager is basically type of CRM, on using this program u can add flat, owner, rentier, agent etc. and create rent agreement from this data. All of this features are created in multi relational database . 
This project also use fremorks like django bootstrap formto creates forms and django fillter to create search option. 
Also tests are very important in this project, i crete over 40 tests to check if evrything is ok.

#How to start
first u need to install python and clone project by
```
git clone https://github.com/Belkacz/FlatManager
```
after this create and activate new environment 
```
python3 -m venv my_env
source my_env/bin/activate   
```
next install requeierments 
```
pip install -r requirements.txt
```
and now runserver by command
```
python manage.py runserver     
```
You will be automaticly get "Starting development server at http://127.0.0.1:8000/", and now go into home pyge at Starting development server at http://127.0.0.1:8000/home

### how to start tests
if u install requirements go into flat_manager folder nad make command 
```
pytest tests.py
```
