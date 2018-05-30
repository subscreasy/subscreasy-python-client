# swagger_client.UsageNotificationResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usage_notification_using_post**](UsageNotificationResourceApi.md#create_usage_notification_using_post) | **POST** /api/usage-notifications | createUsageNotification
[**delete_usage_notification_using_delete**](UsageNotificationResourceApi.md#delete_usage_notification_using_delete) | **DELETE** /api/usage-notifications/{id} | deleteUsageNotification
[**get_all_usage_notifications_using_get**](UsageNotificationResourceApi.md#get_all_usage_notifications_using_get) | **GET** /api/usage-notifications | getAllUsageNotifications
[**get_usage_notification_using_get**](UsageNotificationResourceApi.md#get_usage_notification_using_get) | **GET** /api/usage-notifications/{id} | getUsageNotification
[**update_usage_notification_using_put**](UsageNotificationResourceApi.md#update_usage_notification_using_put) | **PUT** /api/usage-notifications | updateUsageNotification


# **create_usage_notification_using_post**
> UsageNotification create_usage_notification_using_post(usage_notification)

createUsageNotification

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
api_instance = swagger_client.UsageNotificationResourceApi(swagger_client.ApiClient(configuration))
usage_notification = swagger_client.UsageNotification() # UsageNotification | usageNotification

try:
    # createUsageNotification
    api_response = api_instance.create_usage_notification_using_post(usage_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageNotificationResourceApi->create_usage_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_notification** | [**UsageNotification**](UsageNotification.md)| usageNotification | 

### Return type

[**UsageNotification**](UsageNotification.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_usage_notification_using_delete**
> delete_usage_notification_using_delete(id)

deleteUsageNotification

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
api_instance = swagger_client.UsageNotificationResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteUsageNotification
    api_instance.delete_usage_notification_using_delete(id)
except ApiException as e:
    print("Exception when calling UsageNotificationResourceApi->delete_usage_notification_using_delete: %s\n" % e)
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

# **get_all_usage_notifications_using_get**
> list[UsageNotification] get_all_usage_notifications_using_get()

getAllUsageNotifications

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
api_instance = swagger_client.UsageNotificationResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllUsageNotifications
    api_response = api_instance.get_all_usage_notifications_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageNotificationResourceApi->get_all_usage_notifications_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UsageNotification]**](UsageNotification.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_notification_using_get**
> UsageNotification get_usage_notification_using_get(id)

getUsageNotification

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
api_instance = swagger_client.UsageNotificationResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getUsageNotification
    api_response = api_instance.get_usage_notification_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageNotificationResourceApi->get_usage_notification_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**UsageNotification**](UsageNotification.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_notification_using_put**
> UsageNotification update_usage_notification_using_put(usage_notification)

updateUsageNotification

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
api_instance = swagger_client.UsageNotificationResourceApi(swagger_client.ApiClient(configuration))
usage_notification = swagger_client.UsageNotification() # UsageNotification | usageNotification

try:
    # updateUsageNotification
    api_response = api_instance.update_usage_notification_using_put(usage_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageNotificationResourceApi->update_usage_notification_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_notification** | [**UsageNotification**](UsageNotification.md)| usageNotification | 

### Return type

[**UsageNotification**](UsageNotification.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

