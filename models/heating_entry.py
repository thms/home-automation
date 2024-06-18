from lib import orm_sqlite

# Used for neohub data
class HeatingEntry(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    device_id = orm_sqlite.IntegerField()
    device_type = orm_sqlite.StringField()
    heat_on = orm_sqlite.IntegerField()
    low_battery = orm_sqlite.IntegerField()
    name = orm_sqlite.StringField()
    offline = orm_sqlite.IntegerField()
    target_temperature = orm_sqlite.FloatField()
    temperature = orm_sqlite.FloatField()
    created_at = orm_sqlite.IntegerField()

db = orm_sqlite.Database('db/development.sqlite')
HeatingEntry.objects.backend = db
HeatingEntry.create()
