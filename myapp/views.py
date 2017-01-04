from django.shortcuts import render, get_object_or_404
from .models import Workout
from .forms import PostFormWorkout
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.


def workout_list(request):
    workouts = Workout.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/workout_list.html', {'workouts': workouts})


def workout_detail(request, pk):
    post = get_object_or_404(Workout, pk=pk)
    return render(request, 'blog/workout_detail.html', {'workout': post})


def workout_edit(request, pk):
    post = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        form = PostFormWorkout(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('workout_detail', pk=post.pk)
    else:
        form = PostFormWorkout(instance=post)
    return render(request, 'blog/workout_edit.html', {'form': form})


def workout_new(request):
    if request.method == "POST":
        form = PostFormWorkout(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('workout_detail', pk=post.pk)
    else:
        form = PostFormWorkout()
    return render(request, 'blog/workout_edit.html', {'form': form})
