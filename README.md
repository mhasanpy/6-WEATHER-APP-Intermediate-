# 6-WEATHER-APP-Intermediate-
#Concepts: APIs, HTTP requests, JSON parsing
# 🌤️ Weather App (Intermediate)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-OpenWeatherMap-orange.svg)](https://openweathermap.org/api)
[![Requests](https://img.shields.io/badge/Requests-2.x-green.svg)](https://docs.python-requests.org/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A **professional, feature-rich weather application** that provides real-time weather data and 5-day forecasts for any city worldwide. This is **Project 6** in my Python exercises series, demonstrating API integration, JSON data processing, and user preference management.

## 🎯 Purpose

Connect to real-world APIs to fetch live weather data, process JSON responses, and present meaningful information to users. This app bridges the gap between learning Python and building practical, internet-connected applications.

## ✨ Features

### 🌍 Current Weather
- **Real-time data** – Temperature, feels like, min/max, humidity, pressure, wind speed
- **Weather descriptions** – Clear, rainy, cloudy, snowy, etc. with emoji indicators
- **Country detection** – Automatically shows country code with city name
- **Smart advice** – Contextual recommendations based on temperature and conditions

### 📅 5-Day Forecast
- **Daily averages** – Average, maximum, and minimum temperatures
- **Weather patterns** – Dominant weather condition for each day
- **Precipitation alerts** – Rain chance indicators
- **Humidity tracking** – Average humidity per day

### ⭐ Favorites System
- **Save cities** – Build a personal list of favorite locations
- **Persistent storage** – Favorites saved to `favorites.json` file
- **Quick access** – One-click weather checks for saved cities
- **Remove cities** – Manage your favorites list easily

### 🛡️ Error Handling
- **Invalid city names** – Helpful error messages with suggestions
- **Network issues** – Graceful handling of connection problems
- **API key missing** – Clear setup instructions for first-time users

## 🧠 Advanced Concepts Covered

| Concept | Implementation | Why It Matters |
|---------|----------------|----------------|
| **API Integration** | OpenWeatherMap REST API | Connects Python to real-world data |
| **JSON Processing** | Parsing API responses | Extracts meaningful data from web |
| **HTTP Requests** | Python `requests` library | Fundamental for web-connected apps |
| **File I/O** | JSON file for favorites | Persistent user data storage |
| **Error Handling** | Try/except blocks | Robust production-ready code |
| **Data Visualization** | Formatted console output | Presents complex data clearly |
| **User Experience** | Emojis, advice, formatting | Makes CLI apps user-friendly |

## 🚀 How to Run

### Prerequisites

```bash
pip install requests
