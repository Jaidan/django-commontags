=================
Django CommonTags
=================

Common useful django template tags and filters

Getting Started
===============

Simply install, add to your INSTALLED_APPS setting and use {% load common_filters common_tags %} in your templates to enable access to the tags and filters

Installing
==========

You can get Django Commontags by using pip or easy_install::

 $ pip install django-commontags
 or
 $ easy_install django-commontags

If you want to install it from source, grab the git repository from github and run setup.py::

 $ git clone git://github.com/Jaidan/django-commontags.git
 $ cd django-commontags
 $ python setup.py install 

Included Tags and Filters
=========================

Tags
----

divide
  Allows division of two numbers within a template.  Accepts a numerator,
  denominator, and optional format string.  Be aware that the format string
  cannot be a string literal and must be a context variable that contains
  the format string

dynamic_regroup
  Extends the built in regroup tag to allow regrouping by a attribute named
  by a context variable's value. Accepts an iterable, th vairable to be
  resolved to an attribute name, and the variable to write the result into. 

Filters
-------

percentage
  Takes a value converts it to a float and returns the result formatted
  as a percentage.  Accepts an integer for number of decimal places.

truncatechars
  Takes a string value and truncates it to a given number of chars. 
  Appends "..." to the truncated value.  Accepts an integer for the number
  of characters to truncate to

partition
  Break a list into ``n`` pieces. The last list may be larger than the 
  rest if the list doesn't break cleanly. That is::

    >>> l = range(10)

    >>> partition(l, 2)
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]

    >>> partition(l, 3)
    [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]

    >>> partition(l, 4)
    [[0, 1], [2, 3], [4, 5], [6, 7, 8, 9]]

    >>> partition(l, 5)
    [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

lookup
  Looks up a value from a dictionary.  This allows dictionary look ups
  based on a context variables value.  Accepts the name to lookup.

unslugify
  Attempts to roughly unslugify a string.  Replaces '-' and '_' with ' '
