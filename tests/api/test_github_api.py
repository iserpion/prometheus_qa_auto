import pytest


# Required part of project:

@pytest.mark.rest_api
def test_user_exists(github_api):
    """
    Test checks that existing GitHub user is received from /users endpoint
    """

    user = github_api.get_user("ekmett")

    assert user["login"] == "ekmett", "Expected user is not received"


@pytest.mark.rest_api
def test_user_not_exists(github_api):
    """
    Test checks non-existent GitHub user isn't received from /users endpoint
    """

    response = github_api.get_user("butenkosergii")

    assert response["message"] == "Not Found", "Unexpected response message"


@pytest.mark.rest_api
def test_repo_can_be_found(github_api):
    """
    Test checks that existing GitHub repo
    is received from /search/repositories endpoint
    """

    response = github_api.search_repo("become-qa-auto")

    assert (
        "become-qa-auto" in response["items"][0]["name"]
    ), "Expected repo is not found"


@pytest.mark.rest_api
def test_repo_cannot_be_found(github_api):
    """
    Test checks that non-existent GitHub repo
    isn't received from /search/repositories endpoint
    """

    response = github_api.search_repo("funny_repo_non_exist")

    assert response["total_count"] == 0, "Unexpected search result"


@pytest.mark.rest_api
def test_repo_with_single_char_be_found(github_api):
    """
    Test checks that single char search result
    is not empty from /search/repositories endpoint
    """

    response = github_api.search_repo("s")

    assert response["total_count"] > 0


# Individual part of project:

@pytest.mark.rest_api
@pytest.mark.parametrize("branch_name", ["main", "testing", "protected_test_branch"])
def test_repo_branches_are_listed(github_api, branch_name):
    """
    Test checks that GitHub API returns
    list of branches for valid user and valid repo
    """

    response = github_api.list_branches("iserpion", "prometheus_qa_auto")

    is_listed = False
    for item in response:
        if item["name"] == branch_name:
            is_listed = True
            break

    assert is_listed, f"{branch_name} branch is not listed in response"


@pytest.mark.rest_api
def test_committer_email_in_commits_from_web(github_api):
    """
    Test checks that committer email in all commits
    from GitHub website is 'noreply@github.com'
    """

    response = github_api.list_commits_filtered_by_branch_and_committer(
        "iserpion", 
        "prometheus_qa_auto", 
        "testing", 
        "web-flow"
    )

    is_valid_email = False
    for item in response:
        if item["commit"]["committer"]["email"] == "noreply@github.com":
            is_valid_email = True
        else:
            is_valid_email = False

    assert is_valid_email, "Email is not 'noreply@github.com' in commit"


@pytest.mark.rest_api
def test_create_issue_without_authorization(github_api):
    """
    Test status code on attempt to create an issue
    via GitHub API without authorization
    """

    username = "iserpion"
    repo_name = "prometheus_qa_auto"
    title = "Test defect from API"
    body = "Test defect created via GitHub API"

    response = github_api.attempt_to_create_issue(
        username,
        repo_name,
        title,
        body
    )

    assert response.status_code == 404, "Status code is not 404"


@pytest.mark.rest_api
def test_follower_site_admin_exists(github_api):
    """
    This test checks that in GitHub API user followers
    response exists "site admin" follower
    """

    response = github_api.get_followers("ekmett").json()

    is_admin = False
    for item in response:
        if item["site_admin"] == True:
            is_admin = True
            break

    assert is_admin, "There is no site admin users in followers list"


@pytest.mark.rest_api
@pytest.mark.parametrize(
    "key, value",
    [
        pytest.param(
            "Server",
            "GitHub.com",
            id="Server",
        ),
        pytest.param(
            "Content-Type",
            "application/json; charset=utf-8",
            id="Content-Type",
        ),
        pytest.param(
            "Vary",
            "Accept, Accept-Encoding, Accept, X-Requested-With",
            id="Vary",
        ),
        pytest.param(
            "Access-Control-Allow-Origin",
            "*",
            id="Access-Control-Allow-Origin",
        ),
        pytest.param(
            "Content-Encoding",
            "gzip",
            id="Content-Encoding",
        ),
    ],
)
def test_headers_in_followers_response(github_api, key, value):
    """This test checks headers in GitHub API followers response"""

    response_headers = github_api.get_followers("ekmett").headers

    assert response_headers[key] == value, f"{key} header is missing in response"
