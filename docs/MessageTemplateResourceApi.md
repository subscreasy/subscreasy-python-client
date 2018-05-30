# swagger_client.MessageTemplateResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message_template_using_post**](MessageTemplateResourceApi.md#create_message_template_using_post) | **POST** /api/message-templates | createMessageTemplate
[**delete_message_template_using_delete**](MessageTemplateResourceApi.md#delete_message_template_using_delete) | **DELETE** /api/message-templates/{id} | deleteMessageTemplate
[**get_all_message_templates_using_get**](MessageTemplateResourceApi.md#get_all_message_templates_using_get) | **GET** /api/message-templates | getAllMessageTemplates
[**get_message_template_using_get1**](MessageTemplateResourceApi.md#get_message_template_using_get1) | **GET** /api/message-templates/{id} | getMessageTemplate
[**update_message_template_using_put**](MessageTemplateResourceApi.md#update_message_template_using_put) | **PUT** /api/message-templates | updateMessageTemplate


# **create_message_template_using_post**
> MessageTemplate create_message_template_using_post(message_template)

createMessageTemplate

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
api_instance = swagger_client.MessageTemplateResourceApi(swagger_client.ApiClient(configuration))
message_template = swagger_client.MessageTemplate() # MessageTemplate | messageTemplate

try:
    # createMessageTemplate
    api_response = api_instance.create_message_template_using_post(message_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplateResourceApi->create_message_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_template** | [**MessageTemplate**](MessageTemplate.md)| messageTemplate | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_template_using_delete**
> delete_message_template_using_delete(id)

deleteMessageTemplate

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
api_instance = swagger_client.MessageTemplateResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteMessageTemplate
    api_instance.delete_message_template_using_delete(id)
except ApiException as e:
    print("Exception when calling MessageTemplateResourceApi->delete_message_template_using_delete: %s\n" % e)
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

# **get_all_message_templates_using_get**
> list[MessageTemplate] get_all_message_templates_using_get()

getAllMessageTemplates

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
api_instance = swagger_client.MessageTemplateResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllMessageTemplates
    api_response = api_instance.get_all_message_templates_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplateResourceApi->get_all_message_templates_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MessageTemplate]**](MessageTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_template_using_get1**
> MessageTemplate get_message_template_using_get1(id)

getMessageTemplate

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
api_instance = swagger_client.MessageTemplateResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getMessageTemplate
    api_response = api_instance.get_message_template_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplateResourceApi->get_message_template_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message_template_using_put**
> MessageTemplate update_message_template_using_put(message_template)

updateMessageTemplate

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
api_instance = swagger_client.MessageTemplateResourceApi(swagger_client.ApiClient(configuration))
message_template = swagger_client.MessageTemplate() # MessageTemplate | messageTemplate

try:
    # updateMessageTemplate
    api_response = api_instance.update_message_template_using_put(message_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessageTemplateResourceApi->update_message_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_template** | [**MessageTemplate**](MessageTemplate.md)| messageTemplate | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

