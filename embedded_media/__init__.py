__author__ = 'Derek Payton <derek.payton@gmail.com>'
__copyright__ = 'Copyright (c) Derek Payton'
__description__ = 'Directly embed CSS and JS in Django forms media.'
__version__ = '0.0.1'
__license__ = 'MIT License'

try:
    import django
except ImportError:
    pass
    #we are pip installing
else:
    from .media import CSS, JS

