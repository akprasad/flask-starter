import textwrap
from fabric.api import *


def dump_to_file(filename, data):
    data = textwrap.dedent(data).lstrip()
    with open(filename, 'w') as f:
        f.write(data)


@task
def blueprint(name):
    """Create a blueprint."""
    local('mkdir starter/{0}'.format(name))
    local('touch starter/{0}/__init__.py'.format(name))

    forms_data = """
    from flask.ext.wtf import Form
    """

    models_data = """
    from starter import db
    from starter.models import Base
    """

    views_data = """
    from flask import Blueprint, render_template

    bp = Blueprint('{0}', __name__)

    @bp.route('/')
    def index():
        return render_template('{0}/index.html')
    """

    dump_to_file('starter/{0}/forms.py'.format(name), forms_data)
    dump_to_file('starter/{0}/models.py'.format(name), models_data)
    dump_to_file('starter/{0}/views.py'.format(name), views_data)


@task
def init_project(name):
    command = """mv starter {0};
        find . -name "*.py" -print0 |
        xargs -0 sed -i s/starter/{0}/g
        """.format(name)
    local(command)


@task
def server():
    local('python runserver.py')
