# swagger_client.CompanyResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company_using_post**](CompanyResourceApi.md#create_company_using_post) | **POST** /api/companies | createCompany
[**delete_company_using_delete**](CompanyResourceApi.md#delete_company_using_delete) | **DELETE** /api/companies/{id} | deleteCompany
[**get_all_companies_using_get**](CompanyResourceApi.md#get_all_companies_using_get) | **GET** /api/companies | getAllCompanies
[**get_company_using_get**](CompanyResourceApi.md#get_company_using_get) | **GET** /api/companies/{id} | getCompany
[**update_company_using_put**](CompanyResourceApi.md#update_company_using_put) | **PUT** /api/companies | updateCompany


# **create_company_using_post**
> Company create_company_using_post(company)

createCompany

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CompanyResourceApi(swagger_client.ApiClient(configuration))
company = swagger_client.Company() # Company | company

try:
    # createCompany
    api_response = api_instance.create_company_using_post(company)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyResourceApi->create_company_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Company**](Company.md)| company | 

### Return type

[**Company**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_using_delete**
> delete_company_using_delete(id)

deleteCompany

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CompanyResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteCompany
    api_instance.delete_company_using_delete(id)
except ApiException as e:
    print("Exception when calling CompanyResourceApi->delete_company_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_companies_using_get**
> list[Company] get_all_companies_using_get()

getAllCompanies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CompanyResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllCompanies
    api_response = api_instance.get_all_companies_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyResourceApi->get_all_companies_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Company]**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_using_get**
> Company get_company_using_get(id)

getCompany

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CompanyResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getCompany
    api_response = api_instance.get_company_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyResourceApi->get_company_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Company**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_using_put**
> Company update_company_using_put(company)

updateCompany

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CompanyResourceApi(swagger_client.ApiClient(configuration))
company = swagger_client.Company() # Company | company

try:
    # updateCompany
    api_response = api_instance.update_company_using_put(company)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyResourceApi->update_company_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | [**Company**](Company.md)| company | 

### Return type

[**Company**](Company.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

