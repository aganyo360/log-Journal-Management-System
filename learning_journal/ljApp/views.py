from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from . models import Topic, Entry

# Create your views here.
def index(request):
    return render(request, 'ljApp/index.html' )
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context={
        'topics':topics
    }
    return render(request, 'ljApp/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'ljApp/topic.html', context)

def new_topic(request):
    if request.method !='POST':
        #no data submitted, create a blank form
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        #process data  post data submitted
        if form.is_valid():
            #the is_valid option checks whether the form is valid so that it can be submitted to the db
            form.save()
            return redirect('ljApp:topics')
        #since the form has been processed successfully then redirect to topics section
    context ={'form':form}

    return render(request, 'ljApp/new_topic.html', context)
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method !='POST':
        form= EntryForm()        
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()            
            return redirect('ljApp:topic', topic_id=topic_id)
    
    context ={'topic':topic, 'form':form}
    return render(request, 'ljApp/new_entry.html', context)
        
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        
    return render(request, 'ljApp/edit_entry.html')


