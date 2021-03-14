import os
from static_ranges import Ranges
from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')

application = Ranges(Cling(MediaCling(get_wsgi_application())))
