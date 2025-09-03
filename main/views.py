from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406345186',
        'name': 'Muhammad Derriel Ramadhan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
