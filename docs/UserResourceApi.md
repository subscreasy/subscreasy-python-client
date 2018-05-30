# swagger_client.UserResourceApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_using_post**](UserResourceApi.md#create_user_using_post) | **POST** /api/users | createUser
[**delete_user_using_delete**](UserResourceApi.md#delete_user_using_delete) | **DELETE** /api/users/{login} | deleteUser
[**get_all_users_using_get**](UserResourceApi.md#get_all_users_using_get) | **GET** /api/users | getAllUsers
[**get_authorities_using_get**](UserResourceApi.md#get_authorities_using_get) | **GET** /api/users/authorities | getAuthorities
[**get_user_using_get**](UserResourceApi.md#get_user_using_get) | **GET** /api/users/{login} | getUser
[**update_user_using_put**](UserResourceApi.md#update_user_using_put) | **PUT** /api/users | updateUser


# **create_user_using_post**
> ResponseEntity create_user_using_post(managed_user_vm)

createUser

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))
managed_user_vm = swagger_client.ManagedUserVM() # ManagedUserVM | managedUserVM

try:
    # createUser
    api_response = api_instance.create_user_using_post(managed_user_vm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserResourceApi->create_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_user_vm** | [**ManagedUserVM**](ManagedUserVM.md)| managedUserVM | 

### Return type

[**ResponseEntity**](ResponseEntity.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> delete_user_using_delete(login)

deleteUser

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | login

try:
    # deleteUser
    api_instance.delete_user_using_delete(login)
except ApiException as e:
    print("Exception when calling UserResourceApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| login | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_using_get**
> list[User] get_all_users_using_get(page=page, size=size, sort=sort)

getAllUsers

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))
page = 56 # int | Page number of the requested page (optional)
size = 56 # int | Size of a page (optional)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)

try:
    # getAllUsers
    api_response = api_instance.get_all_users_using_get(page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserResourceApi->get_all_users_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number of the requested page | [optional] 
 **size** | **int**| Size of a page | [optional] 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorities_using_get**
> list[str] get_authorities_using_get()

getAuthorities

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))

try:
    # getAuthorities
    api_response = api_instance.get_authorities_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserResourceApi->get_authorities_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> User get_user_using_get(login)

getUser

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | login

try:
    # getUser
    api_response = api_instance.get_user_using_get(login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserResourceApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| login | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_put**
> User update_user_using_put(managed_user_vm)

updateUser

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
api_instance = swagger_client.UserResourceApi(swagger_client.ApiClient(configuration))
managed_user_vm = swagger_client.ManagedUserVM() # ManagedUserVM | managedUserVM

try:
    # updateUser
    api_response = api_instance.update_user_using_put(managed_user_vm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserResourceApi->update_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_user_vm** | [**ManagedUserVM**](ManagedUserVM.md)| managedUserVM | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

