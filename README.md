# Django Quiz App 
This is a Django Quiz Web Application. Users can learn about specific topics and are able to test their knowledge through a quiz at the end of each topic. 

The project includes the following apps
quiz : This app handles all the quiz logic, such as the quiz, questions and options for each question 
user_auth : This app allows users to create accounts and login

## Getting Started
To get started with this project, follow these steps:
* Clone this repository
* Build the Docker image: docker build -t myproject .
* Run the Docker container: docker run -it --rm -p 8000:8000 myproject
* Navigate to http://localhost:8000 in your web browser

## Configuration
The following environment variables are used in this project:
* SECRET_KEY: The secret key used by Django to secure session data and other sensitive information. Please create a .env file in the root folder of the project and add a secret key to run the project. Please see the .env.example file for the format. 
