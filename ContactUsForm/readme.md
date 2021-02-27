## for using this app you need to install the python software in your terminal and the pip package 
## then create a virtual environment using virtualenv <name>
# After this activate the virtual Environment using
'''
source venv/bin/activate
'''
## install the requirement.txt by using
'''
pip install requirements.txt
'''
### after activating this you have to migrate the models using
'''
python manage.py makemigrations
python manage.py migrate
'''

### Use >>>python manage.py createsuperuser to create a user 

# After all this use 
'''
python manage.py runnserver

''' 
## Open browser and go to http://127.0.0.1:8000/

## for admin panel use http://127.0.0.1:8000/admin and login

