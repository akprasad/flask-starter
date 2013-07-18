# -*- coding: utf-8 -*-
"""
    Commands for production environments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    :license: MIT and BSD
"""

from fabric.api import *


@task
def deploy_core():
    pass


@task
def deploy_static():
    """Deploy only static files."""
    pass


@task
def deploy():
    deploy_core()
    deploy_static()
