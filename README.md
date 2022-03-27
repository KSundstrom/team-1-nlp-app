# team-1-nlp-app

Team 1's repo for Uni Helsinki course Building Natural Language Processing Applications 2022. The webapp can be found at team-1-nlp-app.herokuapp.com. The documentation here concerns mostly those who wish to install the program locally and/or tinker with it.

## Running the application on your local computer

* Install the dependencies described in the `environment.yml` or `requirements.txt` to your virtual environment of choice. The former is used with Anaconda/Miniconda implementations and the latter is used with traditional Python installations with `pip
* When in the root of the repo, run the app with `gunicorn wsgi:app
* The site should appear at `localhost:8000` in your browser
* Turn off the server with `Ctrl+C`
* If these steps fail, one could try to run `flask run`, after which the app should appear at `localhost:5000`
* If the program still does not run, try running `python wsgi.py`

## Notes on the program

The web implementation of the app fetches the maritime weather report at 9 am UTC and 9 pm UTC from the Finnish Meteorological institute website. It the appends the new information after the old and when the web app is loaded, indexes the file. 

The version of the program available here on GitHub has one set of weather data. The data collection script does need to be run separately from the main program since it was designed to be able to operate independently from the rest of the program.

## Future plans
* I this were to be developed further, a proper database handling could be implemented. That proved to be a bit too big of a chunk to chew for now
* Also a visualisation of the vectors on a 2D-plane would be interesting to see. This could be achieved with dimension reduction and kmeans.
* There are some redundancies in the environment that could be ironed out
* The stability of the app in different setups seems to be still a bit hit or miss depending on the OS and other variables. We have tried to mitigate this by creating the environment dependency files, but there seems to be still room for improvements
