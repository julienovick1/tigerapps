"""
http://djangosnippets.org/snippets/847/
"""
from django import template
from django.utils.encoding import force_unicode

register = template.Library()

@register.filter
def in_group(user, groups):
    """Returns a boolean if the user is in the given group, or comma-separated
    list of groups.

    Usage::

        {% if user|in_group:"Friends" %}
        ...
        {% endif %}

    or::

        {% if user|in_group:"Friends,Enemies" %}
        ...
        {% endif %}

    """
    group_list = force_unicode(groups).split(',')
    return user.groups.filter(name__in=group_list).exists()
