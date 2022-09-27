from openapi_client.paths.contributions.get import ApiForget
from openapi_client.paths.contributions.post import ApiForpost
from openapi_client.paths.contributions.options import ApiForoptions


class Contributions(
    ApiForget,
    ApiForpost,
    ApiForoptions,
):
    pass
