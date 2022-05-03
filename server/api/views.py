import json
from django.http import JsonResponse
from .models import FoodData, IntakeData, User, WaterConsumption
from .serializers import FoodDataSerializer, UserSerializer, IntakeDataSerializer, WaterCountSerializer
from django.views.decorators.csrf import csrf_exempt

def food_search(request, query):
    foods = FoodData.objects.filter(item__icontains=query)
    sd = FoodDataSerializer(foods, many=True)
    return JsonResponse({"data": sd.data})

@csrf_exempt
def user_signin(request):
    data = json.loads(request.body)
    email = data['data']['email']
    name = data['data']['name']
    user = User.objects.filter(email=email).exists()
    if(not user):
        user = User(email = email, name = name)
        user.save()
    return JsonResponse({"message":"user signed in"})


def user_detail(request, email):
    user = User.objects.get(email=email)
    sd = UserSerializer(user)
    return JsonResponse({"user":sd.data})

@csrf_exempt
def add_intake(request):
    data = json.loads(request.body)['data']
    date = data.get('date')
    time = data.get('time')
    email = data.get('email')
    item = data.get('item')
    quantity = data.get('quantity')
    calorie = data.get('calorie')
    protein = data.get('proteins')
    carb = data.get('carbs')
    fat = data.get('fats')
    fiber = data.get('fiber')
    obj = IntakeData(date=date, email=email,time=time , item=item, quantity=quantity, calorie=calorie, proteins=protein, carbs=carb, fats=fat, fiber=fiber)
    obj.save()
    return JsonResponse({"message":"Data Added"})


@csrf_exempt
def update_intake(request, id):
    data = json.loads(request.body)
    item = data.get('item')
    quantity = data.get('quantity')
    calorie = data.get('calorie')
    obj = IntakeData.objects.filter(id=id) 
    obj.update(item=item, quantity=quantity, calorie=calorie)
    return JsonResponse({"message":"Data Updated"})

def get_data(request):
    data = json.loads(request.body)
    date = data.get('date')
    email = data.get('email')
    obj = IntakeData.objects.filter(email=email, date=date)
    sd = IntakeDataSerializer(obj, many=True)
    return JsonResponse({"data":sd.data})

@csrf_exempt
def user_update(request, email):
    data = json.loads(request.body)
    data = data['data']
    user = User.objects.filter(email=email)
    user.update(gender=data['gender'], height=data['height'], weight=data['weight'], age=data['age'], activity=data['activity'])
    return JsonResponse({"message":"user updated"})

def get_main_data(request, email,date):
    obj = IntakeData.objects.filter(email=email, date=date)
    sd = IntakeDataSerializer(obj, many=True)
    return JsonResponse({"message":sd.data})


def get_time_data(request, email,date, time):
    obj = IntakeData.objects.filter(email=email, date=date, time=time)
    sd = IntakeDataSerializer(obj, many=True)
    return JsonResponse({"data":sd.data})

@csrf_exempt
def delete_item(request, id):
    obj = IntakeData.objects.filter(id=id)
    obj.delete()
    return JsonResponse({"message":"Removed"})

def inc_count(request, email, date):
    obj = WaterConsumption.objects.filter(email=email, date=date).exists()
    if(not obj):
        ob = WaterConsumption(email = email, date=date, counts = 1)
        ob.save()
    else:
        ob = WaterConsumption.objects.get(email=email, date=date)
        sd = WaterCountSerializer(ob)
        curr_count = sd.data['counts']
        ob.counts = curr_count+1
        ob.save()
    return JsonResponse({"message":"updated"})


def dec_count(request, email, date):
    ob = WaterConsumption.objects.get(email=email, date=date)
    sd = WaterCountSerializer(ob)
    curr_count = sd.data['counts']
    ob.counts = curr_count-1
    ob.save()
    return JsonResponse({"message":"updated"})

def get_count(request, email, date):
    count = 0
    try:
        ob = WaterConsumption.objects.get(email=email, date=date)
        sd = WaterCountSerializer(ob)
        count = sd.data['counts']
    except:
        count = 0
    return JsonResponse({"message":count})