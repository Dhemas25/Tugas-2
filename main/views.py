from django.shortcuts import render

# Create your views here.
def show_main(request):
    # Data yang akan dikirimkan ke tampilan HTML

    context = {
        'name': 'Dhemas Wicaksono Nugroho',  
        'class': 'PBP E',
    }

    return render(request, "main.html", context)
