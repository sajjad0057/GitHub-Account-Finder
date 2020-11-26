from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    user = False
    if request.method == 'POST':
        username = request.POST.get('username')
        url = 'https://api.github.com/users/' + str(username)
        response = requests.get(url)
        user = response.json()

    return render(request,'index.html',context={'user':user})


def geo(request):
    pass
    # is_cached = ('geodata' in request.session)
    #
    # if not is_cached:
    #     ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    #     print('sajjjjjjjjjjjjad',ip_address)
    #     response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    #     request.session['geodata'] = response.json()
    #
    # geodata = request.session['geodata']
    return render(request,'geo.html',)
