import os

import logging

import git
from github import Github
from github.GithubException import GithubException


from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = '.'
RESPONSE_DIR = 'chat_gpt_response'

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

REPO_NAME = 'chatGPT-auto-git-deploy'


class Setup:
    def __init__(self):
        self.must_set()

    def must_set(self):
        """
        This method do minimal setup required to run this project.
        :return:
        """
        self.init_git()

    def init_git(self):
        """
        This method init git and push to origin
        :return:
        """

        if not not self.is_git_repo(os.path.abspath(PROJECT_DIR)):
            logging.warning('This directory already has git repo, try with another directory')
            return


        try:
            github = Github(GITHUB_ACCESS_TOKEN)
            github_user = github.get_user()
            repo = github_user.create_repo(REPO_NAME)
        except GithubException as ge:
            ge_data = ge.data
            logging.warning(f"{ge_data['message']}- {ge_data['errors'][0]['message']}\nTry with new repository!")
            return

        # Setup local repo
        self.setup_local_repo()

    @staticmethod
    def is_git_repo(path):
        try:
            _ = git.Repo(os.path.abspath(path)).git_dir
            return True
        except git.exc.InvalidGitRepositoryError:
            return False

    @staticmethod
    def setup_local_repo():
        os.system("git init")
        os.system("git add .gitignore")
        os.system("git commit -m \"Initial commit\"")
        os.system(f"git add {PROJECT_DIR}")
        os.system('git commit -m \"Init codebase\"')
        os.system("git branch -M master")
        os.system(
            "git remote add origin " + f'https://{GITHUB_ACCESS_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git/'
        )
        os.system("git push origin master")


if __name__ == '__main__':
    Setup()
