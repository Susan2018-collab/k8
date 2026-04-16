module "ecr" {
  source = "./ecr"
}

module "s3" {
  source = "./s3"
}

module "cloudwatch" {
  source = "./cloudwatch"
}
