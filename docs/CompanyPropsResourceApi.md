# swagger_client.CompanyPropsResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company_props_using_post**](CompanyPropsResourceApi.md#create_company_props_using_post) | **POST** /api/company-props | createCompanyProps
[**delete_company_props_using_delete**](CompanyPropsResourceApi.md#delete_company_props_using_delete) | **DELETE** /api/company-props/{id} | deleteCompanyProps
[**get_all_company_props_using_get**](CompanyPropsResourceApi.md#get_all_company_props_using_get) | **GET** /api/company-props | getAllCompanyProps
[**get_company_props_by_company_id_using_get**](CompanyPropsResourceApi.md#get_company_props_by_company_id_using_get) | **GET** /api/company-props/company/{companyId} | getCompanyPropsByCompanyId
[**update_company_props_using_put**](CompanyPropsResourceApi.md#update_company_props_using_put) | **PUT** /api/company-props | updateCompanyProps


# **create_company_props_using_post**
> CompanyProps create_company_props_using_post(company_props)

createCompanyProps

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
api_instance = swagger_client.CompanyPropsResourceApi(swagger_client.ApiClient(configuration))
company_props = swagger_client.CompanyProps() # CompanyProps | companyProps

try:
    # createCompanyProps
    api_response = api_instance.create_company_props_using_post(company_props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyPropsResourceApi->create_company_props_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_props** | [**CompanyProps**](CompanyProps.md)| companyProps | 

### Return type

[**CompanyProps**](CompanyProps.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_props_using_delete**
> delete_company_props_using_delete(id)

deleteCompanyProps

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
api_instance = swagger_client.CompanyPropsResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteCompanyProps
    api_instance.delete_company_props_using_delete(id)
except ApiException as e:
    print("Exception when calling CompanyPropsResourceApi->delete_company_props_using_delete: %s\n" % e)
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

# **get_all_company_props_using_get**
> list[CompanyProps] get_all_company_props_using_get()

getAllCompanyProps

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
api_instance = swagger_client.CompanyPropsResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllCompanyProps
    api_response = api_instance.get_all_company_props_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyPropsResourceApi->get_all_company_props_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompanyProps]**](CompanyProps.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_props_by_company_id_using_get**
> CompanyProps get_company_props_by_company_id_using_get(company_id)

getCompanyPropsByCompanyId

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
api_instance = swagger_client.CompanyPropsResourceApi(swagger_client.ApiClient(configuration))
company_id = 789 # int | companyId

try:
    # getCompanyPropsByCompanyId
    api_response = api_instance.get_company_props_by_company_id_using_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyPropsResourceApi->get_company_props_by_company_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| companyId | 

### Return type

[**CompanyProps**](CompanyProps.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_props_using_put**
> CompanyProps update_company_props_using_put(company_props)

updateCompanyProps

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
api_instance = swagger_client.CompanyPropsResourceApi(swagger_client.ApiClient(configuration))
company_props = swagger_client.CompanyProps() # CompanyProps | companyProps

try:
    # updateCompanyProps
    api_response = api_instance.update_company_props_using_put(company_props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyPropsResourceApi->update_company_props_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_props** | [**CompanyProps**](CompanyProps.md)| companyProps | 

### Return type

[**CompanyProps**](CompanyProps.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

