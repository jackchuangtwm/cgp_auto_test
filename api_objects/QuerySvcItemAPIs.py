import os
from utils.api_utlis import APIBase


class QuerySvcItemAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def post_data_info(self, data_info, headers):

        url = f"{os.getenv('API_SERVER')}/portal/api/querySvcItem"

        headers = {
            "Authorization":headers
        }

        self.api_request("post", url, data=data_info, headers=headers)

        return self.response
    