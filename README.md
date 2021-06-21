# Mood & Weather API

A weather api that uses a database to collect a users mood along with the weather of that specific date. The temperatrure, mood, weather description and date stamp will be collected. 

# Instructions to install
In your terminal copy and paste this command to clone this repo:
```Terminal Command
git clone https://github.com/JohnSV18/backend_weather_app
```
You will then navigate to the folder and run the command below to create your virtual environment
```Terminal Command
python3 -m venv venv
```
Then you activate your virtual environment by running the command below:
```Terminal Command
source venv/bin/activate
```
Then install what's required by running this command:
```Terminal Command
pip3 install -r requirements.txt
```
You then want to provide a module and environment variable by running the commands below:
```Terminal Command
export FLASK_APP=run.py
export FLASK_ENV=development 
```
Finally, run this command:
```Terminal Command
flask run 
```