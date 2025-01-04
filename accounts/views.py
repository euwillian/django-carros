from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Este form já está pronto no Django, basta utiliza-lo.


def register_view(request):
    if request.method == "POST":
        user_form  = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request=request, 
                  template_name='register.html', 
                  context={'user_form': user_form})