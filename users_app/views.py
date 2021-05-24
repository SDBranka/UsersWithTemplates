from django.shortcuts import redirect, render, HttpResponse
from .models import users


# Create your views here.
def index(request):
    context = {
        "all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)

def process_form(request):
    if request.method == "POST":
        users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email_address'], age = request.POST['age'])
        return redirect('/')
    else:
        return redirect('/')


# def process(request):
#     if request.method == 'POST':
#         request.session['name'] = request.POST['name']
#         request.session['location'] = request.POST['location']
#         request.session['favLang'] = request.POST['favLang']
#         request.session['travel'] = request.POST['travel']
#         request.session['music'] = request.POST['music']
#         request.session['comment'] = request.POST['comment']
#         # for key, value in request.session.items():
#         #     print(key, value)           #prints all key/value pairs in the terminal
#         return redirect('/result')