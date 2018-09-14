from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

from catalogo.models import prodCad


def catalogo(request):


    dita = prodCad.objects.filter(Q(marcabusca__exact="-"))

    paginator = Paginator(dita, 28)
    page = request.GET.get('page')

    try:
        dita = paginator.page(page)

    except:
        dita = paginator.page(1)

    context = {
        'dita': dita,
        'id': id
    }


    return render(request, 'catalogo.html', context)

