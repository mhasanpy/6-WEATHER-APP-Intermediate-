# weather_app.py
# import requests
# import json
# from datetime import datetime

class WeatherApp:
    def __init__(self):
         #IMPORTANT: Replace with your free API key from https://openweathermap.org/api
        # self.api_key = "YOUR_API_KEY_HERE"  # Get free key from OpenWeatherMap
        # self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        # self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        self.favorites = []
        self.load_favorites()
    
    def load_favorites(self):
        """Load favorite cities from file"""
        try:
            with open('favorites.json', 'r') as f:
                self.favorites = json.load(f)
        except FileNotFoundError:
            self.favorites = []
    
    def save_favorites(self):
        """Save favorite cities to file"""
        with open('favorites.json', 'w') as f:
            json.dump(self.favorites, f)
    
    def add_favorite(self, city):
        """Add city to favorites"""
        if city not in self.favorites:
            self.favorites.append(city)
            self.save_favorites()
            print(f"✅ {city} added to favorites!")
        else:
            print(f"⚠️ {city} already in favorites!")
    
    def get_weather(self, city):
        """Get current weather for any city worldwide"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Celsius
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                self.display_weather(data, city)
                
                # Ask to add to favorites
                add = input("\n📌 Add to favorites? (y/n): ").lower()
                if add == 'y':
                    self.add_favorite(city)
            else:
                print(f"❌ Error: {data.get('message', 'City not found')}")
                print("💡 Tip: Try using 'City,CountryCode' (e.g., 'London,UK' or 'Paris,FR')")
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
            print("💡 Please check your internet connection!")
    
    def display_weather(self, data, city):
        """Display weather information"""
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        # Get country code
        country = data['sys'].get('country', '')
        
        print("\n" + "="*50)
        print(f"🌍 WEATHER IN {city.upper()}{', ' + country if country else ''}")
        print("="*50)
        print(f"🌡️ Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"📉 Min: {temp_min}°C | 📈 Max: {temp_max}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"📊 Pressure: {pressure} hPa")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
        print(f"☁️ Conditions: {description.capitalize()}")
        
        # Add weather advice
        print("\n💡 Weather Advice:")
        if temp < 0:
            print("   🧣 It's freezing! Wear heavy winter clothes.")
        elif temp < 10:
            print("   🧥 It's cold! Wear a jacket.")
        elif temp < 20:
            print("   🧥 It's cool! A light jacket might be good.")
        elif temp < 30:
            print("   👕 Nice weather! Perfect for outdoor activities.")
        else:
            print("   🏖️ It's hot! Stay hydrated and use sunscreen.")
        
        if 'rain' in description.lower():
            print("   ☔ Don't forget your umbrella!")
        elif 'snow' in description.lower():
            print("   ⛄ Wear warm boots and drive carefully!")
        
        print("="*50)
    
    def get_forecast(self, city):
        """Get 5-day weather forecast"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(self.forecast_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                self.display_forecast(data, city)
            else:
                print(f"❌ Error: {data.get('message', 'City not found')}")
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
    
    def display_forecast(self, data, city):
        """Display forecast information"""
        print(f"\n📅 5-DAY FORECAST FOR {city.upper()}")
        print("="*55)
        
        # Group forecasts by day
        daily_forecasts = {}
        for forecast in data['list']:
            date = forecast['dt_txt'].split()[0]
            if date not in daily_forecasts:
                daily_forecasts[date] = []
            daily_forecasts[date].append(forecast)
        
        for date, forecasts in list(daily_forecasts.items())[:5]:
            temps = [f['main']['temp'] for f in forecasts]
            avg_temp = sum(temps) / len(temps)
            max_temp = max(temps)
            min_temp = min(temps)
            
            # Get weather description for the day
            descriptions = [f['weather'][0]['description'] for f in forecasts]
            main_desc = max(set(descriptions), key=descriptions.count)
            
            # Get rain/snow probability
            has_rain = any('rain' in f.get('weather', [{}])[0].get('description', '').lower() for f in forecasts)
            
            print(f"\n📆 {date}")
            print(f"   🌡️ Avg: {avg_temp:.1f}°C | Max: {max_temp:.1f}°C | Min: {min_temp:.1f}°C")
            print(f"   ☁️ {main_desc.capitalize()}")
            print(f"   💧 Avg Humidity: {sum(f['main']['humidity'] for f in forecasts) / len(forecasts):.0f}%")
            
            if has_rain:
                print(f"   ☔ Chance of rain")
        
        print("="*55)
    
    def show_favorites(self):
        """Show favorite cities"""
        if not self.favorites:
            print("\n⭐ No favorite cities yet!")
            print("   Add cities when checking weather to save them here.")
            return
        
        print("\n⭐ YOUR FAVORITE CITIES")
        print("-"*35)
        for i, city in enumerate(self.favorites, 1):
            print(f"{i}. {city}")
        
        print("-"*35)
        choice = input("\n📌 Choose a city number to see weather (or press Enter to skip): ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(self.favorites):
            city = self.favorites[int(choice)-1]
            self.get_weather(city)
            
            forecast = input("\n🔮 See 5-day forecast? (y/n): ").lower()
            if forecast == 'y':
                self.get_forecast(city)
    
    def remove_favorite(self):
        """Remove city from favorites"""
        if not self.favorites:
            print("\n⭐ No favorite cities to remove!")
            return
        
        print("\n⭐ YOUR FAVORITE CITIES")
        print("-"*35)
        for i, city in enumerate(self.favorites, 1):
            print(f"{i}. {city}")
        
        print("-"*35)
        choice = input("\n🗑️ Enter number to remove (or press Enter to cancel): ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(self.favorites):
            removed = self.favorites.pop(int(choice)-1)
            self.save_favorites()
            print(f"✅ {removed} removed from favorites!")

def main():
    print("\n" + "="*50)
    print("🌤️  WELCOME TO THE WEATHER APP  🌤️")
    print("="*50)
    print("\n⚠️  IMPORTANT FIRST TIME SETUP:")
    print("   1. Get a FREE API key from: https://openweathermap.org/api")
    print("   2. Sign up and verify your email")
    print("   3. Copy your API key and replace 'YOUR_API_KEY_HERE' in the code")
    print("   4. Restart the application\n")
    
    input("Press Enter to continue...")
    
    app = WeatherApp()
    
    while True:
        print("\n" + "="*40)
        print("🌤️  WEATHER APP MENU")
        print("="*40)
        print("1. 🌍 Get Weather (Any City)")
        print("2. 📅 Get 5-Day Forecast")
        print("3. ⭐ Show Favorite Cities")
        print("4. 🗑️ Remove Favorite City")
        print("5. 🚪 Exit")
        print("="*40)
        
        choice = input("Choose (1-5): ")
        
        if choice == "1":
            print("\n" + "-"*40)
            city = input("🏙️ Enter city name (e.g., 'Dhaka', 'London,UK', 'New York,US'): ")
            print("-"*40)
            app.get_weather(city)
            
        elif choice == "2":
            print("\n" + "-"*40)
            city = input("🏙️ Enter city name for forecast: ")
            print("-"*40)
            app.get_forecast(city)
            
        elif choice == "3":
            app.show_favorites()
            
        elif choice == "4":
            app.remove_favorite()
            
        elif choice == "5":
            print("\n👋 Thank you for using Weather App! Goodbye!\n")
            break
            
        else:
            print("\n❌ Invalid choice! Please enter 1-5")

if __name__ == "__main__":
    main()