import requests
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse

API_KEY = '5421e02b07d3b8a5484e71b06d17c006'

# Home view
def home(request):
    return render(request, 'weather/home.html')

# View Weather (Map View)
def view_weather(request):
    return render(request, 'weather/view_weather.html')

# Fetch weather data for the map
def fetch_weather_data(request):
    # Example country data for demo purposes
    countries = [
   {"name": "India", "lat": 20.5937, "lon": 78.9629},
    {"name": "USA", "lat": 37.0902, "lon": -95.7129},
    {"name": "Australia", "lat": -33.8688, "lon": 151.2093},
    {"name": "Brazil", "lat": -23.5505, "lon": -46.6333},
    {"name": "Canada", "lat": 45.4215, "lon": -75.6972},
    {"name": "Germany", "lat": 51.1657, "lon": 10.4515},
    {"name": "Japan", "lat": 36.2048, "lon": 138.2529},
    {"name": "UK", "lat": 51.5074, "lon": -0.1278},
    {"name": "France", "lat": 46.6034, "lon": 1.8883},
    {"name": "Russia", "lat": 55.7558, "lon": 37.6173},
    {"name": "China", "lat": 35.8617, "lon": 104.1954},
    {"name": "South Korea", "lat": 35.9078, "lon": 127.7669},
    {"name": "Mexico", "lat": 23.6345, "lon": -102.5528},
    {"name": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"name": "South Africa", "lat": -30.5595, "lon": 22.9375},
    {"name": "Argentina", "lat": -38.4161, "lon": -63.6167},
    {"name": "Spain", "lat": 40.4637, "lon": -3.7492},
    {"name": "Egypt", "lat": 26.8206, "lon": 30.8025},
    {"name": "Saudi Arabia", "lat": 23.8859, "lon": 45.0792},
    {"name": "Turkey", "lat": 38.9637, "lon": 35.2433},
    {"name": "Indonesia", "lat": -0.7893, "lon": 113.9213},
    {"name": "Nigeria", "lat": 9.082, "lon": 8.6753},
    {"name": "Pakistan", "lat": 30.3753, "lon": 69.3451},
    {"name": "Bangladesh", "lat": 23.685, "lon": 90.3563},
    {"name": "Vietnam", "lat": 14.0583, "lon": 108.2772},
    {"name": "Thailand", "lat": 15.8700, "lon": 100.9925},
    {"name": "Ukraine", "lat": 48.3794, "lon": 31.1656},
    {"name": "Kenya", "lat": -1.2921, "lon": 36.8219},
    {"name": "Colombia", "lat": 4.5709, "lon": -74.2973},
    {"name": "Algeria", "lat": 28.0339, "lon": 1.6596},
    {"name": "Poland", "lat": 51.9194, "lon": 19.1451},
    {"name": "Iraq", "lat": 33.2232, "lon": 43.6793},
    {"name": "Korea, North", "lat": 40.3399, "lon": 127.5101},
    {"name": "Romania", "lat": 45.9432, "lon": 24.9668},
    {"name": "Chile", "lat": -35.6751, "lon": -71.5430},
    {"name": "Peru", "lat": -9.1900, "lon": -75.0152},
    {"name": "Malaysia", "lat": 4.2105, "lon": 101.9758},
    {"name": "Singapore", "lat": 1.3521, "lon": 103.8198},
    {"name": "Ethiopia", "lat": 9.145, "lon": 40.4897},
    {"name": "Sudan", "lat": 12.8628, "lon": 30.8025},
    {"name": "Angola", "lat": -11.2027, "lon": 17.8739},
    {"name": "Uzbekistan", "lat": 41.3775, "lon": 64.5852},
    {"name": "Kazakhstan", "lat": 48.0196, "lon": 66.9237},
    {"name": "Venezuela", "lat": 6.4238, "lon": -66.5897},
    {"name": "Greece", "lat": 39.0742, "lon": 21.8243},
    {"name": "Czech Republic", "lat": 49.8175, "lon": 15.4720},
    {"name": "Hungary", "lat": 47.1625, "lon": 19.5033},
    {"name": "Belarus", "lat": 53.7098, "lon": 27.9534},
    {"name": "Austria", "lat": 47.5162, "lon": 14.5501},
    {"name": "Bulgaria", "lat": 42.7339, "lon": 25.4858},
    {"name": "Israel", "lat": 31.0461, "lon": 34.8516},
    {"name": "Jordan", "lat": 30.5852, "lon": 36.2384},
    {"name": "New Zealand", "lat": -40.9006, "lon": 174.8860},
    {"name": "Norway", "lat": 60.4720, "lon": 8.4689},
    {"name": "Finland", "lat": 61.9241, "lon": 25.7482},
    {"name": "Sweden", "lat": 60.1282, "lon": 18.6435},
    {"name": "Denmark", "lat": 56.2639, "lon": 9.5018},
    {"name": "South Sudan", "lat": 6.8777, "lon": 31.3070},
    {"name": "Zimbabwe", "lat": -19.0154, "lon": 29.1549},
    {"name": "Nepal", "lat": 28.3949, "lon": 84.1240},
    {"name": "Mali", "lat": 17.5707, "lon": -3.9962},
    {"name": "Mozambique", "lat": -18.6657, "lon": 35.5296},
    {"name": "Tanzania", "lat": -6.369028, "lon": 34.8888},
    {"name": "Madagascar", "lat": -18.7669, "lon": 46.8691},
    {"name": "Honduras", "lat": 13.9094, "lon": -83.4215},
    {"name": "Cuba", "lat": 21.5218, "lon": -77.7812},
    {"name": "Syria", "lat": 34.8021, "lon": 38.9968},
    {"name": "Lebanon", "lat": 33.8547, "lon": 35.8623},
    {"name": "Kuwait", "lat": 29.3759, "lon": 47.9774},
    {"name": "Qatar", "lat": 25.3548, "lon": 51.1839},
    {"name": "Bahrain", "lat": 25.9304, "lon": 50.6378},
    {"name": "Oman", "lat": 21.4735, "lon": 55.9754},
    {"name": "Armenia", "lat": 40.0691, "lon": 45.0382},
    {"name": "Azerbaijan", "lat": 40.1431, "lon": 47.5769},
    {"name": "Georgia", "lat": 42.3154, "lon": 43.3569},
    ]
    weather_data = []
    for country in countries:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={country['lat']}&lon={country['lon']}&appid={API_KEY}&units=metric"
        )
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                "name": country["name"],
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "rain": data.get("rain", {}).get("1h", 0),
                "lat": country["lat"],
                "lon": country["lon"],
            })
    return JsonResponse(weather_data, safe=False)

