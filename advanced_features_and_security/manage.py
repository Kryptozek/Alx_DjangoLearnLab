#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import YourModel  # Replace with your app and model names

# Get the content type for the model
content_type = ContentType.objects.get_for_model(YourModel)

# Create groups
editors_group, _ = Group.objects.get_or_create(name='Editors')
viewers_group, _ = Group.objects.get_or_create(name='Viewers')
admins_group, _ = Group.objects.get_or_create(name='Admins')

# Define permissions
view_permission = Permission.objects.get(content_type=content_type, codename='view_yourmodel')
create_permission = Permission.objects.get(content_type=content_type, codename='add_yourmodel')
edit_permission = Permission.objects.get(content_type=content_type, codename='change_yourmodel')
delete_permission = Permission.objects.get(content_type=content_type, codename='delete_yourmodel')

# Assign permissions to groups
editors_group.permissions.add(view_permission, create_permission, edit_permission)
viewers_group.permissions.add(view_permission)
admins_group.permissions.add(view_permission, create_permission, edit_permission, delete_permission)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
