from django import template
# from qas.models import *

register = template.Library()

@register.filter(is_safe=True)
def lastName(name):
    """Removes all values of arg from the given string"""
    return name.split(' ')[-1]

@register.filter
def responseFromQuestion(candidate,question):
    try:
        return candidate.response_set.values_list('response_text').get(question_id=question.id)[0]
    except:
        return None

@register.filter
def lookup(d, key):
    return d[key]

@register.filter
def sortLastName(d):
    getKey = lambda x: x.name.split(' ')[-1]
    sortedList = sorted(d, key=getKey)
    return sortedList
