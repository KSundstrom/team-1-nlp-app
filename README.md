# team-1-nlp-app

Team 1's repo for Uni Helsinki course Building Natural Language Processing Applications 2022. The app is not functional as of now, but here is the documentation to see how it would operate if the project were to be finished in time. 

## Running the application on your local computer

* Install the dependencies described in the `environment.yml`
* Set the environment variable `FLASK_APP` to `run.py` with `export FLASK_APP="run.py"`
* Run Flask with `flask run`
* The site should appear at `localhost:5000` in your browser
* Turn off the server with `Ctrl+C`

## Notes on the program

The app is not functional in its current form when it tries to use the daily weather data from the Finnish Meteorological Institute. The visualisation script is working funnily and does not work as of now. If you want to see a functional version of the search presented to class, you may set the environment variable `FLASK_APP` to `flask_searchengine.py` with `export FLASK_APP="flask_searchengine.py"`

## Future plans
* I this were to be developed further, a proper database handling could be implemented. That proved to be a bit too big of a chunk to chew for now
* Also a visualisation of the vectors on a 2D-plane would be interesting to see. This could be achieved with dimension reduction and kmeans.
* It would be interesting to deploy this to the web with Gunicorn and Heroku.
* There are some redundancies in the environment that could be ironed out.
