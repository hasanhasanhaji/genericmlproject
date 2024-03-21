from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def predictdata_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        pass
