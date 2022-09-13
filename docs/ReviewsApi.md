# openapi_client.ReviewsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contributions_health**](ReviewsApi.md#contributions_health) | **GET** /health | Checking the health of the contributions service
[**create_review**](ReviewsApi.md#create_review) | **POST** /contributions/{contributionId}/reviews | Create a new review
[**get_reviews_by_contribution**](ReviewsApi.md#get_reviews_by_contribution) | **GET** /contributions/{contributionId}/reviews | Get reviews for a contribution


# **contributions_health**
> contributions_health()

Checking the health of the contributions service

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import reviews_api
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
    api_instance = reviews_api.ReviewsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Checking the health of the contributions service
        api_instance.contributions_health()
    except openapi_client.ApiException as e:
        print("Exception when calling ReviewsApi->contributions_health: %s\n" % e)
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

# **create_review**
> CreateReview201Response create_review(contribution_id)

Create a new review

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import reviews_api
from openapi_client.model.review_request import ReviewRequest
from openapi_client.model.create_review201_response import CreateReview201Response
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
    api_instance = reviews_api.ReviewsApi(api_client)
    contribution_id = "contributionId_example" # str | The id of the contribution
    review_request = ReviewRequest(
        approved=True,
    ) # ReviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new review
        api_response = api_instance.create_review(contribution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReviewsApi->create_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new review
        api_response = api_instance.create_review(contribution_id, review_request=review_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReviewsApi->create_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contribution_id** | **str**| The id of the contribution |
 **review_request** | [**ReviewRequest**](ReviewRequest.md)|  | [optional]

### Return type

[**CreateReview201Response**](CreateReview201Response.md)

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

# **get_reviews_by_contribution**
> [ReviewResponse] get_reviews_by_contribution(contribution_id)

Get reviews for a contribution

### Example

* Api Key Authentication (JWTAuth):

```python
import time
import openapi_client
from openapi_client.api import reviews_api
from openapi_client.model.review_response import ReviewResponse
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
    api_instance = reviews_api.ReviewsApi(api_client)
    contribution_id = "contributionId_example" # str | 
    reviewer_id = "reviewerId_example" # str | The id of the reviewer (optional)
    start = 1 # int | The first index of the contributions to return (optional)
    length = 1 # int | The amount of the contributions to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get reviews for a contribution
        api_response = api_instance.get_reviews_by_contribution(contribution_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReviewsApi->get_reviews_by_contribution: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get reviews for a contribution
        api_response = api_instance.get_reviews_by_contribution(contribution_id, reviewer_id=reviewer_id, start=start, length=length)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ReviewsApi->get_reviews_by_contribution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contribution_id** | **str**|  |
 **reviewer_id** | **str**| The id of the reviewer | [optional]
 **start** | **int**| The first index of the contributions to return | [optional]
 **length** | **int**| The amount of the contributions to return | [optional]

### Return type

[**[ReviewResponse]**](ReviewResponse.md)

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

