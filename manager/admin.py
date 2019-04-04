# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models.models import Country,State,Town,Source,Profile,User,Articles

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Town)
admin.site.register(Source)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Articles)

