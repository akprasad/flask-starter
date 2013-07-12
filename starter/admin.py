from flask import redirect, url_for
from flask.ext.admin import (Admin, BaseView as _BaseView,
                             AdminIndexView as _AdminIndexView,
                             expose)
from flask.ext.admin.contrib.sqlamodel import ModelView as _ModelView
from flask.ext.security import current_user

from starter import app, db


# Secure views
# ------------
class AuthMixin(object):

    def is_accessible(self):
        return current_user.has_role('admin')


class AdminIndexView(_AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.has_role('admin'):
            return self.render(self._template)
        else:
            return redirect(url_for('index'))


class BaseView(AuthMixin, _BaseView):
    pass


class ModelView(AuthMixin, _ModelView):
    pass


# Admin setup
# -----------
admin = Admin(app, name='Index', index_view=AdminIndexView())

from auth.models import User, Role
class UserView(ModelView):
    column_list = ['email', 'active', 'created']


admin.add_view(UserView(User, db.session, category='Auth'))
admin.add_view(ModelView(Role, db.session, category='Auth'))
