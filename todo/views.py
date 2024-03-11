from django.shortcuts import render,HttpResponse,redirect
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    
    context = {
        'tasks':tasks,
        'total' : tasks.count(),
        'Completed' : tasks.filter(status=True).count(),
        'Incompleted' : tasks.filter(status=False).count(),
    }
    return render(request,'index.html',context)

def about_us(request):
    return render(request,'about_us.html')

def create_task(request):
    error=''
    if request.method=='POST':
        name = request.POST.get('name')
        if name=="":
            error ='Something  is required!!'
            context={
             'error':error
             }
            return  render(request,'create_task.html',context)
            
        description = request.POST.get('description')
        Task.objects.create(name=name,description=description).save()
            
        return redirect('/')

    return  render(request,'create_task.html')



def mark(request,pk):
    task = Task.objects.get(pk=pk)
    task.status = True if  not task.status else False
    task.save()
    return redirect('/')

def delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')


# def add(request):
#     redirect('/create')
#     task = Task.objects.all()
#     task.name= input("Enter the new Name of this Task:")
#     task.description = input("Enter a Description for this Task:")
#     task.save()
#     return redirect('/')

def edit(request,pk): 
    task = Task.objects.get(pk=pk)
    context = {
        'task' : task
    }
    if request.method=="POST":
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/')
    return render(request,"edit.html",context)

       
            