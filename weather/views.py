from django.views.generic import TemplateView
import requests

class WeatherView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        city = request.POST.get('city')
        if city:
            try:
                api_key = 'your_api_key_here'
                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
                response = requests.get(url)
                weather = response.json()

                if weather.get('cod') == 200:
                    context['data'] = {
                        'city': city,
                        'country_code': weather['sys']['country'],
                        'coordinate': f"{weather['coord']['lon']}, {weather['coord']['lat']}",
                        'temp': f"{weather['main']['temp']} °C",
                        'pressure': weather['main']['pressure'],
                        'humidity': weather['main']['humidity'],
                    }
                else:
                    context['data'] = {'error': weather.get('message', 'City not found!')}

            except Exception as e:
                context['data'] = {'error': str(e)}
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
