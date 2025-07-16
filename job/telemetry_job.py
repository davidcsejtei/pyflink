from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

# Példa: forrásként egy lista
data = env.from_collection([
    ("Falcon9", 910),
    ("Starship", 1200)
])

# Egyszerű szűrés: csak ha a hőmérséklet > 1000
overheated = data.filter(lambda x: x[1] > 1000)

# Írjuk ki konzolra
overheated.print()

# Futassuk le a job-ot
env.execute("Telemetry Overheat Detector")