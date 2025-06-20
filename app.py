from smolagents import CodeAgent, HfApiModel, load_tool, tool, Tool
import datetime
import os
import io
import pytz
import yaml
import torch
import soundfile as sf
from huggingface_hub import InferenceClient
from tools.final_answer import FinalAnswerTool
from tools.visit_webpage import VisitWebpageTool
from tools.web_search import DuckDuckGoSearchTool

from Gradio_UI import GradioUI


class TextToSpeechTool(Tool):
    description = "This tool creates an audio tensor from the input, which is text. For audio tasks, the output from this tool is the final answer."
    name = "text_to_speech"
    inputs = {"text": {"type": "string", "description": "This is the text that will be converted into speech"}}
    output_type = "audio"

    client = InferenceClient(
        provider="auto",
        api_key=os.environ["HF_TOKEN"],
    )

    def forward(self, text: str) -> torch.Tensor:
        output = self.client.text_to_speech(
            text,
            model="ResembleAI/chatterbox",
        )

        audio, _ = sf.read(io.BytesIO(output))

        return torch.from_numpy(audio)


@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()
web_search = DuckDuckGoSearchTool()
visit_page = VisitWebpageTool()
read_out_loud = TextToSpeechTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None
)

# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
demo = CodeAgent(
    model=model,
    tools=[
        get_current_time_in_timezone,
        read_out_loud,
        image_generation_tool,
        web_search,
        visit_page,
        final_answer
    ], ## add your tools here (don't remove final answer)
    additional_authorized_imports=['torch.Tensor'],
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


GradioUI(demo).launch()