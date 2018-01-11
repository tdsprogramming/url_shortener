# system imports
import string
import random

# django imports
from django.db import models
from django.urls import reverse_lazy

# project imports
from .utils import format_user_input

URL_SHORT_LENGTH = 7
LOCAL_DOMAIN = 'localhost:8000/'

class Url(models.Model):
    user_input = models.CharField(max_length=1500)
    url_redirect_to = models.CharField(max_length=1500)
    shortened_url_ending = models.CharField(max_length=URL_SHORT_LENGTH)
    shortened_url_full = models.CharField(max_length=(50 + URL_SHORT_LENGTH))

    def __str__(self):
        return self.user_input

    def get_absolute_url(self):
        return reverse_lazy('urls:detail', kwargs={'shortened_url_ending':self.shortened_url_ending})

    def save(self, *args, **kwargs):
        temp = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(URL_SHORT_LENGTH))
        shortened_url_endings = Url.objects.filter(shortened_url_ending=temp)
        while shortened_url_endings:
            temp="".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(URL_SHORT_LENGTH))
            shortened_url_endings = Url.objects.filter(shortened_url_ending=temp)
        self.shortened_url_ending = temp
        self.url_redirect_to = format_user_input(self.user_input)
        self.shortened_url_full = (LOCAL_DOMAIN + str(self.shortened_url_ending))
        super(Url, self).save(*args, **kwargs)
