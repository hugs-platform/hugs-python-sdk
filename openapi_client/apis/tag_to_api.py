import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.contributions_api import ContributionsApi
from openapi_client.apis.tags.applications_api import ApplicationsApi
from openapi_client.apis.tags.cors_api import CORSApi
from openapi_client.apis.tags.reviews_api import ReviewsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONTRIBUTIONS: ContributionsApi,
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.CORS: CORSApi,
        TagValues.REVIEWS: ReviewsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONTRIBUTIONS: ContributionsApi,
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.CORS: CORSApi,
        TagValues.REVIEWS: ReviewsApi,
    }
)
