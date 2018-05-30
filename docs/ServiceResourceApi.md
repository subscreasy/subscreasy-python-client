# swagger_client.ServiceResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_using_post**](ServiceResourceApi.md#create_service_using_post) | **POST** /api/services | createService
[**delete_service_using_delete**](ServiceResourceApi.md#delete_service_using_delete) | **DELETE** /api/services/{id} | deleteService
[**get_all_services_using_get**](ServiceResourceApi.md#get_all_services_using_get) | **GET** /api/services | getAllServices
[**get_service_using_get**](ServiceResourceApi.md#get_service_using_get) | **GET** /api/services/{id} | getService
[**update_service_using_put**](ServiceResourceApi.md#update_service_using_put) | **PUT** /api/services | updateService


# **create_service_using_post**
> Service create_service_using_post(service)

createService

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
api_instance = swagger_client.ServiceResourceApi(swagger_client.ApiClient(configuration))
service = swagger_client.Service() # Service | service

try:
    # createService
    api_response = api_instance.create_service_using_post(service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceResourceApi->create_service_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**Service**](Service.md)| service | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_using_delete**
> delete_service_using_delete(id)

deleteService

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
api_instance = swagger_client.ServiceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteService
    api_instance.delete_service_using_delete(id)
except ApiException as e:
    print("Exception when calling ServiceResourceApi->delete_service_using_delete: %s\n" % e)
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

# **get_all_services_using_get**
> list[Service] get_all_services_using_get()

getAllServices

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
api_instance = swagger_client.ServiceResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllServices
    api_response = api_instance.get_all_services_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceResourceApi->get_all_services_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Service]**](Service.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_using_get**
> Service get_service_using_get(id)

getService

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
api_instance = swagger_client.ServiceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getService
    api_response = api_instance.get_service_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceResourceApi->get_service_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_using_put**
> Service update_service_using_put(service)

updateService

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
api_instance = swagger_client.ServiceResourceApi(swagger_client.ApiClient(configuration))
service = swagger_client.Service() # Service | service

try:
    # updateService
    api_response = api_instance.update_service_using_put(service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceResourceApi->update_service_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**Service**](Service.md)| service | 

### Return type

[**Service**](Service.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

