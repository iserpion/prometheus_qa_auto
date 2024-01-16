import requests

class GitHub:

    def get_user(self, username):
        response = requests.get(f'https://api.github.com/users/{username}')
        body = response.json()

        return body
    
    def search_repo(self, name):
        response = requests.get(
            'https://api.github.com/search/repositories',
            params={'q': name}
        )
        body = response.json()

        return body

    def list_branches(self, username, repo_name):
        response = requests.get(f'https://api.github.com/repos/{username}/{repo_name}/branches')
        body = response.json()

        return body
    
    def list_commits_filtered_by_branch_and_committer(self, username, repo_name, branch, committer):
        payload = {'sha': branch, 'committer': committer}
        response = requests.get(
            f'https://api.github.com/repos/{username}/{repo_name}/commits',
            params = payload
        )
        body = response.json()

        return body
    
    def attempt_to_create_issue(self, username, repo_name):
        payload = {"title":"Test bug from API",
                   "body":"Test bug from API",
                   "assignees":[f'{username}']
                   }
        response = requests.post(
            f'https://api.github.com/repos/{username}/{repo_name}/issues',
            data=payload
            )
        status_code = response.status_code

        return status_code
    
    def get_followers(self, username):
        response = requests.get(f'https://api.github.com/users/{username}/followers')
        return response