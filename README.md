# Dotamagus

> Web-based Dota 2 hero recommendation system and match prediction. The system provides hero suggestions from the combination of heroes that often win when they are picked together. The recommendation system is built based on Association Rules which mined from a dataset of 621,064 Dota 2 matches using the FP-Growth algorithm. I developed 3 machine learning models Multilayer Perceptron, Logistic Regressing, and XGBoost with a similar accuracy of 63%. For deployment, Logistic Regressing is used which has the lowest storage need for dependencies installation. The results of the recommendation system performance obtained a success rate of 81% from 1000 simulations. The source code for data, association rules mining, and model training can be found [here](https://github.com/erwintobing15/rules-model).

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
* Recommend heroes based on at least one hero picked
* Predict the win rate of a team of heroes picked using a recommendation system against the other team
* Give an alert message for a recommendation or match prediction error

## System Design
![system](../assets/system.png)

## Paper
Read more detail of this project on this [paper](../assets/paper.pdf).
