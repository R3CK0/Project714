import openai
import os

class ToolUsage:
    def __init__(self):
        self.API_KEY = open("../../OpenAIApproach/OpenAIAPIKey.txt", "r").read()
        openai.api_key = self.API_KEY

    def promtToTool(self, prompt):
        pass