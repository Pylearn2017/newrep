from django.shortcuts import render, HttpResponse
from . models import Bb, Rubric


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    print(rubrics)
    contex = {
        'bbs':bbs, 'rubrics': rubrics
    }
    print(bbs)
    return render(request, 'bboard/templates/index.html', contex)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/templates/by_rubric.html', context)