class TrackerRouter:
    """
    Controls which migrations run on which database.
    Does NOT touch reads/writes — .using('tracker') in views still works exactly as before.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'tracker':
            return 'tracker'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'tracker':
            return 'tracker'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'tracker' or obj2._meta.app_label == 'tracker':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'tracker':
            return db == 'tracker'
        else:
            return db == 'default'
