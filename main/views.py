from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Adrasa Cantya Salaka',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)