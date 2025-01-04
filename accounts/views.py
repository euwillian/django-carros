from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# função para autenticação pronta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Vai verificar se o usuário existe e senha é correta
        
        if user is not None:
            # Pode fazer o login de sessão
            login(request, user)
            # função pronta
            
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
        # Retorna o form vázio
    return render(request=request,
                  template_name='login.html',
                  context={'login_form': login_form})

  
def logout_view(request):
    logout(request)
    return redirect('cars_list')