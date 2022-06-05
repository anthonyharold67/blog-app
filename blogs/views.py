
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .forms import BlogForm, CommentForm
from .models import Blog, Like,Comment
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.

# class BlogCreateView(CreateView):
#     model = Blog
#     form_class = BlogForm
#     template_name = 'blogs/blog_create.html'
#     success_url = reverse_lazy('home')

@login_required
def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'blogs/blog_create.html', context)
    

class BlogListView(ListView):
    model = Blog
    # extra_context={'comments': Comment.objects.all()}
    template_name = 'blogs/blog_list.html'

# class BlogDetailView(DetailView):
#     model = Blog

@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    model = Blog 
    template_name = "blogs/blog_delete.html"
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blogs/blog_update.html"
    success_url = reverse_lazy('home')

@login_required(login_url='users/login')
def blog_like(request, id):
    blog = Blog.objects.get(id=id)
    like = Like.objects.get_or_create(user=request.user, blog=blog)

    blog.blog_like += 1
    blog.save()
    return redirect("blog_detail", id=id)
    

@login_required
def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=blog.id)
    blog.blog_view += 1
    blog.save()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = blog
            blog.blog_comment +=1 
            comment.user = request.user
            blog.blog_view -= 1
            blog.save()
            comment.save()
            return redirect("blog_detail", id)
    return render(request, 'blogs/blog_detail.html', {'blog': blog, 'comment_form': comment_form, 'comments': comments})



    