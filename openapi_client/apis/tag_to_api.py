import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.applications_api import ApplicationsApi
from openapi_client.apis.tags.contributions_api import ContributionsApi
from openapi_client.apis.tags.reviews_api import ReviewsApi
from openapi_client.apis.tags.cors_api import CorsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.CONTRIBUTIONS: ContributionsApi,
        TagValues.REVIEWS: ReviewsApi,
        TagValues.CORS: CorsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APPLICATIONS: ApplicationsApi,
        TagValues.CONTRIBUTIONS: ContributionsApi,
        TagValues.REVIEWS: ReviewsApi,
        TagValues.CORS: CorsApi,
    }
)
