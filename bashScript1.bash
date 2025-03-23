aws securityhub enable-security-hub
aws securityhub enable-standards \
  --standards-arn "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0"


aws guardduty create-detector --enable
