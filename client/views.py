from importlib.resources import _

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView

from .form import RaqamForms
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Raqam

def delete(request, id):
    model = Raqam.objects.get(id=id)
    model.delete()
    messages.error(request, "Qushilgan Malumot Uchirildi")
    return redirect('index')

def search(request):
    model = Raqam()
    number = Raqam.objects.all()
    form = RaqamForms(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    if request.method == "POST":
        search = request.POST['search']
        venues = Raqam.objects.filter(name__contains=search)
        return render(request, 'main/index.html',
                      {'search': search,
                       'venues': venues,
                       'number':number,
                       "form": form})



def index(request):
    model = Raqam()
    number = Raqam.objects.all()
    form = RaqamForms(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    ctx = {
        'number':number,
        "form": form
    }
    return render(request,'main/index.html',ctx)

class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Royxatdan o'tish !")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })


    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, ("Siz muvaffaqiyatli ro'yxatdan o'tdingiz !! "))
            return redirect('index')


        return render(request, 'layouts/form.html', {
            'form': form
        })




class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, "layouts/form.html", {
            "form": LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if not user is None:
                login(request, user)
                messages.success(request, ("Xush kelibsiz, {}!".format(user.username)))

                return redirect("index")

            form.add_error("password", ("Login yoki parol notoʻgʻri."))

        return render(request, "layouts/form.html", {
            "form": form
        })

@login_required
def clinet_logout(request):
    messages.success(request, "Xayr {}!".format(request.user.username))
    logout(request)
    request.button_title = _("Saqlash")
    return redirect("loginn")
