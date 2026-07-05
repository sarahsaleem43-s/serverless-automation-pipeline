output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.todo_lambda.function_name
}

output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = aws_apigatewayv2_stage.lambda_stage.invoke_url
}
