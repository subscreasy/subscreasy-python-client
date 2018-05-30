# swagger_client.SubscriberResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscriber_using_post**](SubscriberResourceApi.md#create_subscriber_using_post) | **POST** /api/subscribers | createSubscriber
[**delete_subscriber_using_delete**](SubscriberResourceApi.md#delete_subscriber_using_delete) | **DELETE** /api/subscribers/{id} | deleteSubscriber
[**get_all_subscribers_using_get**](SubscriberResourceApi.md#get_all_subscribers_using_get) | **GET** /api/subscribers | getAllSubscribers
[**get_subscriber_by_email_using_get**](SubscriberResourceApi.md#get_subscriber_by_email_using_get) | **GET** /api/subscribers/email/{email} | getSubscriberByEmail
[**get_subscriber_by_name_using_get**](SubscriberResourceApi.md#get_subscriber_by_name_using_get) | **GET** /api/subscribers/name/{name} | getSubscriberByName
[**get_subscriber_using_get**](SubscriberResourceApi.md#get_subscriber_using_get) | **GET** /api/subscribers/{id} | getSubscriber
[**update_subscriber_using_put**](SubscriberResourceApi.md#update_subscriber_using_put) | **PUT** /api/subscribers | updateSubscriber


# **create_subscriber_using_post**
> Subscriber create_subscriber_using_post(subscriber)

createSubscriber

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
subscriber = swagger_client.Subscriber() # Subscriber | subscriber

try:
    # createSubscriber
    api_response = api_instance.create_subscriber_using_post(subscriber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->create_subscriber_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber** | [**Subscriber**](Subscriber.md)| subscriber | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriber_using_delete**
> delete_subscriber_using_delete(id)

deleteSubscriber

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteSubscriber
    api_instance.delete_subscriber_using_delete(id)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->delete_subscriber_using_delete: %s\n" % e)
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

# **get_all_subscribers_using_get**
> list[Subscriber] get_all_subscribers_using_get()

getAllSubscribers

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllSubscribers
    api_response = api_instance.get_all_subscribers_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->get_all_subscribers_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_by_email_using_get**
> list[Subscriber] get_subscriber_by_email_using_get(email)

getSubscriberByEmail

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
email = 'email_example' # str | email

try:
    # getSubscriberByEmail
    api_response = api_instance.get_subscriber_by_email_using_get(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->get_subscriber_by_email_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email | 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_by_name_using_get**
> list[Subscriber] get_subscriber_by_name_using_get(name)

getSubscriberByName

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # getSubscriberByName
    api_response = api_instance.get_subscriber_by_name_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->get_subscriber_by_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriber_using_get**
> Subscriber get_subscriber_using_get(id)

getSubscriber

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getSubscriber
    api_response = api_instance.get_subscriber_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->get_subscriber_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscriber_using_put**
> Subscriber update_subscriber_using_put(subscriber)

updateSubscriber

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
api_instance = swagger_client.SubscriberResourceApi(swagger_client.ApiClient(configuration))
subscriber = swagger_client.Subscriber() # Subscriber | subscriber

try:
    # updateSubscriber
    api_response = api_instance.update_subscriber_using_put(subscriber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriberResourceApi->update_subscriber_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber** | [**Subscriber**](Subscriber.md)| subscriber | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

