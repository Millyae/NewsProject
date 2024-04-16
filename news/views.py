from django.views.generic import (ListView, DetailView, CreateView, View)
from .models import News
from .filters import NewsFilter
from .forms import NewsForms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView

class NewsList(ListView):
    model = News
    ordering = '-created_at'
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 10

    def form_valid(self, form):
        form.instance.type = 'новость'
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

class NewsCreate(CreateView):
    form_class = NewsForms
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

class NewsUpdate(UpdateView):
    form_class = NewsForms
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')

class NewsDelete(DeleteView):
    form_class = NewsForms
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.get_object()
        return context

class NewsSearch(View):
    def get(self, request):
        news_filter = NewsFilter(request.GET, queryset=News.objects.all())
        return render(request, 'news_search.html', {'filter': news_filter})