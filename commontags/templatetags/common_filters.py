from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def percentage(value, arg=2):
    try:
        return ('{0:.%s%%}' % arg).format(float(value))
    except ValueError:
        # Unable to parse value
        return None

@register.filter
@stringfilter
def truncatechars(value, arg):
    """
    Truncates a string after a certain number of letters

    Arguement: Number of letters to truncate after
    """
    try:
        length=int(arg)
    except ValueError:
        pass
    if not isinstance(value, basestring):
        value = str(value)
    if len(value) > length:
        value = value[:length-3] + '...'
    return value

@register.filter
def partition(thelist, n):
    """
    Break a list into ``n`` pieces. The last list may be larger than the rest if the list doesn't break cleanly. That is::

        >>> l = range(10)

        >>> partition(l, 2)
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

        >>> partition(l, 3)
        [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

        >>> partition(l, 4)
        [[0, 1], [2, 3], [4, 5], [6, 7, 8, 9]]

        >>> partition(l, 5)
        [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

    """
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p*i:p*(i+1)] for i in range(n - 1)] + [thelist[p*(i+1):]]

@register.filter
def lookup(d, index):
    try:
        return d[index]
    except KeyError:
        return ''

@register.filter
@stringfilter
def unslugify(value):
    return value.replace('-', ' ').replace('_', ' ')
