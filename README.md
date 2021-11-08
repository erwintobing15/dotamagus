# Dotamagus

> This is a recommendation system for Dota 2 hero and match prediction webapp. It will provides hero suggestions from the combination of heroes that often win when they are picked together. The recommendation system is built based on Association Rules using the FP-Growth algorithm. The recommendation algorithm is a custom made search algorithm with time complexity O(n³) (because I just focus on how to make it work, but will need to optimize it later on). For match prediction I originaly used neural nerwork algorithm Multi Layer Percetron using tensorflow. But because installing tensorflow need 500MB or more storage space, I used logistic regression instead for the sake of deployment. The model and the web app is built with python and django. You can find the association rules and model source code [here](https://github.com/erwintobing15/rules-model).

## Demo
Try live demo [here](https://dotamagos.pythonanywhere.com/).

## Screenshoot
![home](../assets/home.PNG)

## Technologies 
* Python
* Django
* HTML
* CSS
* JS
* Bootstrap

## Features
* Recommend heroes after picking atleast one hero
* Prediction win percentage of radiant team (heroes picked with recommendation)
