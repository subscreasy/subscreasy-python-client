# swagger_client.ProfileInfoResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_profiles_using_get**](ProfileInfoResourceApi.md#get_active_profiles_using_get) | **GET** /api/profile-info | getActiveProfiles


# **get_active_profiles_using_get**
> ProfileInfoVM get_active_profiles_using_get()

getActiveProfiles

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
api_instance = swagger_client.ProfileInfoResourceApi(swagger_client.ApiClient(configuration))

try:
    # getActiveProfiles
    api_response = api_instance.get_active_profiles_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileInfoResourceApi->get_active_profiles_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProfileInfoVM**](ProfileInfoVM.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

