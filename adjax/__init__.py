
from adjax.decorators import adjax_response
from adjax.base import get_store

# The following functions are mirrored for convenience and unity
from django.contrib.messages import success, info, warning, error, debug


__all__ = ('adjax_response', 'success', 'info', 'warning', 'error', 'debug', 
            'redirect', 'update', 'form', 'replace', 'hide', 'extra')


# Adjax API 
# The following functions form the Adjax API.

def update(request, obj, attributes=None):
    """ Sends the updated version of the given attributes on the given object. 
        If no attributes are given, all attributes are sent (be careful if you don't want all data to be public).
        If a minus sign is in front of an attribute, it is omitted.
        A mix of attribtue names with and without minus signs is just silly. No other attributes will be included.
    """
    store = get_store(request)
    if not attributes or all(map(lambda s: s.startswith("-"), attributes)):
        attributes = obj.__dict__.keys()
    store.update(obj, (a for a in attributes if not a.startswith("-")))

def form(request, form_obj):
    get_store(request).form(form_obj)

def replace(request, element, html):
    get_store(request).replace(element, html)

def redirect(request, path):
    get_store(request).redirect(path)

def hide(request, element):
    get_store(request).hide(element)

def extra(request, key, value):
    get_store(request).extra(key, value)


