from django.contrib import admin
from .models import Cold
from .models import Hot
from .models import Dessert
from .models import Snacks

admin.site.register(Cold)
admin.site.register(Hot)
admin.site.register(Dessert)
admin.site.register(Snacks)