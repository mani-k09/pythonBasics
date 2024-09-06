import requests
import json

git_url="https://api.github.com/users/mani-k09/repos"

def get_repo_list():
    git_response = requests.get(git_url)
    my_repo =git_response.json()
    #print(type(my_repo))
    return my_repo
    #print(repo)
    #print(repo[0])

def find_repoName_url(my_repo):
    for repo in my_repo:
        print(f"The repository name is {repo['name']} and the url is {repo['url']}")

def print_git_response(my_repo):
    print(convert_json_to_string(my_repo))

def convert_json_to_string(response_input):
    coverted_json = json.dumps(response_input, indent= 4 )
    #print(type(coverted_json))
    print(coverted_json)


print_git_response(get_repo_list())
find_repoName_url(get_repo_list())