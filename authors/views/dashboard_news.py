

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from authors.forms.news_form import AuthorNewsForm
from news.models import New


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch')
class DashboardNews(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_news(self, id=None):
        new = None

        if id is not None:
            new = New.objects.get(
                is_published=False,
                author=self.request.user,
                pk=id,
            )

            if not new:
                raise Http404()

        return new

    def render_news(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_news.html',
            context={
                'form': form, })

    def get(self, request, id=None):

        new = self.get_news(id)

        form = AuthorNewsForm(instance=new)

        return self.render_news(form)

    def post(self, request, id=None):
        new = self.get_news(id)

        form = AuthorNewsForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=new
        )

        if form.is_valid():
            new = form.save(commit=False)

            new.author = request.user
            new.text_post_html = False
            new.is_published = False

            new.save()
            messages.success(request, 'Sua publicação foi salva com sucesso!')
            return redirect(reverse('authors:dashboard'))

        return self.render_news(form)


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch')
class DashboardNewsDelete(DashboardNews):
    def post(self, *args, **kwargs):
        new = self.get_news(self.request.POST.get("id"))
        new.delete()
        messages.success(self.request, 'Deletado com Sucesso')
        return redirect(reverse('authors:dashboard'))
