# football-analysis-yolo

Computer vision project: build a football analysis system with YOLO v11

Dataset for fine tuning: https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1

Goalkeeper is detected more accurately with fine tuned model.

Tried data augmentation(crop and zoom in), still not good.

Youtube tutorial: Build an AI/ML Football Analysis system with YOLO, OpenCV, and Python

https://youtu.be/neBZ6huolkg?si=2Z91NsgW7hIpaDNW

# Solution Deployment
**Guideline:** always consider the current tech stack and cost.

Using AWS as example.

## Batch Processing Workflow

Storage:
- Store raw images/videos in Amazon S3 for scalable and cost-effective storage.

MLOps Pipeline:
  - Use SageMaker, Kubeflow, or MLflow for automated retraining, testing, and redeployment.
  - Orchestration tool: Choose based on workload complexity:
    - AWS EKS for high scalability and flexibility.
    - AWS Step Functions for lightweight AWS-native workflows.
    -AWS Batch for high-throughput, cost-sensitive workloads.

Model Deployment:
- Dockerize the model with all its dependencies and deploy it on:
  - EKS for Kubernetes-based orchestration.
  - ECS for easier integration and managed service.
  - Use GPU-backed instances for efficient model inference.

Output Storage:
- Store outputs (e.g., annotated frames, bounding boxes, or predictions) back to S3.
- Store metadata (e.g., S3 object keys, bounding box coordinates, or confidence scores) in DynamoDB.

Monitoring:
- AWS CloudWatch for metrics like request latency, GPU/CPU utilization, and error rates.
- Prometheus/Grafana for custom dashboards and detailed real-time monitoring if using Kubernetes or ECS.

## Real-Time Inference Workflow

Data Ingestion:
  - Option 1: Kafka:
    - Use Kafka if we already have an established Kafka ecosystem or require flexibility to run on-premises or across multiple clouds.
    - Use Kafka producers to ingest video frames and stream them into topics for real-time processing. Partition streams for load balancing and high-throughput data ingestion.
  - Option 2: Amazon Kinesis Video Streams (KVS):
    - If using AWS exclusively, KVS is worth trying as it natively supports real-time video ingestion, storage, and time-synchronized processing.

Model Deployment:
  - AWS ECS or EKS with GPU-backed containers.
  - AWS Lambda (if the model and video frame size are small enough and latency requirements allow serverless processing).

Output Handling:
  - Publish inference results (e.g., bounding boxes, class labels, confidence scores) to:
    - Kafka topics for downstream consumers (e.g., analytics pipelines).
    - Amazon S3 or DynamoDB for storage and easy retrieval.

Monitoring and Scaling:
  - Monitor using:
    - CloudWatch for KVS and ECS/EKS metrics.
    - Prometheus/Grafana for Kafka and Kubernetes-based workflows.
  - Implement auto-scaling policies for ECS/EKS tasks or pods based on CPU/GPU utilization and request rates.

Cost Optimization:
  - Use Amazon Elastic Inference for real-time inference to reduce GPU costs.
  - Optimize video frame rates to balance processing time and model performance.
