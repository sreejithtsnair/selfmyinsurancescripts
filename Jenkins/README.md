# Jenkins + terraform

## Install the following plugins:
- [Azure Credentials](https://plugins.jenkins.io/azure-credentials/)

## Get the sucription id
- subId=$(az account show --output tsv --query id)
- echo $subId

## Create a principal
-  az ad sp create-for-rbac --name terraform-jenkins --role Contributor --scopes /subscriptions/${subId}
    - Create an azure credential with the returned data, named: "azure-credentials"

## Create storage account and a storage container
- resourceGroup="terraform_group"
- az group create --name $resourceGroup --location eastus
- az storage account create  --name jenkinsterraformsa  --resource-group $resourceGroup --location eastus
- az storage container create --account-name jenkinsterraformsa --name jenkinsterraformac

### Get the primary key
    - az storage account keys list -g $resourceGroup -n jenkinsterraformsa --query [0].value -o tsv
        - Create a text credential named: "access-key"

## Create pipeline as in the example 
- [Jenkinsfile-terraform](./Jenkinsfile-terraform)

