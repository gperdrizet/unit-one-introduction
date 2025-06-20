from typing import Any, Optional
from smolagents.tools import Tool

class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer or result for the question or request. You do not need to tell the user that the task is complete, simply return the result."
    inputs = {'answer': {'type': 'any', 'description': 'An image, audio tensor or text response'}}
    output_type = "any"

    def forward(self, answer: Any) -> Any:
        return answer

    def __init__(self, *args, **kwargs):
        self.is_initialized = False
