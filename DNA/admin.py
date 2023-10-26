from django.contrib import admin
from .models import User
from .models import Types
from .models import Menu
from .models import Basket

admin.site.register(User)
admin.site.register(Types)
admin.site.register(Menu)
admin.site.register(Basket)