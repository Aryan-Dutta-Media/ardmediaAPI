# Aryan Dutta Media Backend Forms API

##### An API for handling GET/POST request from the forms and dump it in the Database.

## Technologies Used
* Python
* MongoDB
* Flask

## Live Server Status
www.ardmedia.herokuapp.com

## Github Steps:
* Fork the repository to your Github account
* Copy the link (ends with a .git) of your forked repository
* In a folder of your choice in your local machine, run git clone thelinkyoujustcopied.git
* ```cd ardmediaAPI```
* git remote add upstream https://github.com/Aryan-Dutta-Media/ardmediaAPI
* Whenever you want to push your change, do git add . and git commit -m "did a change" and then do git pull upstream master
* Then finally, do git push origin master.
* After pushing, go to your forked repository on Github and create a pull request.

## Steps to run the API:
* ```cd ardmediaAPI```
* Create a virtual environment ```py -3 -m venv venv```
* Activate virtual environment ```venv\Scripts\activate``` (for Windows) and ```venv\bin\activate``` (for Mac)
* ```pip install -r requirements.txt```(only for the first time after clonning) then ```python app.py```
* Add or Edit the routes and functions in the file app.py

## Testing the API:
* Locally
* With LIVE Heroku server :
* Test the API with POSTMAN

Example for GET request :
* Set the URL to ```www.ardmedia.herokuapp.com/contact?api_key=<your_key>``` get all the entries from the contact form.
* Set the URL to ```www.ardmedia.herokuapp.com/landing?api_key=<your_key>``` get all the entries from landing form.
* Set the URL to ```www.ardmedia.herokuapp.com/subscribe?api_key=<your_key>``` get all the entries from subscribe form.

Example for POST request :
* Set the URL to ```www.ardmedia.herokuapp.com/contact?api_key=<your_key>``` to update any entry from contact form.<br><br>

    Sample JSON Data to contact route:
    ```json
    {
        "firstname": "testName",
        "lastname": "testName",
        "email": "sample@gmail.com",
        "contact": 1234567890,
        "message": "Hello Everyone"
    }
    ```
    <br>
* Set the URL to ```www.ardmedia.herokuapp.com/landing?api_key=<your_key>?api_key=<your_key>``` to update any entry from landing form.<br>
    Sample JSON Data to landing route:
    ```json
    {
        "firstname": "testName",
        "email": "sample@gmail.com"
    }
    ```
    <br>
* Set the URL to ```www.ardmedia.herokuapp.com/subscribe?api_key=<your_key>``` to update any entry subscribe form.<br>
Sample JSON Data to subscribe route:
    ```json
    {
        "email": "sample@gmail.com"
    }
    ```
<br>
Example for DELETE request :

* Set the URL to ```www.ardmedia.herokuapp.com/contact?api_key=<your_key>``` to delete any entry from contact form.

* Set the URL to ```www.ardmedia.herokuapp.com/landing?api_key=<your_key>``` to delete any entry from landing form.

* Set the URL to ```www.ardmedia.herokuapp.com/subscribe?api_key=<your_key>``` to delete any entry from subscribe form.

