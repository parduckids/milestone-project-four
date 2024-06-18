from django.shortcuts import render

# custom 404 error handler
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# # custom 500 error handler
# def custom_500(request):
#     return render(request, '500.html', status=500)

# custom 403 error handler
def custom_403(request, exception):
    return render(request, '403.html', status=403)

# custom 400 error handler
def custom_400(request, exception):
    return render(request, '400.html', status=400)