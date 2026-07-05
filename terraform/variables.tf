variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "function_name" {
  description = "Name of the Lambda function"
  default     = "serverless-todo-function"
}

variable "api_name" {
  description = "Name of the API Gateway"
  default     = "serverless-todo-api"
}
