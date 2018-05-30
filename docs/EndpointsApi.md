# swagger_client.EndpointsApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_using_put**](EndpointsApi.md#authorize_using_put) | **PUT** /api/authorize | authorize
[**deduct_using_put**](EndpointsApi.md#deduct_using_put) | **PUT** /api/deduct | deduct
[**get_authorized_services_using_get**](EndpointsApi.md#get_authorized_services_using_get) | **GET** /api/service/subscriber/{secureId} | getAuthorizedServices
[**get_charging_log_by_subscription_using_get**](EndpointsApi.md#get_charging_log_by_subscription_using_get) | **GET** /api/charging-logs/subscription/{id} | getChargingLogBySubscription
[**get_customer_total_amount_using_get**](EndpointsApi.md#get_customer_total_amount_using_get) | **GET** /api/customer-totalAmountCharge/{id} | getCustomerTotalAmount
[**get_invoice_details_using_get**](EndpointsApi.md#get_invoice_details_using_get) | **GET** /api/getInvoiceDetails | getInvoiceDetails
[**get_message_template_using_get**](EndpointsApi.md#get_message_template_using_get) | **GET** /api/message-templates/email/{lifecycleEventName} | getMessageTemplate
[**get_service_instances_by_subscription_using_get**](EndpointsApi.md#get_service_instances_by_subscription_using_get) | **GET** /api/service-instances/subscription/{id} | getServiceInstancesBySubscription
[**get_service_offerings_by_subscription_plan_using_get**](EndpointsApi.md#get_service_offerings_by_subscription_plan_using_get) | **GET** /api/service-offerings/offer/{id} | getServiceOfferingsBySubscriptionPlan
[**get_total_revenue_per_month_using_get**](EndpointsApi.md#get_total_revenue_per_month_using_get) | **GET** /api/charging-logs-totalamount-customer/{id} | getTotalRevenuePerMonth


# **authorize_using_put**
> bool authorize_using_put(authorization)

authorize

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
authorization = swagger_client.Authorization() # Authorization | authorization

try:
    # authorize
    api_response = api_instance.authorize_using_put(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->authorize_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**Authorization**](Authorization.md)| authorization | 

### Return type

**bool**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deduct_using_put**
> DeductionResult deduct_using_put(deduction)

deduct

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
deduction = swagger_client.Deduction() # Deduction | deduction

try:
    # deduct
    api_response = api_instance.deduct_using_put(deduction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->deduct_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deduction** | [**Deduction**](Deduction.md)| deduction | 

### Return type

[**DeductionResult**](DeductionResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorized_services_using_get**
> AuthorizedServicesResponse get_authorized_services_using_get(secure_id)

getAuthorizedServices

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
secure_id = 'secure_id_example' # str | secureId

try:
    # getAuthorizedServices
    api_response = api_instance.get_authorized_services_using_get(secure_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_authorized_services_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secure_id** | **str**| secureId | 

### Return type

[**AuthorizedServicesResponse**](AuthorizedServicesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charging_log_by_subscription_using_get**
> list[ChargingLog] get_charging_log_by_subscription_using_get(id)

getChargingLogBySubscription

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getChargingLogBySubscription
    api_response = api_instance.get_charging_log_by_subscription_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_charging_log_by_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**list[ChargingLog]**](ChargingLog.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_total_amount_using_get**
> int get_customer_total_amount_using_get(id)

getCustomerTotalAmount

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # getCustomerTotalAmount
    api_response = api_instance.get_customer_total_amount_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_customer_total_amount_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**int**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_details_using_get**
> object get_invoice_details_using_get(invoice_request)

getInvoiceDetails

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
invoice_request = swagger_client.InvoiceRequest() # InvoiceRequest | invoiceRequest

try:
    # getInvoiceDetails
    api_response = api_instance.get_invoice_details_using_get(invoice_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_invoice_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_request** | [**InvoiceRequest**](InvoiceRequest.md)| invoiceRequest | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_template_using_get**
> MessageTemplate get_message_template_using_get(lifecycle_event_name)

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
lifecycle_event_name = 'lifecycle_event_name_example' # str | lifecycleEventName

try:
    # getMessageTemplate
    api_response = api_instance.get_message_template_using_get(lifecycle_event_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_message_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lifecycle_event_name** | **str**| lifecycleEventName | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_instances_by_subscription_using_get**
> list[ServiceInstanceResult] get_service_instances_by_subscription_using_get(id)

getServiceInstancesBySubscription

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getServiceInstancesBySubscription
    api_response = api_instance.get_service_instances_by_subscription_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_service_instances_by_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**list[ServiceInstanceResult]**](ServiceInstanceResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_offerings_by_subscription_plan_using_get**
> list[ServiceOfferingResult] get_service_offerings_by_subscription_plan_using_get(id)

getServiceOfferingsBySubscriptionPlan

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getServiceOfferingsBySubscriptionPlan
    api_response = api_instance.get_service_offerings_by_subscription_plan_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_service_offerings_by_subscription_plan_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**list[ServiceOfferingResult]**](ServiceOfferingResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_revenue_per_month_using_get**
> list[object] get_total_revenue_per_month_using_get(id)

getTotalRevenuePerMonth

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
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getTotalRevenuePerMonth
    api_response = api_instance.get_total_revenue_per_month_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_total_revenue_per_month_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

**list[object]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

