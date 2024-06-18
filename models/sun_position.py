from lib import orm_sqlite

class SunPosition(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    altitude = orm_sqlite.FloatField() 
    azimuth = orm_sqlite.FloatField()
    sunrise = orm_sqlite.StringField() # "06:13"
    sunset = orm_sqlite.StringField() # "19:54"
    created_at = orm_sqlite.IntegerField()

db = orm_sqlite.Database('db/development.sqlite')
SunPosition.objects.backend = db
SunPosition.create()
