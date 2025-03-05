from diagrams import Diagram
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Spark

def create_diagram(filename):
    with Diagram("Cloud Architecture", show=False, filename='cloud_architecture_1741158922'):
        # Define architecture components
        ingress = Nginx("ingress")
        
        grpc1 = Server("grpc1")
        grpc2 = Server("grpc2")
        grpc3 = Server("grpc3")
        
        session_primary = Redis("session-primary")
        session_replica = Redis("session-replica")
        
        users_primary = PostgreSQL("users-primary")
        users_replica = PostgreSQL("users-replica")
        
        metric = Prometheus("metric")
        monitoring = Grafana("monitoring")
        
        logging = Fluentd("logging")
        stream = Kafka("stream")
        analytics = Spark("analytics")
        
        # Define connections
        ingress >> [grpc1, grpc2, grpc3]
        
        grpc1 >> session_primary
        grpc2 >> session_primary
        grpc3 >> session_primary
        
        session_primary - session_replica
        
        grpc1 >> users_primary
        grpc2 >> users_primary
        grpc3 >> users_primary
        
        users_primary - users_replica
        
        metric >> monitoring
        
        logging >> stream >> analytics

create_diagram("cloud_architecture")