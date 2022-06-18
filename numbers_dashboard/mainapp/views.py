from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.response import TemplateResponse


class IndexView(View):

    def get(self, request):
        r = request.method
        # return render(request, 'mainapp/index.html', {})
        return HttpResponse('hello')



