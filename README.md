# flask-starter

Starter code, boilerplate, skeleton -- whatever you want to call it. Batteries included.
Best for large projects.


## Layout
This project uses the [Larger Applications](http://flask.pocoo.org/docs/patterns/packages/)
layout described in the Flask documentation. All static assets are in
`starter/static` and all templates are in `starter/templates`.

### Blueprints layout
A blueprint `bp` is at `starter/bp` and contains modules like the following:

- `forms.py` for forms
- `models.py` for various models
- `views.py` for view functions

Blueprint templates are in `starter/templates/bp` and blueprint assets are in
`starter/static/bp`.


## Extensions
I added basic support for some common extensions:

- [Flask-Admin](http://flask-admin.readthedocs.org/en/latest/) for basic admin
  functionality.
- [Flask-Assets](http://elsdoerfer.name/docs/flask-assets/) for compiling and
  managing assets. Generated assets are stored in `starter/static/gen`.
- [Flask-DebugToolbar](http://flask-debugtoolbar.readthedocs.org/) for debugging
  and profiling. If `app.config['DEBUG'] == False` the extension isn't imported
  at all.
- [Flask-Restless](http://flask-restless.readthedocs.org/)
- [Flask-Security](http://pythonhosted.org/Flask-Security/) for all-in-one
  authentication stuff
- [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/) for database
  management. The default development config creates an sqlite database, but
  that's easy to change.
- [Flask-Uploads](http://pythonhosted.org/Flask-Uploads/) for managing file
  uploads. This is listed in `requirements.txt`, but none of the starter code
  uses it.
- [Flask-WTF](http://pythonhosted.org/Flask-WTF/) for forms


## Quickstart

    git clone git@github.com:akprasad/flask-starter.git
    cd flask-starter
    pip install -r requirements.txt
    fab init_project:<name>
    fab auth.add_admin


## Sample commands
See the full list of available commands:

    fab --list

Read more about a command:

    fab -d <command>

Rename the project to `name`:

    fab init_project:name

Start the server:

    fab server

Create a blueprint `name`:

    fab blueprint:name

Launch an interactive shell with some useful locals:

    fab shell
