import os
from autopush_lib.chatgpt_wrapper.chatgpt import ChatGPT

PROGRAMMING_QUESTION = 'Write one useful program in any language with comments so that it is easy to understand for ' \
                       'anyone and also send it in .MD format '
FILE_RECOMMENDATION_QUESTION = 'What can be the best file name and also make it random and never used before for this ' \
                               'programming file without extension? '
COMMIT_MSG_QUESTION = 'What is appropriate commit message for this committing above code?'


class ChatGptQuestion:
    def __init__(self):
        self.__commit_message = COMMIT_MSG_QUESTION
        self.__common_programming = PROGRAMMING_QUESTION
        self.__file_recommendation = FILE_RECOMMENDATION_QUESTION

    def get_common_programming_question(self):
        return self.__common_programming

    def get_file_recommendation_question(self):
        return self.__file_recommendation

    def get_commit_message_question(self):
        return self.__commit_message


class ChatGPTGitPush(ChatGPT, ChatGptQuestion):
    def __init__(self, model_engine, openai_api_key, repo):
        ChatGPT.__init__(self, model_engine, openai_api_key)
        ChatGptQuestion.__init__(self)

        self.repo = repo
        self.question = ''
        self.answer_file_name = ''
        self.answer = None

    def ask_question(self, question):
        self.answer = self.ask(question)

    def write_answer_to_file(self):
        self.answer_file_name = self.ask(self.get_file_recommendation_question()).strip() + '.md'
        with open(self.repo + self.answer_file_name, 'w') as f:
            f.write(self.answer)

        with open(self.repo + 'README.md', 'w') as f:
            f.write(self.answer)

    def push_file_to_github(self):
        commit_msg = self.ask(self.get_commit_message_question()).strip()
        os.system("git add " + self.repo + self.answer_file_name)
        os.system(f"git commit -m '{commit_msg}'")
        os.system('git add ' + self.repo + 'README.md')
        os.system(f"git commit -m \"Updated README.md\"")
        os.system('git push origin master')

    def do_all_operations(self):
        self.ask_question(self.get_common_programming_question())
        self.write_answer_to_file()
        self.push_file_to_github()
