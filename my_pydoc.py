import django
import pydoc
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ListaTareas.settings')
django.setup()
pydoc.cli()