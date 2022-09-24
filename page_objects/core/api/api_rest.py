from requests import request, Session
from requests.auth import AuthBase
from requests.exceptions import HTTPError, RequestException
from typing import List

import structlog

logger = structlog.get_logger(__name__)


class RequestAPI:

    '''
    API Requests : POST, GET, PUT, DELET, OPTIONS
    '''

    def __init__(self, method: str, url: str, header: str, param: dict| None =  None, json: dict|None = None, auth:AuthBase|None = None):
        self.method =  method # HTTP method POST, GET, PUT, DELET, etc
        self.url = url # endpoint url
        self.header = header # key, value pair of header  
        self.param = param # query parameter 
        self.json = json  # payload 
        self.auth = auth # Authentication
        self.timeout = 10


    def send_request(self):
        try:
            logger.info(
                "Sending API request",
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
                auth=auth
            )
            response = requests(
                method = self.method,
                url = self.url,
                params = self.param,
                json = self.json,
                headers = self.header,
                auth = self.auth
            )
        except HTTPError as http_err:
            logger.error(
                "An HTTP error occurred.",
                url=self.url,
                params=self.params,
                headers=self.headers,
                status_code=http_err.response.status_code,
                response_output=http_err.response.text
            )
        except RequestException as req_exc:
            logger.error(
                "Server side error, unable to handle your request",
                url=url,
                params=params,
                headers=headers,
                args=req_exc.args,
            )