# openapi_client.ApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /applications | Create a new application
[**create_contribution_type**](ApplicationsApi.md#create_contribution_type) | **POST** /applications/{applicationId}/contributionTypes | Create a new contribution type
[**get_application_by_id**](ApplicationsApi.md#get_application_by_id) | **GET** /applications/{applicationId} | Get application by Id
[**get_applications**](ApplicationsApi.md#get_applications) | **GET** /applications | Get applications
[**get_contribution_type_by_name**](ApplicationsApi.md#get_contribution_type_by_name) | **GET** /applications/{applicationId}/contributionTypes/{name} | Get contribution type by name
[**get_contribution_types**](ApplicationsApi.md#get_contribution_types) | **GET** /applications/{applicationId}/contributionTypes | Get contributionTypes
[**update_contribution_type_by_name**](ApplicationsApi.md#update_contribution_type_by_name) | **PUT** /applications/{applicationId}/contributionTypes/{name} | Update contribution type by name


# **create_application**
> CreateApplication201Response create_application()

Create a new application

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.create_application201_response import CreateApplication201Response
from openapi_client.model.application_request import ApplicationRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_request = ApplicationRequest(
        name="name_example",
        client_id="client_id_example",
        url="url_example",
    ) # ApplicationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new application
        api_response = api_instance.create_application(application_request=application_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)|  | [optional]

### Return type

[**CreateApplication201Response**](CreateApplication201Response.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contribution_type**
> CreateContributionType201Response create_contribution_type(application_id)

Create a new contribution type

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.contribution_type_request import ContributionTypeRequest
from openapi_client.model.create_contribution_type201_response import CreateContributionType201Response
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "applicationId_example" # str | The id of the application
    contribution_type_request = ContributionTypeRequest(
        name="name_example",
        review_config=ReviewConfig(
            review_policy=ReviewPolicy("majority"),
            reviewer_amount=1,
        ),
    ) # ContributionTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new contribution type
        api_response = api_instance.create_contribution_type(application_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->create_contribution_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new contribution type
        api_response = api_instance.create_contribution_type(application_id, contribution_type_request=contribution_type_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->create_contribution_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application |
 **contribution_type_request** | [**ContributionTypeRequest**](ContributionTypeRequest.md)|  | [optional]

### Return type

[**CreateContributionType201Response**](CreateContributionType201Response.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_by_id**
> ApplicationResponse get_application_by_id(application_id)

Get application by Id

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.application_response import ApplicationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "applicationId_example" # str | The id of the application to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Get application by Id
        api_response = api_instance.get_application_by_id(application_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_application_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application to retrieve |

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> [ApplicationResponse] get_applications()

Get applications

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.application_response import ApplicationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    start = 1 # int | The first index of the elements to return (optional)
    length = 1 # int | The amount of the elements to return (optional)
    owner_id = "ownerId_example" # str |  (optional)
    client_id = "clientId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get applications
        api_response = api_instance.get_applications(start=start, length=length, owner_id=owner_id, client_id=client_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| The first index of the elements to return | [optional]
 **length** | **int**| The amount of the elements to return | [optional]
 **owner_id** | **str**|  | [optional]
 **client_id** | **str**|  | [optional]

### Return type

[**[ApplicationResponse]**](ApplicationResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contribution_type_by_name**
> ContributionTypeResponse get_contribution_type_by_name(application_id, name)

Get contribution type by name

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.contribution_type_response import ContributionTypeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "applicationId_example" # str | The id of the application
    name = "name_example" # str | The name of the contribution type

    # example passing only required values which don't have defaults set
    try:
        # Get contribution type by name
        api_response = api_instance.get_contribution_type_by_name(application_id, name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_contribution_type_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application |
 **name** | **str**| The name of the contribution type |

### Return type

[**ContributionTypeResponse**](ContributionTypeResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contribution_types**
> [ContributionTypeResponse] get_contribution_types(application_id)

Get contributionTypes

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.contribution_type_response import ContributionTypeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "applicationId_example" # str | The id of the application

    # example passing only required values which don't have defaults set
    try:
        # Get contributionTypes
        api_response = api_instance.get_contribution_types(application_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->get_contribution_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application |

### Return type

[**[ContributionTypeResponse]**](ContributionTypeResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contribution_type_by_name**
> update_contribution_type_by_name(application_id, name)

Update contribution type by name

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import applications_api
from openapi_client.model.contribution_type_request import ContributionTypeRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuth
configuration.api_key['JWTAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = applications_api.ApplicationsApi(api_client)
    application_id = "applicationId_example" # str | The id of the application
    name = "name_example" # str | The name of the contribution type
    contribution_type_request = ContributionTypeRequest(
        name="name_example",
        review_config=ReviewConfig(
            review_policy=ReviewPolicy("majority"),
            reviewer_amount=1,
        ),
    ) # ContributionTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update contribution type by name
        api_instance.update_contribution_type_by_name(application_id, name)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->update_contribution_type_by_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update contribution type by name
        api_instance.update_contribution_type_by_name(application_id, name, contribution_type_request=contribution_type_request)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplicationsApi->update_contribution_type_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application |
 **name** | **str**| The name of the contribution type |
 **contribution_type_request** | [**ContributionTypeRequest**](ContributionTypeRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

