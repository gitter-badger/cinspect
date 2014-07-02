""" A startup script for IPython to patch it to 'inspect' using cinspect. """

# Place this file in ~/.ipython/<PROFILE_DIR>/startup to patch your IPython to
# use cinspect for the code inspection.

import inspect

from cinspect import getsource, getfile

import IPython.core.oinspect as OI
from IPython.utils.py3compat import cast_unicode

old_find_file = OI.find_file
old_getsource = inspect.getsource

inspect.getsource = getsource

def patch_find_file(obj):
    fname = old_find_file(obj)
    if fname is None:
        try:
            fname = cast_unicode(getfile(obj))
        except:
            pass
    return fname

OI.find_file = patch_find_file
