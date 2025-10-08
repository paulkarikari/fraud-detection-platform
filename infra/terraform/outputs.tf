output "environment" {
  description = "Resolved deployment environment."
  value       = var.environment
}

output "resource_group_name" {
  description = "Resource group that hosts shared platform resources."
  value       = azurerm_resource_group.platform.name
}

output "storage_account_name" {
  description = "Primary ADLS Gen2 storage account for lakehouse data."
  value       = azurerm_storage_account.platform.name
}

output "databricks_workspace_id" {
  description = "Databricks workspace resource identifier."
  value       = azurerm_databricks_workspace.platform.id
}

output "databricks_workspace_url" {
  description = "Databricks workspace URL for CLI and bundle targeting."
  value       = azurerm_databricks_workspace.platform.workspace_url
}
