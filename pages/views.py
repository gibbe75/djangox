from django.views.generic import TemplateView


class HomePageView(request):
	messages.success(request, 'Cadeau supprimé.')

    return render(request, 'pages/home.html')


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'