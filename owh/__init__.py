# -*- coding: utf-8 -*-
# owh (c) Thomas C Hicks

from flask_diamond import Diamond
from flask_diamond.facets.administration import AdminModelView
from flask_diamond.facets.database import db
from .models import User, Role, ThinPrepResults, Impressions

# declare these globalish objects before initializing models
application = None


class owh(Diamond):

    def init_accounts(self):
        "initialize accounts with the User and Role classes imported from .models"
        return self.super("accounts", user=User, role=Role)

    def init_administration(self):
        "Initialize admin interface"

        admin = self.super("administration", user=User, role=Role)

        model_list = [ThinPrepResults, Impressions
        ]

        for model in model_list:
            admin.add_view(AdminModelView(
                model,
                db.session,
                name=model.__name__,
                category="Models")
            )

        return admin

    def init_blueprints(self):
        "Application blueprints"

        self.super("blueprints")

        # administration blueprint is custom to this application
        from .views.administration.modelviews import adminbaseview
        self.app.register_blueprint(adminbaseview)

        from .views.diamond import diamond_blueprint
        self.app.register_blueprint(diamond_blueprint)


def create_app():
    global application
    if not application:
        application = owh()
        application.facet("configuration")
        application.facet("logs")
        application.facet("database")
        application.facet("marshalling")
        application.facet("blueprints")
        application.facet("accounts")
        application.facet("signals")
        application.facet("forms")
        application.facet("error_handlers")
        application.facet("request_handlers")
        application.facet("administration")
        # application.facet("rest", api_map=api_map)
        # application.facet("webassets")
        # application.facet("email")
        # application.facet("debugger")
        # application.facet("task_queue")

    # print application.app.url_map
    return application.app
