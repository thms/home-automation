from lib import orm_sqlite

# Readinds from the inverter are intergers in fractions of volts, amps and kW
# For storage in database we convert them to floats with the normal units.
class SolarEntry(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True)
    battery_charge = orm_sqlite.FloatField()
    battery_power = orm_sqlite.FloatField() # positive or negative, depending the direction of flow
    battery_voltage = orm_sqlite.FloatField()
    battery_current = orm_sqlite.FloatField()
    battery_temperature = orm_sqlite.FloatField()
    battery_cycles = orm_sqlite.IntegerField()

    pv_1_voltage = orm_sqlite.FloatField()
    pv_1_current = orm_sqlite.FloatField()
    pv_1_power = orm_sqlite.FloatField() # positive only
    pv_2_voltage = orm_sqlite.FloatField()
    pv_2_current = orm_sqlite.FloatField()
    pv_2_power = orm_sqlite.FloatField() # positive only
    pv_power = orm_sqlite.FloatField() # positive only
    grid_power = orm_sqlite.FloatField() # positive or negative, depending the direction of flow
    load_power = orm_sqlite.FloatField()

    today_generated_solar_energy = orm_sqlite.FloatField()
    today_sold_solar_energy = orm_sqlite.FloatField()
    today_bought_grid_energy = orm_sqlite.FloatField()
    today_consumed_energy = orm_sqlite.FloatField()
    created_at = orm_sqlite.IntegerField()

db = orm_sqlite.Database('db/development.sqlite')
SolarEntry.objects.backend = db
SolarEntry.create()
