import datetime

def dateNow(request):
    return {'dateNow':datetime.datetime.now()}