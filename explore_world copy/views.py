from django.http import HttpResponse

def hello_srm(request):
    return HttpResponse("Hello SRM!")