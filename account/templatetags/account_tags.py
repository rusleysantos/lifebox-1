from django import template
from django.contrib.auth.models import User
#from social_django.models import UserSocialAuth

register = template.Library()


@register.simple_tag
def total_people():
    return User.objects.count()
