from github import Github
import base64

g = Github("github_auth_token")

def readProgress():
	repo = g.get_repo("democat3457/ChairBot")
	contents = repo.get_contents("progressServer4.json")
	s = contents.content
	s = s.encode('ascii')
	s = base64.b64decode(s)
	s = s.decode('ascii')
	return s

def updateProgress(data):
	repo = g.get_repo("democat3457/ChairBot")
	contents = repo.get_contents("progressServer4.json")
	repo.update_file(contents.path, "Automated json update", data, contents.sha)
