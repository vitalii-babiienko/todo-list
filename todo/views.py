from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from todo.forms import TagForm, TaskForm
from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "task_list"
    paginate_by = 5

    def post(self, request):
        pk = request.POST.get("pk")

        task = get_object_or_404(Task, id=pk)
        task.is_completed = not task.is_completed
        task.save()

        return HttpResponseRedirect(self.request.path)


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
