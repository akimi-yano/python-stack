from django.shortcuts import render, HttpResponse, redirect
import random 
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

def process_money(request, location):

    # if request.method == "POST":
    #     val_from_forms= request.POST["which_form"]

    # if val_from_forms == 'farm':
    if location == 'farm':
        if 'addition' in request.session:
             del request.session['addition'] 
        request.session['addition'] = random.randint(10,20)
        request.session['gold'] = request.session['gold'] + request.session['addition'] 
        result = f"Earned {request.session['addition']} golds from the farm! "
  
    # if val_from_forms == 'cave':
    if location == 'cave':
        if 'addition' in request.session:
            del request.session['addition'] 
        request.session['addition'] = random.randint(5,10)
        request.session['gold'] = request.session['gold'] + request.session['addition'] 
        result = f"Earned {request.session['addition']} golds from the cave! "

    # if val_from_forms == 'house': 
    if location == 'house':
        if 'addition' in request.session:
            del request.session['addition']      
        request.session['addition'] = random.randint(2,5)
        request.session['gold'] = request.session['gold'] + request.session['addition'] 
        result = f"Earned {request.session['addition']} golds from the house! "
       
    # if val_from_forms == 'casino':
    if location == 'casino':
        if 'addition' in request.session:
            del request.session['addition'] 
        request.session['addition'] = random.randint(-50, 50)
        if request.session['addition']<0:
            result = f"Entered a casino and lost {-1*request.session['addition']} golds... Ouch... " 
        elif request.session['addition']>0:
            result = f"Entered a casino and gained {request.session['addition']} golds! " 
        else: 
            result = f"Entered a casino and did not gain anything but {request.session['addition']} golds "
        request.session['gold'] = request.session['gold'] + request.session['addition'] 

    if 'activities' not in request.session:
        request.session['activities'] = []
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['activities'].append([result, time])

    if 'attempts' not in request.session:
        request.session['attempts'] = 1
    elif 'attempts' in request.session:
        request.session['attempts'] += 1
    return redirect('/')

def rules(request):
    if request.method == "POST" and 'goal' not in request.session and 'moves' not in request.session:
        request.session['goal']= int(request.POST['goal'])
        request.session['moves']= int(request.POST['moves'])
        request.session['attempts'] = 0
    return redirect('/')
    
