from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

def login(request):
    return render(request, 'login.html')
@staff_member_required
def add(request):
    return render(request, 'cadastroUsuario.html')

@require_POST
def usuario_novo(request):
    try:
        usuario_aux = User.objects.get(username=request.POST['usuario'])
        if usuario_aux:
            return render(request, '/usuarios/add/', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = request.POST['usuario']

        novoUsuario = User.objects.create_user(username=usuario, email=email, password=senha)
        novoUsuario.first_name = nome
        novoUsuario.save()
        return redirect ('/contas/login/')

@login_required
def usuario_edita(request):
    data = {}
    usuario = request.user
    form = UsuarioEditaForm(request.POST or None, instance=request.user)
    data['usuario'] = usuario
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #return redirect('/projetos/')
    else:
        return render(request, 'editaUsuario.html', data)
