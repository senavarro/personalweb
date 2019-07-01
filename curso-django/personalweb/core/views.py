from django.shortcuts import render, HttpResponse

html_base = """
<h1>My personal website</h1>
<ul>
	<li><a href="/">Homepage</a></li>
	<li><a href="/about-me">About me</a></li>
	<li><a href="/portfolio">Portfolio</a></li>
	<li><a href="/contact">Contact</a></li>
</ul>


"""
# Create your views here.
def home(request):
	return render(request, "core/home.html")

def about(request):
	return render(request, "core/about_me.html")

def portfolio(request):
	return render(request, "core/portfolio.html")

def contact(request):
	return render(request, "core/contact.html")
