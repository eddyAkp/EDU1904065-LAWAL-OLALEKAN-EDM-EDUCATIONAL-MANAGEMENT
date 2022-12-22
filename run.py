import os

os.system("python -m venv . && cd Scripts && activate.bat && cd .. && cd src && python -m pip install -r requirements.txt && python manage.py migrate && python manage.py runserver 2332")

# Open the correct webpage
