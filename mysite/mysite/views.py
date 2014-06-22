from django.shortcuts import render

def test_404_view(request):
	return render(request, '404.html', {'info':'can not found the page'})