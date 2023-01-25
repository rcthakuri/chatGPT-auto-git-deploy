import os
import time
from dotenv import load_dotenv

from autopush_lib.chatgpt_git_push.git_auto_push import ChatGPTGitPush

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL_ENGINE = os.getenv('OPENAI_MODEL_ENGINE')
REPO = 'chat_gpt_response/'

if __name__ == '__main__':
    run_time = time.time()
    while True:
        if (run_time - time.time()) / 60 / 60 \
                >= 0.01:
            chatgpt_git_push = ChatGPTGitPush(OPENAI_MODEL_ENGINE, OPENAI_API_KEY, REPO)
            chatgpt_git_push.do_all_operations()
            run_time = time.time()
            print('Pushing new changes....')
        time.sleep(1)
