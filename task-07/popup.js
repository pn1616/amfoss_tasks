const API_key = '09b61393f1440bc5f96ed68e8e4771d6';

document.addEventListener('DOMContentLoaded', function () {
  const locationInput = document.getElementById('location');
  const checkWeatherButton = document.getElementById('checkWeather');
  const weatherInfo = document.getElementById('weatherInfo');

  checkWeatherButton.addEventListener('click', () => {
    const location = locationInput.value;
    if (location) {
      // Construct the API request URL with the user's input location
      const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${API_key}`;

      // Make the API request
      fetch(apiUrl)
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          // Parse and display the weather data
          const temperatureKelvin = data.main.temp;
          const temperatureCelsius = (temperatureKelvin - 273).toFixed(2)
          const weatherDescription = data.weather[0].description;
          weatherInfo.textContent = `Weather in ${location}: ${weatherDescription}, ${temperatureCelsius}°C`;
        })
        .catch((error) => {
          console.error('Error:', error);
          weatherInfo.textContent = 'Error fetching weather data.';
        });
    } else {
      weatherInfo.textContent = 'Please enter a location.';
    }
  });
});
