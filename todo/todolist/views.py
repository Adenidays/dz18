from django.shortcuts import render,  redirect
from .models import TodoList


def first_page(request):
    sort_order = request.GET.get('sort')
    if sort_order == 'date':
        tasks = TodoList.objects.order_by('start_deadline')
    elif sort_order == 'priority':
        tasks = TodoList.objects.order_by('priority')
    elif sort_order == 'name':
        tasks = TodoList.objects.order_by('task_name')
    else:
        tasks = TodoList.objects.all()

    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def delete_task(request, task_id):
    task = TodoList.objects.get(id=task_id)
    task.delete()
    return redirect('first_page')




def edit_task(request, task_id):
    task = TodoList.objects.get(id=task_id)

    if request.method == 'POST':

        task.task_name = request.POST.get('task_name')
        task.task_description = request.POST.get('task_description')
        task.start_deadline = request.POST.get('start_deadline')
        task.deadline = request.POST.get('deadline')
        task.priority = request.POST.get('priority')
        task.status = bool(request.POST.get('status'))
        task.save()
        return redirect('first_page')

    context = {'task': task}
    return render(request, 'change.html', context=context)



def crate_post(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        start_deadline = request.POST.get('start_deadline')
        deadline = request.POST.get('deadline')
        priority = request.POST.get('priority')
        status = request.POST.get('status') == 'on'

        task = TodoList(task_name=task_name,
                        task_description=task_description,
                        start_deadline=start_deadline,
                        deadline=deadline,
                        priority=priority,
                        status=status)
        task.save()

        return redirect('first_page')

    return render(request, 'new_post.html')
