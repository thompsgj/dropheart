import os
import django
import random

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.dropheart.settings")
django.setup()

from django.contrib.auth.models import User

first_names = ["James", "Jakob", "Min", "Bob", "Dragon"]
last_names = ["Brooklyn", "Grazy", "Corn", "Fragment", "Graze"]

def create_users():
    for i in range(5):
        username = f"{random.choice(first_names)}_{random.choice(last_names)}"
        password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
        user = User.objects.create_user(username=username, password=password)
        user.save()
        print(f"User {user.username} created successfully.")

if __name__ == "__main__":
    create_users()