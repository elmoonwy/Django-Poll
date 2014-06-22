# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice

def index(request):
	# latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {
	# 	'latest_poll_list': latest_poll_list
	# 	})
	# return HttpResponse(template.render(context))
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	return render(request, 'polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request,poll_id):
	# try:
	# 	poll = Poll.objects.get(pk = poll_id)
	# except Poll.DoesNotExist:
	# 	raise Http404
	# return render(request, 'polls/detail.html', {'poll':poll})
	poll = get_object_or_404(Poll, pk = poll_id)
	return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk = poll_id)
	return render(request, 'polls/result.html', {'poll':poll})

def vote(request,poll_id):
	p = get_object_or_404(Poll, pk = poll_id)
	try:
		selected_choice = p.choice_set.get(pk = request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'poll':p,
			'error_message':"You did't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))