def compare_weather(request):
    if request.method == 'POST':
        countries = request.POST.getlist('countries')  # Get selected countries
        weather_data = []
        
        # Predefined latitude and longitude for countries
        country_coords = {
            "India": (20.5937, 78.9629),
            "USA": (37.0902, -95.7129),
            "Australia": (-33.8688, 151.2093),
            "Brazil": (-23.5505, -46.6333),
            "Canada": (45.4215, -75.6972),
            "Germany": (51.1657, 10.4515),
            "Japan": (36.2048, 138.2529),
            "UK": (51.5074, -0.1278),
            "France": (46.6034, 1.8883),
            "Russia": (55.7558, 37.6173),
            "China": (35.8617, 104.1954),
            # Add other countries and their lat/lon as needed
        }

        for country in countries:
            lat, lon = country_coords.get(country, (0, 0))
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            )
            if response.status_code == 200:
                data = response.json()
                weather_data.append({
                    "name": country,
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "rain": data.get("rain", {}).get("1h", 0),
                })
        return render(request, 'weather/weather_comparison.html', {'weather_data': weather_data})

    return render(request, 'weather/compare_weather.html')



# Search Weather
def search_weather(request):
    if request.method == 'POST':  # Use POST for the search form
        location = request.POST.get('location')
        if location:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
            )
            if response.status_code == 200:
                data = response.json()
                
                # Extract weather data
                weather_data = {
                    "name": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "pressure":data["main"]["pressure"],
                    "visibility":data["visibility"],
                }

                return render(request, 'weather/search_results.html', {'weather_data': weather_data})
            else:
                error_message = "Location not found or API error."
                return render(request, 'weather/search_weather.html', {'error_message': error_message})
    return render(request, 'weather/search_weather.html')

