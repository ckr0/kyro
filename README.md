Please note that this is a prototype application and works with economictimes.com news articles but can be adapted for most of the
free news websites( without hard or soft paywall ).

This is an example web application and AI powered news article classifier. 
The application takes a news article URL as input and predicts its category along with maintaining a history of inputs and outputs.
It is written in python as detailed below:

Scraper: takes a url, converts the html page into pure text consisting only of the news text using beautifulsoup python module.

News Classification: This is a machine learning algorithm ( Logistics regression ) which uses scikit-learn module
to implement the model. It also serialises the models using pickle module so as to bring efficiency in the prediction process.

Database: A sqlite3 database is used to store the input urls and ouput news categories using flask_sqlalchemy python module.

Web server: This website is powered by flask, a popular web server python module.

Local Deployment : The app can be deployed locally by cloning the repository ( https://github.com/ckr0/kyro ) on to your 
local machine. 

Please make sure that all the python modules mentioned in the requirements.txt file are installed. You can use the following 
command to install all the modules at once : pip install -r requirements.txt

After cloning move into the root folder of the application and start the app by typing the following:

Windows : py main.py
Linux/MacOs : python3 main.py

Now you can access the web app by opening the URL (localhost:5000) in any web browser. On the main page of the website enter the 
URL into the textbox and click 'Submit'. The predicted category will be displayed below alomg with the history of all submissions.

An example web app is located at : https://kyro.ckr0.repl.co ( Please note that this example app may not run always as replit kills
the app frequently. In case it doesn't work please deploy it for free on replit as detailed below.)

You can also deploy this app in a few clicks on replit platform. Just select Github repo ( github.com/ckr0/kyro ) when creating 
a new repl. Once the deployment is complete, you can click on the 'Run' button to start the app(It may take a couple of minutes
to load the modules).