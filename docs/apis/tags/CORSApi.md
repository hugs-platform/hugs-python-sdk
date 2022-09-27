<a name="__pageTop"></a>
# openapi_client.apis.tags.cors_api.CORSApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contributions_options**](#contributions_options) | **options** /contributions | CORS support

# **contributions_options**
<a name="contributions_options"></a>
> contributions_options()

CORS support

Enable CORS by returning correct headers 

### Example

* Api Key Authentication (JWTAuth):
```python
import openapi_client
from openapi_client.apis.tags import cors_api
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
    api_instance = cors_api.CORSApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # CORS support
        api_response = api_instance.contributions_options()
    except openapi_client.ApiException as e:
        print("Exception when calling CORSApi->contributions_options: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#contributions_options.ApiResponseFor200) | Default response for CORS method

#### contributions_options.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional
Access-Control-Allow-Methods | AccessControlAllowMethodsSchema | | optional
Access-Control-Allow-Headers | AccessControlAllowHeadersSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowMethodsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowHeadersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

[JWTAuth](../../../README.md#JWTAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

