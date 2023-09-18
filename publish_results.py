import testrail_api
import os

def publish_results():
    client = testrail_api.TestRailAPI(
        url=['https://swe401pro.testrail.io'],
        email=['gr.eg.or.ymj.en.son6@gmail.com'],
        password=['aPAgZT6rynaBWwcJA48W-EK89Ugq/Qdsv6pBZeL2B']
    )

    project_id = ['1']

    run_id = ['TESTRAIL_RUN_ID']

    test_results = {
        'CT': {
            'status_id': 1, 
            'comment': 'Test passed successfully.'
        },
        'CF': {
            'status_id': -1,
            'comment': 'Test failed due to assertion error.'
        }
    }


    for case_id, result in test_results.items():
        client.send_post(
            f'add_result_for_case/{run_id}/{case_id}',
            result
        )
        
if __name__ == "__main__":
    publish_results()