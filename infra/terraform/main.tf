locals {
  normalized_environment = lower(var.environment)
  base_name              = lower(replace("${var.name_prefix}-${local.normalized_environment}", "_", "-"))

  default_tags = {
    environment = local.normalized_environment
    managed_by  = "terraform"
    workload    = "enterprise-lakehouse"
    owner       = "data-platform"
  }

  effective_tags = merge(local.default_tags, var.tags)
}

resource "random_string" "suffix" {
  length  = 6
  upper   = false
  lower   = true
  numeric = true
  special = false
}

resource "azurerm_resource_group" "platform" {
  name     = "rg-${local.base_name}"
  location = var.region
  tags     = local.effective_tags
}

resource "azurerm_storage_account" "platform" {
  name                     = substr(replace("st${var.name_prefix}${local.normalized_environment}${random_string.suffix.result}", "-", ""), 0, 24)
  resource_group_name      = azurerm_resource_group.platform.name
  location                 = azurerm_resource_group.platform.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
  is_hns_enabled           = true
  tags                     = local.effective_tags
}

resource "azurerm_databricks_workspace" "platform" {
  name                        = "dbw-${local.base_name}"
  resource_group_name         = azurerm_resource_group.platform.name
  location                    = azurerm_resource_group.platform.location
  sku                         = var.workspace_sku
  managed_resource_group_name = "rg-${local.base_name}-managed"
  tags                        = local.effective_tags
}
