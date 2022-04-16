# FlatManager
FlatManager is basically a type of CRM, on using this program you can add flat, owner, rentier, agent etc. and create a rent agreement from this data. All of these features are created in a multi-relational database .
This project also uses frameworks like django bootstrap form to create forms and django filter to create search options.
Also tests are very important in this project, I created over 40 tests.

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
next install requirements
```
pip install -r requirements.txt
```
and now runserver by command
```
python manage.py runserver     
```
You will be automatically get "Starting development server at http://127.0.0.1:8000/", and now go into home page at Starting development server at http://127.0.0.1:8000/home

### how to start tests
if u install requirements go into flat_manager folder and make command
```
pytest tests.py
```
