from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Article,Comment
from .forms import CommentForm
from django.http import request
from django.contrib.auth.decorators import login_required
# Create your views here.
#class ArticleView()
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title','body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_view.html'
    login_url = 'login'

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_Detail.html"
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title','body']
    template_name = "article_update.html"
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()         #return article author
        return obj.author == self.request.user   #check whether current_obj is equal to author

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
    login_url = 'login'                            #if user is not logged in then before deleting he/she has to login

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

@login_required
def post_detail(request,pk):
    article = get_object_or_404(Article,pk=pk)
    new_comment = None
    print(request.user.username)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article_c = article
            new_comment.author_c = request.user.username
            #new_comment.author_c_id = article.pk
            #print(new_comment)
            new_comment.save()
            return redirect('article_view',pk=article.pk)
    else:
        comment_form = CommentForm()
    return render(request,'comment.html',{'new_comment':new_comment,'comment_form':comment_form})
