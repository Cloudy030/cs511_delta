# Global Carbon Emission from Countries during 1996-2021
This the group project of Team Delta to show global and national fossil carbon dioxide (CO2) emission from year 1996 to year 2021.
This project is developed with Django and deployed in Render. 
Visit this link https://delta-emission.onrender.com to access the website.

Data shown in the website is extracted from https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022?select=GCB2022v27_sources_flat.csv 
produced by The Devastator by quantifying sources and emission levels. 
Such data is retrieved from the Global Carbon Project's fossil CO2 emissions dataset: 2022 release by Robbie Andrew and Glen P. Peters, CICERO Center for International Climate Research.

## Main features of the website
There are ? templates in this web application.
- Home Page
  - Search function based on
    - Country
    - Type
    - Sector
- Annual CO2 emissions Page
  - Chart
  - Map
  - Table
    - Showing data points of annual CO2 emissions from all countries 
- Per Capita CO2 emissions Page
  - Chart
  - Map
  - Table
    - Showing data points of per capita CO2 emissions from all countries 

## Basic setup of the virtual environment
A virtual environment with Python version 3.10.7 is created. 
Run the following code in the terminal inside the project folder to setup the required virtual environment.
~~~
pyenv install 3.10.7
pyenv local 3.10.7
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
~~~
For later times for open the previously created virtual environment, run the following code in the project folder.
~~~
source .venv/bin/activate
~~~

## Reset database
For database regeneration, use the following command after deleting the file db.sqlite3
~~~
python3 manage.py migrate
~~~

To generate migration folder and files, use the following command:
~~~
python3 manage.py makemigrations emission
~~~

To run the generated migration, use the following command:
~~~
python3 manage.py migrate emission
~~~

To parse the data from csv files in data folder into the database, run the following command:
~~~
python3 manage.py parse_csv
~~~

## Start the server
For starting the server in local machine, run the following command in terminal:
~~~
python3 manage.py runserver
~~~

For starting the server in Codio, run the following command in Codio terminal:
~~~
python3 manage.py runserver 0.0.0.0:8000
~~~

## Maintenance
Latest code is pulled from GitHub for Render deployment.
At most two websites can be opened at once from the Render deployed link.
The number of rows of data in the three data csv files can be increased and include data from more number of years.
However, the server ability on Render should also be considered when doing such decision.

## Testing
Django tests for model setup and data input are used.
Random data objects are created to be passed into the model in testing database for testing.

For running tests, run the following command in the terminal:
~~~
python3 manage.py test
~~~

## Documents
Git-log: git.log.txt

Submission report: ?

## License
MIT License

Copyright (c) 2023 Cloudy030

## Documentation
Documentation is placed in the code's comments.

## Background
This is an assessment of course Enterprise Software Development (CS551Q) for Master of Information Technology (MScIT) from University of Aberdeen (UoA).
It is required to develop a database-driven web application using Django and deploy the developed website with Render.

This is a production of Team Delta in March 2023.

### Team Delta
- Amaldev Edamana Sudhakaran (ESAmadev)
- Chinedu Ezeokoye (dunchee)
- Ogugua Ezedozie (Ogugua Ezedozie)
- Pok Nga Ho (Cloudy0303)
- Tasnim Fateha (Tasnim Fetcha)
- Zishuo Liu (dingzhen00)