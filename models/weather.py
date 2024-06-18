from lib import orm_sqlite

# Used for weatherapi
class Weather(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    temperature = orm_sqlite.FloatField()
    condition = orm_sqlite.StringField()
    cloud = orm_sqlite.IntegerField()
    created_at = orm_sqlite.IntegerField()
    source = orm_sqlite.StringField()

db = orm_sqlite.Database('db/development.sqlite')
Weather.objects.backend = db
Weather.create()
