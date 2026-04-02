import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import PodcastShow, Episode, PodSubscriber


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['podcastshow_count'] = PodcastShow.objects.count()
    ctx['podcastshow_technology'] = PodcastShow.objects.filter(category='technology').count()
    ctx['podcastshow_business'] = PodcastShow.objects.filter(category='business').count()
    ctx['podcastshow_education'] = PodcastShow.objects.filter(category='education').count()
    ctx['podcastshow_total_rating'] = PodcastShow.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['episode_count'] = Episode.objects.count()
    ctx['episode_draft'] = Episode.objects.filter(status='draft').count()
    ctx['episode_scheduled'] = Episode.objects.filter(status='scheduled').count()
    ctx['episode_published'] = Episode.objects.filter(status='published').count()
    ctx['podsubscriber_count'] = PodSubscriber.objects.count()
    ctx['podsubscriber_apple'] = PodSubscriber.objects.filter(platform='apple').count()
    ctx['podsubscriber_spotify'] = PodSubscriber.objects.filter(platform='spotify').count()
    ctx['podsubscriber_google'] = PodSubscriber.objects.filter(platform='google').count()
    ctx['recent'] = PodcastShow.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def podcastshow_list(request):
    qs = PodcastShow.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'podcastshow_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def podcastshow_create(request):
    if request.method == 'POST':
        obj = PodcastShow()
        obj.title = request.POST.get('title', '')
        obj.host = request.POST.get('host', '')
        obj.category = request.POST.get('category', '')
        obj.episodes = request.POST.get('episodes') or 0
        obj.subscribers = request.POST.get('subscribers') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/podcastshows/')
    return render(request, 'podcastshow_form.html', {'editing': False})


@login_required
def podcastshow_edit(request, pk):
    obj = get_object_or_404(PodcastShow, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.host = request.POST.get('host', '')
        obj.category = request.POST.get('category', '')
        obj.episodes = request.POST.get('episodes') or 0
        obj.subscribers = request.POST.get('subscribers') or 0
        obj.rating = request.POST.get('rating') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/podcastshows/')
    return render(request, 'podcastshow_form.html', {'record': obj, 'editing': True})


@login_required
def podcastshow_delete(request, pk):
    obj = get_object_or_404(PodcastShow, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/podcastshows/')


@login_required
def episode_list(request):
    qs = Episode.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'episode_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def episode_create(request):
    if request.method == 'POST':
        obj = Episode()
        obj.title = request.POST.get('title', '')
        obj.show_title = request.POST.get('show_title', '')
        obj.episode_number = request.POST.get('episode_number') or 0
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.published_date = request.POST.get('published_date') or None
        obj.downloads = request.POST.get('downloads') or 0
        obj.status = request.POST.get('status', '')
        obj.audio_url = request.POST.get('audio_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/episodes/')
    return render(request, 'episode_form.html', {'editing': False})


@login_required
def episode_edit(request, pk):
    obj = get_object_or_404(Episode, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.show_title = request.POST.get('show_title', '')
        obj.episode_number = request.POST.get('episode_number') or 0
        obj.duration_mins = request.POST.get('duration_mins') or 0
        obj.published_date = request.POST.get('published_date') or None
        obj.downloads = request.POST.get('downloads') or 0
        obj.status = request.POST.get('status', '')
        obj.audio_url = request.POST.get('audio_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/episodes/')
    return render(request, 'episode_form.html', {'record': obj, 'editing': True})


@login_required
def episode_delete(request, pk):
    obj = get_object_or_404(Episode, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/episodes/')


@login_required
def podsubscriber_list(request):
    qs = PodSubscriber.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(platform=status_filter)
    return render(request, 'podsubscriber_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def podsubscriber_create(request):
    if request.method == 'POST':
        obj = PodSubscriber()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.subscribed_shows = request.POST.get('subscribed_shows', '')
        obj.platform = request.POST.get('platform', '')
        obj.subscribed_date = request.POST.get('subscribed_date') or None
        obj.status = request.POST.get('status', '')
        obj.listens = request.POST.get('listens') or 0
        obj.save()
        return redirect('/podsubscribers/')
    return render(request, 'podsubscriber_form.html', {'editing': False})


@login_required
def podsubscriber_edit(request, pk):
    obj = get_object_or_404(PodSubscriber, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.subscribed_shows = request.POST.get('subscribed_shows', '')
        obj.platform = request.POST.get('platform', '')
        obj.subscribed_date = request.POST.get('subscribed_date') or None
        obj.status = request.POST.get('status', '')
        obj.listens = request.POST.get('listens') or 0
        obj.save()
        return redirect('/podsubscribers/')
    return render(request, 'podsubscriber_form.html', {'record': obj, 'editing': True})


@login_required
def podsubscriber_delete(request, pk):
    obj = get_object_or_404(PodSubscriber, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/podsubscribers/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['podcastshow_count'] = PodcastShow.objects.count()
    data['episode_count'] = Episode.objects.count()
    data['podsubscriber_count'] = PodSubscriber.objects.count()
    return JsonResponse(data)
