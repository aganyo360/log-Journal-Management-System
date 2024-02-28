from django.shortcuts import render, redirect
from .forms import TopicForm
from . models import Topic

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

def new_topic(req):
    if req.method !='POST':
        #no data submitted, create a blank form
        form = TopicForm()
    else:
        #process data  post data submitted
        if form.is_valid():
            #the is_valid option checks whether the form is valid so that it can be submitted to the db
            form.save()
            return redirect('ljApp:topics')
        #since the form has been processed successfully then redirect to topics section
    context ={'form':form}

    return render(req, 'ljApp/new_topic.html', context)

