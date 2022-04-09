import requests
import getpass
import sys


def get_repos(username, auth):
    """ username should be a string
    auth should be a tuple of username and password.
    eventually, we'll switch it to use an oauth token
    """
    tmpl = "https://api.github.com/users/{username}/repos?per_page=100"
    url = tmpl.format(username=username)
    return _getter(url, auth)


def get_issues(username, repo, auth):
    """ username and repo should be strings
    auth should be a tuple of username and password.
    eventually, we'll switch it to use an oauth token
    """
    tmpl = "https://api.github.com/repos/{username}/{repo}/issues?state=closed"
    url = tmpl.format(username=username, repo=repo)
    return _getter(url, auth)


def get_all_issues(username,repo, auth):
    '''
    for repo in get_repos(username, auth):
        if not repo['has_issues']:
            continue
        for issue in get_issues(username, repo['name'], auth):
            yield issue
    '''
    for issue in get_issues(username, repo , auth):
        yield issue


def _getter(url, auth):
    """ Pagination utility.  Obnoxious. """

    link = dict(next=url)
    while 'next' in link:
        response = requests.get(link['next'], auth=auth)

        # And.. if we didn't get good results, just bail.
        if response.status_code != 200:
            raise IOError(
                "Non-200 status code %r; %r; %r" % (
                    response.status_code, url, response.json()))

        for result in response.json():
            yield result

        link = _link_field_to_dict(response.headers.get('link', None))


def _link_field_to_dict(field):
    """ Utility for ripping apart github's Link header field.
    It's kind of ugly.
    """

    if not field:
        return dict()

    return dict([
        (
            part.split('; ')[1][5:-1],
            part.split('; ')[0][1:-1],
        ) for part in field.split(', ')
    ])


if __name__ == '__main__':
    #username = raw_input("Username: ")
    username= "signalapp"
    password = "hello"
    repo = "Signal-Android"
    auth = (username, password)
    issue_list = []
    for issue in get_all_issues(username,repo, auth):
        issue_list.append(issue['body'])
        print(len(issue_list))

    print(len(issue_list))
