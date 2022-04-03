from django.shortcuts import render
from django.http import HttpResponse

#models
from .models import Professor

# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
#serializers
from .serializers import (
    ProfessorSerializer
)


@api_view(['GET'])
def getProfessors(request):
    context={}
    professors=Professor.objects.all().order_by('department__name')
    if professors.count()>0:
        context['status']="found"
    else:
        context['status']="not found"

    serializers=ProfessorSerializer(professors,many=True)
    context['professors']=serializers.data
    return Response(context)

