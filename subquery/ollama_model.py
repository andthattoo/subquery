import re
from typing import List
from ollama import Client
from .core import SubqueryGenerator, SubqueryResult


class OllamaSubqueryGenerator(SubqueryGenerator):
    def __init__(self):
        self.client = Client()

    def get_text_between_tags(self, text: str, tag: str) -> List[str]:
        pattern = f'<{tag}>(.*?)</{tag}>'
        return re.findall(pattern, text, re.DOTALL)

    def generate(self, question: str) -> SubqueryResult:
        prompt = f"Generate subqueries for a given question. <question>{question}</question>"
        response = self.client.generate(model="andthattoo/subquery-smollm", prompt=prompt, options={"num_predict": 100})

        follow_ups = self.get_text_between_tags(response['response'], "follow_up")
        subqueries = self.get_text_between_tags(response['response'], "subquery")

        follow_ups = list(set([s.lower() for s in follow_ups]))
        subqueries = list(set([s.lower() for s in subqueries]))

        return SubqueryResult(follow_ups, subqueries)