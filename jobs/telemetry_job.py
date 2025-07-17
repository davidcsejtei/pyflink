from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# Configure for cluster execution
env.get_config().set_auto_watermark_interval(1000)

data = env.from_collection(
    collection=[("Starship", 1200), ("Falcon9", 910)],
    type_info=Types.TUPLE([Types.STRING(), Types.INT()])
)

data.print()

env.execute("Telemetry Overheat Detector")