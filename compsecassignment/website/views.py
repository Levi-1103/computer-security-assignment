from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RequestForm
from django.contrib import messages
from django.views.generic.list import ListView

from .models import Request


def index(request):
    return render(request, 'index.html')

@login_required
def staff_view(request):
    if request.user.is_staff:
        req_list = Request.objects.all()
        context = {'req_list': req_list}
        return render(request, 'staff_view.html', context)
    else:
        return render(request, 'not_staff.html')

@login_required
def request_view(request):
    if request.method == "POST":

        form = RequestForm(request.POST,request.FILES)
        if form.is_valid():
            user_req = form.save(commit= False)
            user_req.user = request.user
            user_req.save()
            
            return HttpResponseRedirect("/")
    else:
        form = RequestForm()
    return render(request, 'request_view.html', {"form": form})



class RequestListView(ListView):
    model = Request