resource "aws_cloudwatch_log_group" "logs" {
  name              = "/devops/notifier"
  retention_in_days = 7
}
