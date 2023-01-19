from django.shortcuts import render

# Create your views here.
def test(request):
    context = {
        'title':' O Influencio',
      }
    return render (request,'qr/test.html', context )
