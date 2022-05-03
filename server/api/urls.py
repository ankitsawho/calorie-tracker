from django.urls import path
from .views import dec_count, food_search, get_count, get_main_data, inc_count, user_signin, user_detail, add_intake, update_intake, get_data, user_update,get_main_data, get_time_data,delete_item
urlpatterns = [
    path('search/<str:query>', food_search),
    path('user/', user_signin),
    path('user_detail/<str:email>', user_detail),
    path('add/', add_intake),
    path('update/<int:id>', update_intake),
    path('get-data/', get_data),
    path('user-update/<str:email>/', user_update),
    path('get-main-date/<str:email>/<str:date>',get_main_data),
    path('get-time-data/<str:email>/<str:date>/<str:time>',get_time_data),
    path('delete-item/<int:id>', delete_item),
    path('inc-count/<str:email>/<str:date>', inc_count),
    path('dec-count/<str:email>/<str:date>', dec_count),
    path('get-count/<str:email>/<str:date>', get_count),
]
