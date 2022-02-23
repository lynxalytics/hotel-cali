from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import mixins

from .models import Comment


class CommentListView(generic.ListView):
    model = Comment
    context_object_name = 'comments'
    paginate_by = 20
    ordering = ['-created_at']
    template_name = "comments/comments_list.html"


class CommentCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['text']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('comment-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommentUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Comment
    fields = ['text']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('comment-list')


class CommentDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('comment-list')
