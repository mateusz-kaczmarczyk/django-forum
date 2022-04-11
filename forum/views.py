from .models import Comment, Subforum, Thread
from users.models import Profile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, ThreadForm


def home(request):
    context = {
        'forums': get_main_page_context(),
    }
    return render(request, 'forum/home.html', context)

class SubforumDetailView(DetailView):
    model = Subforum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subforums = Subforum.objects.filter(parent=self.kwargs['pk'])
        for subforum in subforums:
            subforum.threadsNum = Thread.objects.filter(subforum=subforum.id).count()
        context['subforums'] = subforums
        threads = Thread.objects.filter(subforum=self.kwargs['pk'])
        for thread in threads:
            thread.commentsNum = Comment.objects.filter(thread=thread.id).count()
        context['threads'] = threads
        return context

class ThreadDetailView(DetailView):
    model = Thread

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = Thread.objects.filter(id=self.object.pk).first()
        profile = Profile.objects.filter(user=thread.author).first()
        thread.author.profile = profile
        context['author'] = thread.author
        context['comments'] = Comment.objects.filter(thread=thread.id)
        return context

class ThreadCreateView(LoginRequiredMixin, CreateView):
    form_class = ThreadForm
    template_name = 'forum/thread_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.subforum = Subforum.objects.get(id=self.kwargs['subforum_id'])
        return super().form_valid(form)

class ThreadUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/thread_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        thread = self.get_object()
        if self.request.user == thread.author:
            return True
        return False

class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thread
    template_name = 'forum/thread_delete.html'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse_lazy('subforum-detail', kwargs={'pk':self.object.subforum.id})

class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'forum/comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thread = Thread.objects.get(id=self.kwargs['thread_id'])
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'forum/comment_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thread = Thread.objects.get(id=self.kwargs['thread_id'])
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'forum/comment_delete.html'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('thread-detail', kwargs={'pk':self.object.thread.id})


def get_main_page_context():
    main_forums = Subforum.objects.filter(parent_id=None)
    for forum in main_forums:
        forum.subforums = Subforum.objects.filter(parent_id=forum.id)
        for subforum in forum.subforums:
            subforum.links = Subforum.objects.filter(parent_id=subforum.id)
    return main_forums