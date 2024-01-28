import pytest
from modules.api.baseclasses.response import Response
from modules.common.schemas.follower import Follower


# Required part of project:
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    response = github_api.get_user("butenkosergii")
    assert response["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    response = github_api.search_repo("become-qa-auto")
    assert response["total_count"] == 54
    assert "become-qa-auto" in response["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    response = github_api.search_repo("funny_repo_non_exist")
    assert response["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    response = github_api.search_repo("s")
    assert response["total_count"] != 0


# Individual part of project:
@pytest.mark.api
@pytest.mark.parametrize("branch_name", ["main", "testing", "protected_test_branch"])
def test_repo_branches_are_listed(github_api, branch_name):
    """Test checks that GitHub API returns
    list of branches for valid user and valid repo."""

    response = github_api.list_branches("iserpion", "prometheus_qa_auto")

    is_listed = False
    for item in response:
        if item["name"] == branch_name:
            is_listed = True
            break

    assert is_listed == True, f"{branch_name} branch is not listed in response"


@pytest.mark.api
def test_committer_email_in_commits_from_web(github_api):
    """Test checks that committer email in all commits
    from GitHub website is 'noreply@github.com'"""

    response = github_api.list_commits_filtered_by_branch_and_committer(
        "iserpion", "prometheus_qa_auto", "testing", "web-flow"
    )

    is_valid_email = False
    for item in response:
        if item["commit"]["committer"]["email"] == "noreply@github.com":
            is_valid_email = True
        else:
            is_valid_email = False

    assert is_valid_email == True, "Email is not 'noreply@github.com' in commit"


@pytest.mark.api
def test_create_issue_without_authorization(github_api):
    """Test status code on attempt to create an issue
    via GitHub API without authorization"""

    status_code = github_api.attempt_to_create_issue("iserpion", "prometheus_qa_auto")

    assert status_code == 404, "Status code is not 404"


@pytest.mark.api
def test_validate_followers(github_api):
    """This test validates GitHub API user followers
    response body using Pydantic library and checks response status code"""

    Response(github_api.get_followers("defunkt")).validate(Follower).assert_status_code(
        200
    )


@pytest.mark.skip("Test skipping")
@pytest.mark.api
def test_follower_site_admin_exists(github_api):
    """This test checks that in GitHub API user followers
    response exists follower with key "site_admin":true"""

    response = github_api.get_followers("defunkt").json()

    is_admin = False
    for item in response:
        if item["site_admin"] == True:
            is_admin = True
            break

    assert is_admin, "There is no site admin users in followers list"


@pytest.mark.api
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

    response_headers = github_api.get_followers("defunkt").headers

    assert response_headers[key] == value, f"{key} header is not existed in response"
