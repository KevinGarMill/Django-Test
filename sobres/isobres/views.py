from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

# Create your views here.

def mainpage(request):
    return render_to_response("principal.html", {
        'appname': "electrosobres",
        'titlepage': "sobres",
        'author': "Luis Barcenas"
    })


def dashboard(request, usuario):
    try :
        user = User.objects.get(username=usuario)
    except:
        raise Http404("El usuario no esta")

    sobres = user.sobre_set.all()
    template = get_template("dashboard.html")
    variables = Context({
        'username': usuario,
        'author': "Luis Barcenas",
        'sobres': sobres
    })

    page = template.render(variables)
    return HttpResponse(page)
