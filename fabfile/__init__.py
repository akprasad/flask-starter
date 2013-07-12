import textwrap
from fabric.api import *


def dump_to_file(data, filename):
    """Dump some data to a file. This is a helper function.

    :param data: the data to dump
    :param filename: name of the file to dump to
    """
    data = textwrap.dedent(data).lstrip()
    with open(filename, 'w') as f:
        f.write(data)


@task
def blueprint(name):
    """Create a blueprint and some common modules:

    - ``forms.py`` for forms
    - ``models.py`` for models
    - ``views.py`` for views

    In addition, this function creates an index template at
    ``starter/templates/<name>/index.html``.

    :param name: the blueprint name
    """
    local('mkdir starter/{0}'.format(name))
    local('mkdir starter/templates/{0}'.format(name))
    local('touch starter/templates/{0}/index.html'.format(name))
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

    bp = Blueprint('{0}', __name__, url_prefix='/{0}')


    @bp.route('/')
    def index():
        return render_template('{0}/index.html')
    """.format(name)

    dump_to_file(forms_data, 'starter/{0}/forms.py'.format(name))
    dump_to_file(models_data, 'starter/{0}/models.py'.format(name))
    dump_to_file(views_data, 'starter/{0}/views.py'.format(name))


@task
def init_project(name):
    """Replace all instances of ``'starter'`` with ``name``.

    This does not rename the top-level folder (``flask-starter``).

    If ``name`` doesn't conflict with any other terms, you can run this
    command again with no ill effects. When run this way, the command
    will replace all instances of the old name with ``name``.

    :param name: the new project name
    """
    command = """mv starter {0};
        find . -name "*.py" -print0 |
        xargs -0 sed -i s/starter/{0}/g
        """.format(name)
    local(command)


@task
def server():
    local('python runserver.py')
