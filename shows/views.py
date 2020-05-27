from django.shortcuts import render, get_object_or_404, redirect
from .models import Shows
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ShowsModelForm
from comments.models import Comment
from comments.forms import CommentModelForm
from django.contrib.auth.decorators import login_required
from PIL import Image
# Create your views here.


def shows_list_view(request):
    if request.user.is_authenticated:
        queryset = Shows.objects.published()
    else:
        queryset = Shows.objects.published()[:5]
    context = {
        'queryset': queryset,
        'all': False,
        'live-action': False,
        # 'tv-series': False,
        'animation': False,
    }
    context[request.path.split('/')[-2]] = True
    if context['live-action']:
        if request.user.is_authenticated:
            queryset = Shows.objects.published().filter(animation=False)
        else:
            queryset = Shows.objects.published().filter(animation=False)[:2]
    if context['animation']:
        if request.user.is_authenticated:
            queryset = Shows.objects.published().filter(animation=True)
        else:
            queryset = Shows.objects.published().filter(animation=True)[:2]

    # if request.user.is_authenticated:
    #     qs = Shows.objects.all()
    #     queryset = (queryset | qs).distinct()
    context['queryset'] = queryset
    return render(request, 'shows/shows_list.html', context)


@login_required
def show_create_view(request):
    form = ShowsModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        img = obj.image
        image = Image.open(f'media/{img}')
        image.thumbnail((300, 300))
        image.save(f'media/{img}', 'JPEG')
        form = ShowsModelForm()
    context = {
        'form': form
    }
    return render(request, 'shows/show_create.html', context)


@login_required
def show_update_view(request, username, slug):
    obj = get_object_or_404(Shows, slug=slug, user__username__exact=username)
    form = ShowsModelForm(request.POST or None,
                          request.FILES or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
    context = {
        'form': form
    }
    return render(request, 'shows/show_create.html', context)


@login_required
def show_delete_view(request, username, slug):
    obj = get_object_or_404(Shows, slug=slug, user__username__exact=username)
    if request.POST:
        obj.delete()
        return redirect('/shows/all/')
    context = {
        'obj': obj,
    }
    return render(request, 'shows/show_delete.html', context)


def show_detail_view(request, username, slug):
    obj = get_object_or_404(Shows, slug=slug, user__username__exact=username)

    comments = Comment.objects.filter(
        slug=obj.slug, commented_to__exact=username)
    form = CommentModelForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.slug = obj.slug
            form_obj.commented_to = obj.user
            form_obj.user = request.user
            form_obj.save()
            form = CommentModelForm()

    context = {
        'obj': obj,
        "form": form,
        'comments': comments
    }
    return render(request, 'shows/show_detail.html', context)
