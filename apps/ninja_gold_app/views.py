from django.shortcuts import render, HttpResponse, redirect
import random, datetime

def index(request):
    print("///////////////////////////////////")
    print("RUNNING INDEX FUNCTION")
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'activities':request.session['activities'],
        'gold': request.session['gold']
    }    
    return render(request,'ninja_gold_app/index.html', context)


# def index():
#     if 'activities' not in session:
#         session['activities'] = []
#     if 'gold' not in session:
#         session['gold'] = 0
#     return render_template('index.html', color=session['color'])



def process_money(request):
    if request.method == 'POST':

        if request.POST['building'] == "farm":
            winnings = random.randrange(10, 21)
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)

        elif request.POST['building'] == "cave":
            winnings = random.randrange(5, 11)
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)
        elif request.POST['building'] == "house":
            winnings = random.randrange(2, 6)
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {datetime.datetime.now()}</p>"
            request.session['activities'].insert(0,activity)
        else:
            winnings = random.randrange(-50, 50)
            if winnings < 0:
                activity = f"<p style='color:red'>Earned {winnings} from {request.POST['building']} at {datetime.datetime.now()}</p>"
            else:
                activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {datetime.datetime.now()}</p>"
            
            request.session['activities'].insert(0,activity)

        request.session['gold'] += winnings

    return redirect('/')

def clear_funds(request):
    request.session.clear()
    return redirect('/')