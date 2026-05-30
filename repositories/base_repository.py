from core.extensions import db


class BaseRepository:

    model = None

    def create(self, **kwargs):
        instance = self.model(**kwargs)

        db.session.add(instance)
        db.session.commit()

        return instance

    def get_by_id(self, id):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()