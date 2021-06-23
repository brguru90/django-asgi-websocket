from django.http import HttpResponse

def test(request):
    return HttpResponse("test api", content_type="text")