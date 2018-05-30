# swagger_client.InvoiceResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice_using_post**](InvoiceResourceApi.md#create_invoice_using_post) | **POST** /api/invoices | createInvoice
[**delete_invoice_using_delete**](InvoiceResourceApi.md#delete_invoice_using_delete) | **DELETE** /api/invoices/{id} | deleteInvoice
[**get_all_invoices_using_get**](InvoiceResourceApi.md#get_all_invoices_using_get) | **GET** /api/invoices | getAllInvoices
[**get_invoice_by_subscriber_using_get**](InvoiceResourceApi.md#get_invoice_by_subscriber_using_get) | **GET** /api/invoices/subscriber/{subscriberSecureId} | getInvoiceBySubscriber
[**get_invoice_using_get**](InvoiceResourceApi.md#get_invoice_using_get) | **GET** /api/invoices/{id} | getInvoice
[**update_invoice_using_put**](InvoiceResourceApi.md#update_invoice_using_put) | **PUT** /api/invoices | updateInvoice


# **create_invoice_using_post**
> Invoice create_invoice_using_post(invoice)

createInvoice

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))
invoice = swagger_client.Invoice() # Invoice | invoice

try:
    # createInvoice
    api_response = api_instance.create_invoice_using_post(invoice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->create_invoice_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)| invoice | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_using_delete**
> delete_invoice_using_delete(id)

deleteInvoice

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteInvoice
    api_instance.delete_invoice_using_delete(id)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->delete_invoice_using_delete: %s\n" % e)
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

# **get_all_invoices_using_get**
> list[Invoice] get_all_invoices_using_get()

getAllInvoices

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllInvoices
    api_response = api_instance.get_all_invoices_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->get_all_invoices_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_subscriber_using_get**
> list[Invoice] get_invoice_by_subscriber_using_get(subscriber_secure_id)

getInvoiceBySubscriber

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))
subscriber_secure_id = 'subscriber_secure_id_example' # str | subscriberSecureId

try:
    # getInvoiceBySubscriber
    api_response = api_instance.get_invoice_by_subscriber_using_get(subscriber_secure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->get_invoice_by_subscriber_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_secure_id** | **str**| subscriberSecureId | 

### Return type

[**list[Invoice]**](Invoice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_using_get**
> Invoice get_invoice_using_get(id)

getInvoice

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getInvoice
    api_response = api_instance.get_invoice_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->get_invoice_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_using_put**
> Invoice update_invoice_using_put(invoice)

updateInvoice

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
api_instance = swagger_client.InvoiceResourceApi(swagger_client.ApiClient(configuration))
invoice = swagger_client.Invoice() # Invoice | invoice

try:
    # updateInvoice
    api_response = api_instance.update_invoice_using_put(invoice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceResourceApi->update_invoice_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)| invoice | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

