from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

#def home(request):
#	return render(request, 'home.html', {})


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	cats = Category.objects.all
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()	
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


		

def enviarAdmin(request):
    return redirect('/admin')

def bloquearUsuarios(request):
    return render(request, "bloquearUsuarios.html")

def listarUsers(request):
    users = User.objects.all()
    contexto = {
        'users':users
    }
    return render(request,'listarUsers.html',contexto)

def search(request):
	# allPosts = Post.objects.all()
	search = request.GET['search']
	allPosts = Post.objects.filter(post_date=search)
	params = {'allPosts': allPosts}
	return render(request, "search.html",params)



def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	# fields = '__all__'

class AddCommentView(CreateView):
	model = Comment
	#form_class = PostForm
	template_name = 'add_comment.html'
	fields = '__all__'

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')