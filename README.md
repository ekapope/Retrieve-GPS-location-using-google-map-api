# Using Google Map Geocoding API to retrieve GPS location from an input list (Python)

The purpose of this project is to get Latitude and Longitude for every operating metro and skytrain stations in Bangkok, Thailand. Input keyword list is in 'Trains_LatLong_Input.xlsx', under the 'StationName' column. 

# Steps:

1. Install required package.
    Since we are using Anaconda for this project, install the package by:

    conda install -c conda-forge googlemaps

    Visit this page for more details. https://anaconda.org/conda-forge/googlemaps

2. Enable Google Map Geocoding API, follow the instruction in this page. https://github.com/googlemaps/google-maps-services-python

    The free daily qouta is enough for this small personal project like this (as of 21-Jul-2018), the official pricing and premium qouta is mentioned in this page. https://developers.google.com/maps/documentation/geocoding/usage-and-billing?hl=en_US

3. Run 'Get GPS Coordinates from google map API' to extract the lat/long coordinates from the requests. Then, we can save the output for further step.

