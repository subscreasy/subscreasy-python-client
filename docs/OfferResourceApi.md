# swagger_client.OfferResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_using_post**](OfferResourceApi.md#create_offer_using_post) | **POST** /api/offers | createOffer
[**delete_offer_using_delete**](OfferResourceApi.md#delete_offer_using_delete) | **DELETE** /api/offers/{id} | deleteOffer
[**get_all_offers_using_get**](OfferResourceApi.md#get_all_offers_using_get) | **GET** /api/offers | getAllOffers
[**get_offer_using_get**](OfferResourceApi.md#get_offer_using_get) | **GET** /api/offers/{id} | getOffer
[**update_offer_using_put**](OfferResourceApi.md#update_offer_using_put) | **PUT** /api/offers | updateOffer


# **create_offer_using_post**
> Offer create_offer_using_post(offer)

createOffer

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
api_instance = swagger_client.OfferResourceApi(swagger_client.ApiClient(configuration))
offer = swagger_client.Offer() # Offer | offer

try:
    # createOffer
    api_response = api_instance.create_offer_using_post(offer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferResourceApi->create_offer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer** | [**Offer**](Offer.md)| offer | 

### Return type

[**Offer**](Offer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_offer_using_delete**
> delete_offer_using_delete(id)

deleteOffer

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
api_instance = swagger_client.OfferResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteOffer
    api_instance.delete_offer_using_delete(id)
except ApiException as e:
    print("Exception when calling OfferResourceApi->delete_offer_using_delete: %s\n" % e)
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

# **get_all_offers_using_get**
> list[Offer] get_all_offers_using_get()

getAllOffers

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
api_instance = swagger_client.OfferResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllOffers
    api_response = api_instance.get_all_offers_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferResourceApi->get_all_offers_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Offer]**](Offer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_using_get**
> Offer get_offer_using_get(id)

getOffer

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
api_instance = swagger_client.OfferResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getOffer
    api_response = api_instance.get_offer_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferResourceApi->get_offer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Offer**](Offer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_offer_using_put**
> Offer update_offer_using_put(offer)

updateOffer

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
api_instance = swagger_client.OfferResourceApi(swagger_client.ApiClient(configuration))
offer = swagger_client.Offer() # Offer | offer

try:
    # updateOffer
    api_response = api_instance.update_offer_using_put(offer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OfferResourceApi->update_offer_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer** | [**Offer**](Offer.md)| offer | 

### Return type

[**Offer**](Offer.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

