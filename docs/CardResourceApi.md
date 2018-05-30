# swagger_client.CardResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_card_using_post**](CardResourceApi.md#create_card_using_post) | **POST** /api/cards | createCard
[**delete_card_using_delete**](CardResourceApi.md#delete_card_using_delete) | **DELETE** /api/cards/{id} | deleteCard
[**get_all_cards_using_get**](CardResourceApi.md#get_all_cards_using_get) | **GET** /api/cards | getAllCards
[**get_card_using_get**](CardResourceApi.md#get_card_using_get) | **GET** /api/cards/{id} | getCard
[**update_card_using_put**](CardResourceApi.md#update_card_using_put) | **PUT** /api/cards | updateCard


# **create_card_using_post**
> SavedCard create_card_using_post(card)

createCard

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
api_instance = swagger_client.CardResourceApi(swagger_client.ApiClient(configuration))
card = swagger_client.SavedCard() # SavedCard | card

try:
    # createCard
    api_response = api_instance.create_card_using_post(card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardResourceApi->create_card_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card** | [**SavedCard**](SavedCard.md)| card | 

### Return type

[**SavedCard**](SavedCard.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_card_using_delete**
> delete_card_using_delete(id)

deleteCard

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
api_instance = swagger_client.CardResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteCard
    api_instance.delete_card_using_delete(id)
except ApiException as e:
    print("Exception when calling CardResourceApi->delete_card_using_delete: %s\n" % e)
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

# **get_all_cards_using_get**
> list[SavedCard] get_all_cards_using_get()

getAllCards

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
api_instance = swagger_client.CardResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllCards
    api_response = api_instance.get_all_cards_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardResourceApi->get_all_cards_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SavedCard]**](SavedCard.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_using_get**
> SavedCard get_card_using_get(id)

getCard

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
api_instance = swagger_client.CardResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getCard
    api_response = api_instance.get_card_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardResourceApi->get_card_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**SavedCard**](SavedCard.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_card_using_put**
> SavedCard update_card_using_put(card)

updateCard

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
api_instance = swagger_client.CardResourceApi(swagger_client.ApiClient(configuration))
card = swagger_client.SavedCard() # SavedCard | card

try:
    # updateCard
    api_response = api_instance.update_card_using_put(card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardResourceApi->update_card_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card** | [**SavedCard**](SavedCard.md)| card | 

### Return type

[**SavedCard**](SavedCard.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

