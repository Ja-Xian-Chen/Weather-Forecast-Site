#!/bin/bash
while true
do
    NY="$(date '+%Y-%m-%d-%H-%M-%S-NY')"
    HNY="${NY}.html"
    XNY="${NY}.xhtml"
    wget -O $HNY 'https://forecast.weather.gov/MapClick.php?lat=40.781&lon=-73.97'
    java -jar tagsoup-1.2.1.jar --files $HNY
    python3 parser.py $XNY

    CA="$(date '+%Y-%m-%d-%H-%M-%S-CA')"
    HCA="${CA}.html"
    XCA="${CA}.xhtml"
    wget -O $HCA 'https://forecast.weather.gov/MapClick.php?lat=34.021&lon=-118.45'
    java -jar tagsoup-1.2.1.jar --files $HCA
    python3 parser.py $XCA
    
    IL="$(date '+%Y-%m-%d-%H-%M-%S-IL')"
    HIL="${IL}.html"
    XIL="${IL}.xhtml"
    wget -O $HIL 'https://forecast.weather.gov/MapClick.php?lat=41.781&lon=-87.76'
    java -jar tagsoup-1.2.1.jar --files $HIL
    python3 parser.py $XIL
   
    TX="$(date '+%Y-%m-%d-%H-%M-%S-TX')"
    HTX="${TX}.html"
    XTX="${TX}.xhtml"
    wget -O $HTX 'https://forecast.weather.gov/MapClick.php?lat=29.641&lon=-95.28'
    java -jar tagsoup-1.2.1.jar --files $HTX
    python3 parser.py $XTX
   
    AZ="$(date '+%Y-%m-%d-%H-%M-%S-AZ')"
    HAZ="${AZ}.html"
    XAZ="${AZ}.xhtml"
    wget -O $HAZ 'https://forecast.weather.gov/MapClick.php?lat=33.691&lon=-112.07'
    java -jar tagsoup-1.2.1.jar --files $HAZ
    python3 parser.py $XAZ
   
    PA="$(date '+%Y-%m-%d-%H-%M-%S-PA')"
    HPA="${PA}.html"
    XPA="${PA}.xhtml"
    wget -O $HPA 'https://forecast.weather.gov/MapClick.php?lat=40.081&lon=-75.01'
    java -jar tagsoup-1.2.1.jar --files $HPA
    python3 parser.py $XPA
   
    FL="$(date '+%Y-%m-%d-%H-%M-%S-FL')"
    HFL="${FL}.html"
    XFL="${FL}.xhtml"
    wget -O $HFL 'https://forecast.weather.gov/MapClick.php?lat=30.231&lon=-81.67'
    java -jar tagsoup-1.2.1.jar --files $HFL
    python3 parser.py $XFL
    
    sleep 21600
done 