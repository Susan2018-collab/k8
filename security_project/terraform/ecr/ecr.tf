resource "aws_ecr_repository" "repo" {
  name = "notifier-app"
}

output "repo_url" {
  value = aws_ecr_repository.repo.repository_url
}
