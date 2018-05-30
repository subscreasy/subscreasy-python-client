# swagger_client.CouponResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_using_post**](CouponResourceApi.md#create_coupon_using_post) | **POST** /api/coupons | createCoupon
[**delete_coupon_using_delete**](CouponResourceApi.md#delete_coupon_using_delete) | **DELETE** /api/coupons/{id} | deleteCoupon
[**get_all_coupons_using_get**](CouponResourceApi.md#get_all_coupons_using_get) | **GET** /api/coupons | getAllCoupons
[**get_coupon_using_get**](CouponResourceApi.md#get_coupon_using_get) | **GET** /api/coupons/{id} | getCoupon
[**update_coupon_using_put**](CouponResourceApi.md#update_coupon_using_put) | **PUT** /api/coupons | updateCoupon


# **create_coupon_using_post**
> Coupon create_coupon_using_post(coupon)

createCoupon

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
api_instance = swagger_client.CouponResourceApi(swagger_client.ApiClient(configuration))
coupon = swagger_client.Coupon() # Coupon | coupon

try:
    # createCoupon
    api_response = api_instance.create_coupon_using_post(coupon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponResourceApi->create_coupon_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | [**Coupon**](Coupon.md)| coupon | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_using_delete**
> delete_coupon_using_delete(id)

deleteCoupon

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
api_instance = swagger_client.CouponResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # deleteCoupon
    api_instance.delete_coupon_using_delete(id)
except ApiException as e:
    print("Exception when calling CouponResourceApi->delete_coupon_using_delete: %s\n" % e)
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

# **get_all_coupons_using_get**
> list[Coupon] get_all_coupons_using_get()

getAllCoupons

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
api_instance = swagger_client.CouponResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAllCoupons
    api_response = api_instance.get_all_coupons_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponResourceApi->get_all_coupons_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Coupon]**](Coupon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_using_get**
> Coupon get_coupon_using_get(id)

getCoupon

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
api_instance = swagger_client.CouponResourceApi(swagger_client.ApiClient(configuration))
id = 789 # int | id

try:
    # getCoupon
    api_response = api_instance.get_coupon_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponResourceApi->get_coupon_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_using_put**
> Coupon update_coupon_using_put(coupon)

updateCoupon

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
api_instance = swagger_client.CouponResourceApi(swagger_client.ApiClient(configuration))
coupon = swagger_client.Coupon() # Coupon | coupon

try:
    # updateCoupon
    api_response = api_instance.update_coupon_using_put(coupon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CouponResourceApi->update_coupon_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | [**Coupon**](Coupon.md)| coupon | 

### Return type

[**Coupon**](Coupon.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

