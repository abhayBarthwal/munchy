from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Bestseller)
admin.site.register(Display)
admin.site.register(Item)
admin.site.register(Orders)
admin.site.register(Weekly)