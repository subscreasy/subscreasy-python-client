# swagger_client.ChargingLogResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_charging_log_using_post**](ChargingLogResourceApi.md#create_charging_log_using_post) | **POST** /api/charging-logs | createChargingLog
[**delete_charging_log_using_delete**](ChargingLogResourceApi.md#delete_charging_log_using_delete) | **DELETE** /api/charging-logs/{id} | deleteChargingLog
[**get_all_charging_logs_using_get**](ChargingLogResourceApi.md#get_all_charging_logs_using_get) | **GET** /api/charging-logs | getAllChargingLogs
[**get_charging_log_using_get**](ChargingLogResourceApi.md#get_charging_log_using_get) | **GET** /api/charging-logs/{id} | getChargingLog
[**refund_using_post**](ChargingLogResourceApi.md#refund_using_post) | **POST** /api/charging-logs/refund/{chargingLogId} | refund
[**update_charging_log_using_put**](ChargingLogResourceApi.md#update_charging_log_using_put) | **PUT** /api/charging-logs | updateChargingLog


# **create_charging_log_using_post**
> ChargingLog create_charging_log_using_post(charging_log)

createChargingLog

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
charging_log = swagger_client.ChargingLog() # ChargingLog | chargingLog

try:
    # createChargingLog
    api_response = api_instance.create_charging_log_using_post(charging_log)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->create_charging_log_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charging_log** | [**ChargingLog**](ChargingLog.md)| chargingLog | 

### Return type

[**ChargingLog**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_charging_log_using_delete**
> delete_charging_log_using_delete(id)

deleteChargingLog

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteChargingLog
    api_instance.delete_charging_log_using_delete(id)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->delete_charging_log_using_delete: %s\n" % e)
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

# **get_all_charging_logs_using_get**
> list[ChargingLog] get_all_charging_logs_using_get(page=page, size=size, sort=sort)

getAllChargingLogs

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
page = 56 # int | Page number of the requested page (optional)
size = 56 # int | Size of a page (optional)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # getAllChargingLogs
    api_response = api_instance.get_all_charging_logs_using_get(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->get_all_charging_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of the requested page | [optional] 
 **size** | **int**| Size of a page | [optional] 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**list[ChargingLog]**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charging_log_using_get**
> ChargingLog get_charging_log_using_get(id)

getChargingLog

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getChargingLog
    api_response = api_instance.get_charging_log_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->get_charging_log_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**ChargingLog**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_using_post**
> ChargingLog refund_using_post(charging_log_id)

refund

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
charging_log_id = 789 # int | chargingLogId

try:
    # refund
    api_response = api_instance.refund_using_post(charging_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->refund_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charging_log_id** | **int**| chargingLogId | 

### Return type

[**ChargingLog**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_charging_log_using_put**
> ChargingLog update_charging_log_using_put(charging_log)

updateChargingLog

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
api_instance = swagger_client.ChargingLogResourceApi(swagger_client.ApiClient(configuration))
charging_log = swagger_client.ChargingLog() # ChargingLog | chargingLog

try:
    # updateChargingLog
    api_response = api_instance.update_charging_log_using_put(charging_log)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChargingLogResourceApi->update_charging_log_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charging_log** | [**ChargingLog**](ChargingLog.md)| chargingLog | 

### Return type

[**ChargingLog**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

