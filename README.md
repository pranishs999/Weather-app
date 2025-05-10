# Weather App with Django

This is a simple weather app built using Django that fetches current weather data from the OpenWeatherMap API. The app allows users to search for weather details by city and displays the current temperature, pressure, humidity, and weather description.

## Features

- **Current Weather**: Displays the current weather information such as temperature, pressure, humidity, and weather description for today.
- **User Input**: Allows the user to input a city name to get weather data for that location.

## Tech Stack

- **Django**: Web framework to build the app.
- **OpenWeatherMap API**: Provides weather data (current conditions).
- **HTML/CSS**: For front-end design.
- **TailwindCSS**: For styling the app.
- **Flowbite**: For additional UI components.

## Requirements

- Python 3.x
- Django 5.x.y or higher
- An OpenWeatherMap API key (free plan available)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```
2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

   ```
4. **Setup environment variables**:
   -Create an .env file in the root of the project and add your OpenWeatherMap API key.

   ```bash
   api_key='your_api_key_here'
   ```
5. **Run the migrations (to setup the database)**:

   ```bash
   python manage.py migrate
   ```
6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```
7. **Access the app**:

   - Open a browser and go to http://127.0.0.1:8000/

## How to Use
   1. On the homepage, enter the name of a city in the input field and click the Get Weather button.
   2. The current weather data for that city will be displayed, including temperature, pressure, humidity, and description.
   3. Only the weather for today is shown, with no forecast for future days.

## Example
   For example, if you enter London:
      - The current weather will display:
         - Temperature: 21.44°C
         - Pressure: 1016 hPa
         - Humidity: 32%
         - Weather: Clear sky

## Project Structure
   ```bash
      weather-app/
      ├── manage.py
      ├── weather/
      │   ├── migrations/
      │   ├── __init__.py
      │   ├── admin.py
      │   ├── apps.py
      │   ├── models.py
      │   ├── tests.py
      │   ├── views.py
      │   └── templates/
      │       └── index.html
      ├── requirements.txt
      └── README.md 
   ```

## Troubleshooting
   1. Invalid API Key Error (401):

      - Ensure you have entered a valid OpenWeatherMap API key in your .env file.
      - Sign up for a free API key at OpenWeatherMap.

   2. No Data Returned:

      - Ensure the city name is correct. The API will return an error message if the city is not found.

## License
   This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
   - OpenWeatherMap for providing the weather API.
   - Django for the web framework.
   - Tailwind CSS for styling the app.
   - Flowbite for additional UI components.