from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm ,JobForm
from .filters import JobFilter

from django.contrib.auth.decorators import login_required




# Create your views here.
#model query set
#i want to return all jobs where is it ?? in model so i imported the job class
def job_list(request):
    job_list =Job.objects.all()


    filter = JobFilter(request.GET, queryset=job_list)
    job_list=filter.qs

    p = Paginator(job_list, 2)  # creating a paginator object
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    #context : usint variable from here to html page
    #context={name in html : name_variable}
    context ={'jobs' :page_obj ,'p' :p ,'filter':filter}

    return render(request ,'job/job_list.html',context)

#id for job what i want


def job_detail(request ,slug):
    #using id to get the detecte job
    job_detail=Job.objects.get(slug =slug)

    if request.method =='POST':
        form =ApplyForm(request.POST ,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False) 
            myform.job =job_detail
            myform.save()

    else :
        form =ApplyForm()


    context={'job' :job_detail , 'form':form}
    return render(request ,'job/job_details.html',context)


@login_required
def add_job(request):
    if request.method == 'POST' :
        form =JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.ownerr = request.user
            myform.save()
            return redirect(reverse('jobs:job_list' ,))
        
    else : 
        form =JobForm()

    return render(request , 'job/add_job.html',{'form' : form})