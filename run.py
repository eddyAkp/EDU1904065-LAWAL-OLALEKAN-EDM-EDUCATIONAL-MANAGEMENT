import os

os.system("cd src")
os.system("Scripts/activate.ps1")
os.system("python pip install -r requirements.txt")
os.system("python manage.py runserver 2332")

# Open the correct webpage
