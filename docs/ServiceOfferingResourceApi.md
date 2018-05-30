# swagger_client.ServiceOfferingResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_offering_using_post**](ServiceOfferingResourceApi.md#create_service_offering_using_post) | **POST** /api/service-offerings | createServiceOffering
[**delete_service_offering_using_delete**](ServiceOfferingResourceApi.md#delete_service_offering_using_delete) | **DELETE** /api/service-offerings/{id} | deleteServiceOffering
[**get_all_service_offerings_using_get**](ServiceOfferingResourceApi.md#get_all_service_offerings_using_get) | **GET** /api/service-offerings | getAllServiceOfferings
[**get_service_offering_using_get**](ServiceOfferingResourceApi.md#get_service_offering_using_get) | **GET** /api/service-offerings/{id} | getServiceOffering
[**update_service_offering_using_put**](ServiceOfferingResourceApi.md#update_service_offering_using_put) | **PUT** /api/service-offerings | updateServiceOffering


# **create_service_offering_using_post**
> ServiceOffering create_service_offering_using_post(service_offering)

createServiceOffering

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
api_instance = swagger_client.ServiceOfferingResourceApi(swagger_client.ApiClient(configuration))
service_offering = swagger_client.ServiceOffering() # ServiceOffering | serviceOffering

try:
    # createServiceOffering
    api_response = api_instance.create_service_offering_using_post(service_offering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOfferingResourceApi->create_service_offering_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_offering** | [**ServiceOffering**](ServiceOffering.md)| serviceOffering | 

### Return type

[**ServiceOffering**](ServiceOffering.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_offering_using_delete**
> delete_service_offering_using_delete(id)

deleteServiceOffering

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
api_instance = swagger_client.ServiceOfferingResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteServiceOffering
    api_instance.delete_service_offering_using_delete(id)
except ApiException as e:
    print("Exception when calling ServiceOfferingResourceApi->delete_service_offering_using_delete: %s\n" % e)
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

# **get_all_service_offerings_using_get**
> list[ServiceOffering] get_all_service_offerings_using_get()

getAllServiceOfferings

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
api_instance = swagger_client.ServiceOfferingResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllServiceOfferings
    api_response = api_instance.get_all_service_offerings_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOfferingResourceApi->get_all_service_offerings_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceOffering]**](ServiceOffering.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_offering_using_get**
> ServiceOffering get_service_offering_using_get(id)

getServiceOffering

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
api_instance = swagger_client.ServiceOfferingResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getServiceOffering
    api_response = api_instance.get_service_offering_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOfferingResourceApi->get_service_offering_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ServiceOffering**](ServiceOffering.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_offering_using_put**
> ServiceOffering update_service_offering_using_put(service_offering)

updateServiceOffering

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
api_instance = swagger_client.ServiceOfferingResourceApi(swagger_client.ApiClient(configuration))
service_offering = swagger_client.ServiceOffering() # ServiceOffering | serviceOffering

try:
    # updateServiceOffering
    api_response = api_instance.update_service_offering_using_put(service_offering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOfferingResourceApi->update_service_offering_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_offering** | [**ServiceOffering**](ServiceOffering.md)| serviceOffering | 

### Return type

[**ServiceOffering**](ServiceOffering.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

