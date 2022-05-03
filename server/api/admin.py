from django.contrib import admin
from .models import User, FoodData, IntakeData, WaterConsumption

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'name']


class IntakeDataAdmin(admin.ModelAdmin):
    list_display = ['id','date', 'email']


class FoodDataAdmin(admin.ModelAdmin):
    list_display = ['id','item', 'calories']


class WaterAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'date']



admin.site.register(User, UserAdmin)
admin.site.register(IntakeData, IntakeDataAdmin)
admin.site.register(FoodData, FoodDataAdmin)
admin.site.register(WaterConsumption, WaterAdmin)