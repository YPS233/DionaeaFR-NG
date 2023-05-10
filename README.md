# DionaeaFR-NG

> Due to the fact that DionaeaFR has not been updated for 9 years, many dependencies were found to be outdated and the correct library versions could not be found when setting up the environment. Therefore, the project was refactored using the latest versions of related dependencies. Only the code was made compatible with the new versions, while everything else remained unchanged.

DionaeaFR is a Dionaea honeypot log analysis tool based on the Django framework. It is used to analyze Dionaea honeypot logs and provide visual reports and statistics. 
This project is a refactoring based on https://github.com/rubenespadas/DionaeaFR, using the Django4.2 framework and related dependencies to ensure that the project can work properly in the latest environment.

## Dependencies

This project requires the following dependencies to work properly:

-   Python 3.8.2
-   Django 4.2
-   geoip2
-   Node.js

## Installation

1. Clone this project to your local machine:

   ```
   git clone 
   cd DionaeaFR
   ```

2. Create and activate a Python virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install project dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Get GeoIP2 database:

   Download GeoIP and GeoLiteCity:
   ```
   wget https://mailfud.org/geoip-legacy/GeoIP.dat.gz
   wget https://mailfud.org/geoip-legacy/GeoIPCity.dat.gz
   ```

   Decompress GeoIP and GeoLiteCity:

   ```
   gunzip GeoIP.dat.gz
   gunzip GeoIPCity.dat.gz
   ```

   Move GeoIP and GeoLiteCity to DionaeaFR/DionaeaFR/static:
   ```
   mv dbip-country.mmdb DionaeaFR/DionaeaFR/static/GeoLite2-Country.mmdb
   mv dbip-city.mmdb DionaeaFR/DionaeaFR/static/GeoLite2-City.mmdb
   ```


5. Edit the configuration file.

   The default configuration file is DionaeaFR/settings.py.dict. Rename it to settings.py and modify it as needed. The path to the Dionaea database must be correctly written in the corresponding location in settings.py under DATABASES.
   ```
   mv DionaeaFR/settings.py.dict DionaeaFR/settings.py
   ```
6. Create an administrator account if needed:

   ```
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Open `http://localhost:8000` in your browser to access DionaeaFR.


## Contribution

If you want to contribute to this project, you can do so in the following ways:

-   Submit issues and suggestions on GitHub.
-   Submit code improvements and fixes.
-   Share your usage experience and feedback.

We welcome your contributions and will be happy to provide support and assistance.