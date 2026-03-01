from django.db import migrations
from django.contrib.auth.models import User
import os

def create_admin_user(apps, schema_editor):
    # This will create a superuser if it doesn't already exist
    # You can change these values after logging in
    username = "admin"
    email = "admin@example.com"
    password = "admin12345"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully.")

def remove_admin_user(apps, schema_editor):
    User.objects.filter(username="admin").delete()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0003_alter_homepage_id_alter_siteconfiguration_id'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, remove_admin_user),
    ]
