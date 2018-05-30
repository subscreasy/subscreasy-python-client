# swagger_client.SubsriptionResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription_using_put**](SubsriptionResourceApi.md#cancel_subscription_using_put) | **PUT** /api/subscriptions/cancel | cancelSubscription
[**get_active_subscriptions_using_get**](SubsriptionResourceApi.md#get_active_subscriptions_using_get) | **GET** /api/subsriptions/subscriber/{secureId} | getActiveSubscriptions
[**get_all_company_subscriptions_using_get**](SubsriptionResourceApi.md#get_all_company_subscriptions_using_get) | **GET** /api/subscriptions/company/{id} | getAllCompanySubscriptions
[**get_subsription_using_get**](SubsriptionResourceApi.md#get_subsription_using_get) | **GET** /api/subsriptions/{id} | getSubsription
[**start_subscription_using_post**](SubsriptionResourceApi.md#start_subscription_using_post) | **POST** /api/subscriptions/start | startSubscription


# **cancel_subscription_using_put**
> Subsription cancel_subscription_using_put(cancellation)

cancelSubscription

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
api_instance = swagger_client.SubsriptionResourceApi(swagger_client.ApiClient(configuration))
cancellation = swagger_client.Cancellation() # Cancellation | cancellation

try:
    # cancelSubscription
    api_response = api_instance.cancel_subscription_using_put(cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsriptionResourceApi->cancel_subscription_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancellation** | [**Cancellation**](Cancellation.md)| cancellation | 

### Return type

[**Subsription**](Subsription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_subscriptions_using_get**
> list[Subsription] get_active_subscriptions_using_get(secure_id)

getActiveSubscriptions

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
api_instance = swagger_client.SubsriptionResourceApi(swagger_client.ApiClient(configuration))
secure_id = 'secure_id_example' # str | secureId

try:
    # getActiveSubscriptions
    api_response = api_instance.get_active_subscriptions_using_get(secure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsriptionResourceApi->get_active_subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secure_id** | **str**| secureId | 

### Return type

[**list[Subsription]**](Subsription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_company_subscriptions_using_get**
> list[Subsription] get_all_company_subscriptions_using_get(id)

getAllCompanySubscriptions

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
api_instance = swagger_client.SubsriptionResourceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # getAllCompanySubscriptions
    api_response = api_instance.get_all_company_subscriptions_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsriptionResourceApi->get_all_company_subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**list[Subsription]**](Subsription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subsription_using_get**
> Subsription get_subsription_using_get(id)

getSubsription

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
api_instance = swagger_client.SubsriptionResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getSubsription
    api_response = api_instance.get_subsription_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsriptionResourceApi->get_subsription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Subsription**](Subsription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_subscription_using_post**
> SubscriptionCreateResult start_subscription_using_post(request)

startSubscription

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
api_instance = swagger_client.SubsriptionResourceApi(swagger_client.ApiClient(configuration))
request = swagger_client.StartSubscriptionRequest() # StartSubscriptionRequest | request

try:
    # startSubscription
    api_response = api_instance.start_subscription_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsriptionResourceApi->start_subscription_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**StartSubscriptionRequest**](StartSubscriptionRequest.md)| request | 

### Return type

[**SubscriptionCreateResult**](SubscriptionCreateResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

