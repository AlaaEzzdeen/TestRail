import requests
import testrail_api

# GitHub API endpoint to get recent actions
github_api_url = 'https://api.github.com/repos/AlaaEzzdeen/TestRail/actions/runs'

# TestRail API endpoint and credentials
testrail_url = 'https://swe401pro.testrail.io/'
testrail_user = 'gr.eg.or.ymj.en.son6@gmail.com'
testrail_password = 'StarTrail*1'

# GitHub repository information
owner = 'AlaaEzzdeen'
repo = 'https://github.com/AlaaEzzdeen/TestRail'

# TestRail project and suite IDs
project_id = 1
suite_id = 1

# Fetch recent actions from GitHub
response = requests.get(github_api_url.format(owner=owner, repo=repo))
actions = response.json().get('workflow_runs', [])

# Initialize TestRail API client
client = testrail_api.TestRailAPI(testrail_url, testrail_user, testrail_password)

# Create test cases in TestRail
for action in actions:
    # Extract relevant information
    action_id = action['id']
    action_name = action['name']
    action_status = action['status']

    # Create a new test case in TestRail
    case = client.create_case(project_id, suite_id, action_name, action_name)

    # Set the custom case fields based on the GitHub action information
    client.update_case(case['id'], {'custom_action_id': action_id, 'custom_action_status': action_status})

    print(f"Test case created: {case['title']}")