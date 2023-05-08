from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm

# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Muestra todo los topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Muestra un unico topic y todos sus items"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # Post data submitted 
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)