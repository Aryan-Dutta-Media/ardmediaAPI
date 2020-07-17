#Aryan Dutta Media Backend Forms API

#####An API for handling GET/POST request from the forms and dump it in the Database.

##Technologies Used
* Python
* MongoDB
* Flask

##Live Server Status
www.aryanduttamedia.herokuapp.com

##Github Steps:
* Fork the repository to your Github account
* Copy the link (ends with a .git) of your forked repository
* In a folder of your choice in your local machine, run git clone thelinkyoujustcopied.git
* ```cd ardmediaAPI```
* git remote add upstream https://github.com/Aryan-Dutta-Media/ardmediaAPI
* Whenever you want to push your change, do git add . and git commit -m "did a change" and then do git pull upstream master
* Then finally, do git push origin master.
* After pushing, go to your forked repository on Github and create a pull request.

##Steps to run the API:
* ```cd ardmediaAPI```
* ```pip install -r requirements.txt```(only for the first time after clonning) then ```python app.py```
* Add or Edit the routes and functions in the file app.py

##Testing the API:
* Locally
* With LIVE Heroku server :
* Test the API with POSTMAN

Example for GET request :
* Set the URL to ```www.aryanyanduttamedia.herokuapp.com/``` get all the entries.

Example for POST reqest :
* Set the URL to ```www.aryanduttamedia.herokuapp.com/``` to update any entry.

Example for DELETE request :
* Set the URL to ```www.aryanduutamedia.herokuapp.com``` to delete any entry.