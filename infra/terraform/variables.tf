variable "environment" {
  description = "Deployment environment name (dev/test/prod)."
  type        = string

  validation {
    condition     = contains(["dev", "test", "prod"], var.environment)
    error_message = "environment must be one of: dev, test, prod."
  }
}

variable "region" {
  description = "Primary Azure region for platform resources."
  type        = string
  default     = "eastus"
}

variable "name_prefix" {
  description = "Client-neutral prefix used in resource naming."
  type        = string
  default     = "entlh"
}

variable "subscription_id" {
  description = "Azure subscription ID. Supplied at deployment time; never hard-code."
  type        = string
  default     = null
}

variable "tenant_id" {
  description = "Azure tenant ID. Supplied at deployment time; never hard-code."
  type        = string
  default     = null
}

variable "workspace_sku" {
  description = "Databricks workspace SKU. Premium is required for Unity Catalog features."
  type        = string
  default     = "premium"

  validation {
    condition     = contains(["standard", "premium", "trial"], var.workspace_sku)
    error_message = "workspace_sku must be one of: standard, premium, trial."
  }
}

variable "tags" {
  description = "Optional caller-provided tags merged with platform defaults."
  type        = map(string)
  default     = {}
}
