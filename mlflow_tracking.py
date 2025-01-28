import mlflow
import dagshub

# Initialize the DagsHub connection
dagshub.init(
    repo_owner='rushikesh092002',
    repo_name='End_to_End_machine_learning_with_MLFlow',
    mlflow=True
)

# Optionally set the tracking URI explicitly (DagsHub will do this internally too)
mlflow.set_tracking_uri("https://dagshub.com/rushikesh092002/End_to_End_machine_learning_with_MLFlow.mlflow")

# Start an MLflow run
with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)
