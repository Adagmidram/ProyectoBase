from django.http import HttpResponse
from django.template import Template, Context

def _index_ (request): # Vista
    html_ext=open("D:/Proyectos/ProyectoBase/PJBase/PJBase/Templates/index.html")
    templ=Template(html_ext.read())
    html_ext.close()
    ctx=Context()
    documento=templ.render(ctx)
    return HttpResponse(documento)

    