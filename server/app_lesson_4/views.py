from django.http import HttpResponse


def index(request):
    return HttpResponse("Homework for lesson 4.")


index = lambda request: HttpResponse("Homework for lesson 4.")  # why not?
