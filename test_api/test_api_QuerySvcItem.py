import pytest
import logging
import json

from test_data.get_data_from_excel import process_excel_data
from api_objects.QuerySvcItemAPIs import QuerySvcItemAPIs
from utils.object_utils import ObjectUtils

# EXCEL 路徑
file_path = r'test_data/QuerySvcItemAPIs_TestCase.xlsx'
sheet_name = '工作表1'
data_dicts = process_excel_data(file_path, sheet_name)

@pytest.mark.parametrize('data_dict', data_dicts)
def test_api_QuerySvcItemAPIs_success(data_dict, get_session):

    headers = data_dict['Authorization']
    request_body = data_dict['Body'] 
    excel_result = data_dict['result']   
    
    try:
        querySvcItem_apis = QuerySvcItemAPIs(get_session)
        response = querySvcItem_apis.post_data_info(request_body, headers)        
    
        if response.status_code != 200:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
            return

        response_data = response.json()    
        excel_result_data = json.loads(excel_result)
        keys_to_compare = ["return_code", "return_msg", "ref_id", "uid", "svc_item", "plan_code"]

        for key in keys_to_compare:
            ObjectUtils.equal_str(key, excel_result_data[key], response_data[key]) 

    except Exception as e:
        logging.exception(f"An error occurred: {e}")
        raise

    finally:
        logging.info("END")
