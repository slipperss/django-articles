from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'main/index.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/detail_view.html'
    context_object_name = 'article'

class NewsChangeView(UpdateView):
    model = Articles
    template_name = 'main/change.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView, UpdateView):
    model = Articles
    template_name = 'main/delete.html'
    form_class = ArticlesForm
    success_url = '/'

def about(request):
    return render(request, 'main/about.html')

def createnews(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверно введена'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createnews.html', data)