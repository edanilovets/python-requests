import requests


class GithubApi:

    def test_github_api(self):
        r = requests.get('https://api.github.com/user', auth=('edanilovets', 'anepam88'))
        print(r.json())
        assert 1