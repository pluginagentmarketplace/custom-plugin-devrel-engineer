---
name: devops-cloud
description: Master cloud platforms including AWS, GCP, and Azure. Learn services, infrastructure automation, and cloud-native patterns.
---

# Cloud Platforms

## AWS
```bash
# EC2 - Compute
aws ec2 run-instances --image-id ami-xxx --instance-type t3.micro

# S3 - Storage
aws s3 cp file.txt s3://my-bucket/

# RDS - Database
aws rds create-db-instance --db-instance-identifier mydb

# Lambda - Serverless
aws lambda create-function --function-name myfunction --zip-file fileb://deployment.zip

# CloudFront - CDN
# Distribution configuration for static assets

# IAM - Access control
aws iam create-user --user-name developer
aws iam attach-user-policy --user-name developer --policy-arn arn:aws:iam::aws:policy/PowerUserAccess
```

## Terraform - Infrastructure as Code
```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  tags = {
    Name = "web-server"
  }
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

## GCP Services
- **Compute Engine**: Virtual machines
- **App Engine**: Managed platform
- **Cloud Run**: Serverless containers
- **Cloud SQL**: Managed databases
- **Cloud Storage**: Object storage
- **BigQuery**: Data warehouse

## Azure Services
- **Virtual Machines**: Compute
- **App Service**: Web apps
- **Azure Kubernetes**: Managed Kubernetes
- **Azure SQL**: Managed databases
- **Cosmos DB**: NoSQL
- **Azure DevOps**: CI/CD

## Key Concepts

✅ Regions & availability zones
✅ Virtual networks & security
✅ Storage options
✅ Database services
✅ Load balancing
✅ Auto-scaling
✅ Cost optimization
✅ Disaster recovery

## Choosing Cloud Provider
- **AWS**: Most services, mature
- **GCP**: Data/ML focus, good pricing
- **Azure**: Enterprise, Microsoft integration
