from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from board_body.models import Post, Stock
from .forms import PostForm, StockForm



def index(request):
    posts = Post.objects.all()
    stock = Stock.objects.all().last()
    return render(request, 'index.html', locals())


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_categories/man_boots.html'
    context_object_name = 'posts'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_crud/post_detail.html'
    context_object_name = 'post'
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={
            'pk': post_id})


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/create.html'
    success_url = reverse_lazy('index')



class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/update.html'
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('post_detail', kwargs={
            'pk': post_id})



class PostDeleteView(generic.DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'post_crud/delete.html'
    success_url = reverse_lazy('index')


class StockDetailView(generic.DetailView):
    model = Stock
    template_name = 'stock_crud/stock_detail.html'
    context_object_name = 'stock'
    def get_success_url(self):
        stock_id = self.kwargs['pk']
        return reverse_lazy('stock_detail', kwargs={
            'pk': stock_id})



class StockCreateView(generic.CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_crud/create.html'
    success_url = reverse_lazy('index')



class StockUpdateView(generic.UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_crud/update.html'
    def get_success_url(self):
        stock_id = self.kwargs['pk']
        return reverse_lazy('stock_detail', kwargs={
            'pk': stock_id})



class StockDeleteView(generic.DeleteView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_crud/delete.html'
    success_url = reverse_lazy('index')


class StockListView(generic.ListView):
    model = Stock
    template_name = 'stocks.html'
    context_object_name = 'stocks'




