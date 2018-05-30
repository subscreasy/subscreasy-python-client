# swagger_client.ServiceInstanceResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_instance_using_post**](ServiceInstanceResourceApi.md#create_service_instance_using_post) | **POST** /api/service-instances | createServiceInstance
[**delete_service_instance_using_delete**](ServiceInstanceResourceApi.md#delete_service_instance_using_delete) | **DELETE** /api/service-instances/{id} | deleteServiceInstance
[**get_all_service_instances_using_get**](ServiceInstanceResourceApi.md#get_all_service_instances_using_get) | **GET** /api/service-instances | getAllServiceInstances
[**get_service_instance_using_get**](ServiceInstanceResourceApi.md#get_service_instance_using_get) | **GET** /api/service-instances/{id} | getServiceInstance
[**update_service_instance_using_put**](ServiceInstanceResourceApi.md#update_service_instance_using_put) | **PUT** /api/service-instances | updateServiceInstance


# **create_service_instance_using_post**
> ServiceInstance create_service_instance_using_post(service_instance)

createServiceInstance

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
api_instance = swagger_client.ServiceInstanceResourceApi(swagger_client.ApiClient(configuration))
service_instance = swagger_client.ServiceInstance() # ServiceInstance | serviceInstance

try:
    # createServiceInstance
    api_response = api_instance.create_service_instance_using_post(service_instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstanceResourceApi->create_service_instance_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_instance** | [**ServiceInstance**](ServiceInstance.md)| serviceInstance | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_instance_using_delete**
> delete_service_instance_using_delete(id)

deleteServiceInstance

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
api_instance = swagger_client.ServiceInstanceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteServiceInstance
    api_instance.delete_service_instance_using_delete(id)
except ApiException as e:
    print("Exception when calling ServiceInstanceResourceApi->delete_service_instance_using_delete: %s\n" % e)
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

# **get_all_service_instances_using_get**
> list[ServiceInstance] get_all_service_instances_using_get()

getAllServiceInstances

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
api_instance = swagger_client.ServiceInstanceResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllServiceInstances
    api_response = api_instance.get_all_service_instances_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstanceResourceApi->get_all_service_instances_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceInstance]**](ServiceInstance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instance_using_get**
> ServiceInstance get_service_instance_using_get(id)

getServiceInstance

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
api_instance = swagger_client.ServiceInstanceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getServiceInstance
    api_response = api_instance.get_service_instance_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstanceResourceApi->get_service_instance_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_instance_using_put**
> ServiceInstance update_service_instance_using_put(service_instance)

updateServiceInstance

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
api_instance = swagger_client.ServiceInstanceResourceApi(swagger_client.ApiClient(configuration))
service_instance = swagger_client.ServiceInstance() # ServiceInstance | serviceInstance

try:
    # updateServiceInstance
    api_response = api_instance.update_service_instance_using_put(service_instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceInstanceResourceApi->update_service_instance_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_instance** | [**ServiceInstance**](ServiceInstance.md)| serviceInstance | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

