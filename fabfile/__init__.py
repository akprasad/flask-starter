from fabric.api import *


@task
def server():
    local('python runserver.py')
