from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . forms import CreateForm


class PostListView(ListView):
	model = Post
	template_name = 'content/home.html'

	# loopable variable
	context_object_name = 'posts'



class PostDetailView(DetailView):
	model = Post
	context_object_name = 'posts'
	


class PostCreateView(LoginRequiredMixin, CreateView):

	model = Post
	form_class = CreateForm

	# fields = ['title', 'challenge_type', 'description', 'link', 'last_reg_date', 'poster']
	success_url = '/'
	def form_valid(self, form):
		form.instance.college = self.request.user
		form.save()
		return super().form_valid(form)
	def form_invalid(self, form):
		print(form.errors)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = CreateForm

	# fields = ['title', 'challenge_type', 'description', 'link', 'last_reg_date', 'poster']
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.college:
			return True
		else:
			return False

	def form_valid(self, form):
		form.instance.college = self.request.user
		return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.college:
            return True
        return False



def about(request):
    return render(request, 'content/about.html', {'title': 'About'})


