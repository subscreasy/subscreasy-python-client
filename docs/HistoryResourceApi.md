# swagger_client.HistoryResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_history_using_post**](HistoryResourceApi.md#create_history_using_post) | **POST** /api/histories | createHistory
[**delete_history_using_delete**](HistoryResourceApi.md#delete_history_using_delete) | **DELETE** /api/histories/{id} | deleteHistory
[**get_all_histories_using_get**](HistoryResourceApi.md#get_all_histories_using_get) | **GET** /api/histories | getAllHistories
[**get_history_using_get**](HistoryResourceApi.md#get_history_using_get) | **GET** /api/histories/{id} | getHistory
[**update_history_using_put**](HistoryResourceApi.md#update_history_using_put) | **PUT** /api/histories | updateHistory


# **create_history_using_post**
> History create_history_using_post(history)

createHistory

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
api_instance = swagger_client.HistoryResourceApi(swagger_client.ApiClient(configuration))
history = swagger_client.History() # History | history

try:
    # createHistory
    api_response = api_instance.create_history_using_post(history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryResourceApi->create_history_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history** | [**History**](History.md)| history | 

### Return type

[**History**](History.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_history_using_delete**
> delete_history_using_delete(id)

deleteHistory

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
api_instance = swagger_client.HistoryResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteHistory
    api_instance.delete_history_using_delete(id)
except ApiException as e:
    print("Exception when calling HistoryResourceApi->delete_history_using_delete: %s\n" % e)
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

# **get_all_histories_using_get**
> list[History] get_all_histories_using_get()

getAllHistories

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
api_instance = swagger_client.HistoryResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllHistories
    api_response = api_instance.get_all_histories_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryResourceApi->get_all_histories_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[History]**](History.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_using_get**
> History get_history_using_get(id)

getHistory

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
api_instance = swagger_client.HistoryResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getHistory
    api_response = api_instance.get_history_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryResourceApi->get_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**History**](History.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_history_using_put**
> History update_history_using_put(history)

updateHistory

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
api_instance = swagger_client.HistoryResourceApi(swagger_client.ApiClient(configuration))
history = swagger_client.History() # History | history

try:
    # updateHistory
    api_response = api_instance.update_history_using_put(history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryResourceApi->update_history_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history** | [**History**](History.md)| history | 

### Return type

[**History**](History.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

