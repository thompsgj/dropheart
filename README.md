# Dropheart

## MVP Features

- Anonymous Pickup

- Geocache Dropoff

## Additional Features

- Profile Page

- Reporting

- Collaborating with NGOs and Charities

- Multiple languages

A web application that combines the fun and interactive elements of Geocaching with the functionality of a CRUD app for donations. 
The app will allow users to hide and find "donation caches" in various locations, 
where people can pick up approved items like socks, masks, period products, etc.
, anonymously. The app will feature a map interface for users to locate and donate items. 
Additionally, it will include data visualization to show the demand and supply of donated items in different areas, 
helping identify where needs are greatest. 
Hoping to leverage different languages and i18n to aid foreign communities and a11y to assist those less capable. 

- Potential Impact
- Creativity
- Design
- Technical Prowess

## Set up
The following steps cover how to set up the backend of the Dropheart application.  The application's frontend [lives in a separate repository](https://github.com/thompsgj/dropheart-frontend/tree/master), which has separate instructions for setting that up.

Create a virtual environment.
```
python3 -m virtualenv .venv
```

Activate your virtual environment.
```
# Linux
source .venv/bin/activate

# Windows
source .venv/scripts/activate
```

Install dependencies.
```
pip install -r requirements.txt
```

Create an .env file based on the .env-copy and add your secrets.
```
cp .env-copy .env
```

Run the application.
```
python backend/manage.py runserver
```