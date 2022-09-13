# openapi_client.ContributionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contributions_health**](ContributionsApi.md#contributions_health) | **GET** /health | Checking the health of the contributions service
[**create_contribution**](ContributionsApi.md#create_contribution) | **POST** /contributions | Create a new contribution
[**create_resolution**](ContributionsApi.md#create_resolution) | **POST** /contributions/{contributionId}/resolutions | Resolve a contribution
[**get_contributions**](ContributionsApi.md#get_contributions) | **GET** /contributions | Get contributions
[**get_contributions_by_id**](ContributionsApi.md#get_contributions_by_id) | **GET** /contributions/{contributionId} | Get contribution by Id


# **contributions_health**
> contributions_health()

Checking the health of the contributions service

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import contributions_api
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
    api_instance = contributions_api.ContributionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Checking the health of the contributions service
        api_instance.contributions_health()
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->contributions_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contribution**
> CreateApplication201Response create_contribution()

Create a new contribution

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import contributions_api
from openapi_client.model.contribution_request import ContributionRequest
from openapi_client.model.create_application201_response import CreateApplication201Response
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
    api_instance = contributions_api.ContributionsApi(api_client)
    contribution_request = ContributionRequest(
        app_id="app_id_example",
        contribution_type="contribution_type_example",
        external_resource_ref="external_resource_ref_example",
        contribution_data={},
    ) # ContributionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new contribution
        api_response = api_instance.create_contribution(contribution_request=contribution_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->create_contribution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contribution_request** | [**ContributionRequest**](ContributionRequest.md)|  | [optional]

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

# **create_resolution**
> CreateResolution201Response create_resolution(contribution_id)

Resolve a contribution

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import contributions_api
from openapi_client.model.create_resolution201_response import CreateResolution201Response
from openapi_client.model.resolution_request import ResolutionRequest
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
    api_instance = contributions_api.ContributionsApi(api_client)
    contribution_id = "contributionId_example" # str | The id of the contribution
    resolution_request = ResolutionRequest(
        accepted=True,
    ) # ResolutionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resolve a contribution
        api_response = api_instance.create_resolution(contribution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->create_resolution: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resolve a contribution
        api_response = api_instance.create_resolution(contribution_id, resolution_request=resolution_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->create_resolution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contribution_id** | **str**| The id of the contribution |
 **resolution_request** | [**ResolutionRequest**](ResolutionRequest.md)|  | [optional]

### Return type

[**CreateResolution201Response**](CreateResolution201Response.md)

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

# **get_contributions**
> [ContributionResponse] get_contributions()

Get contributions

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import contributions_api
from openapi_client.model.contribution_response import ContributionResponse
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
    api_instance = contributions_api.ContributionsApi(api_client)
    external_resource_ref = "externalResourceRef_example" # str | The external resource ref of the contribution (optional)
    contribution_type = "contributionType_example" # str | The type of the contribution (optional)
    user_id = "userId_example" # str | The id of the user who created the contribution (optional)
    app_id = "appId_example" # str | The id of the app for which the contribution was created (optional)
    start = 1 # int | The first index of the contributions to return (optional)
    length = 1 # int | The amount of the contributions to return (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get contributions
        api_response = api_instance.get_contributions(external_resource_ref=external_resource_ref, contribution_type=contribution_type, user_id=user_id, app_id=app_id, start=start, length=length)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->get_contributions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_resource_ref** | **str**| The external resource ref of the contribution | [optional]
 **contribution_type** | **str**| The type of the contribution | [optional]
 **user_id** | **str**| The id of the user who created the contribution | [optional]
 **app_id** | **str**| The id of the app for which the contribution was created | [optional]
 **start** | **int**| The first index of the contributions to return | [optional]
 **length** | **int**| The amount of the contributions to return | [optional]

### Return type

[**[ContributionResponse]**](ContributionResponse.md)

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

# **get_contributions_by_id**
> ContributionResponse get_contributions_by_id(contribution_id)

Get contribution by Id

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import contributions_api
from openapi_client.model.contribution_response import ContributionResponse
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
    api_instance = contributions_api.ContributionsApi(api_client)
    contribution_id = "contributionId_example" # str | The id of the contribution to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Get contribution by Id
        api_response = api_instance.get_contributions_by_id(contribution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContributionsApi->get_contributions_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contribution_id** | **str**| The id of the contribution to retrieve |

### Return type

[**ContributionResponse**](ContributionResponse.md)

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

