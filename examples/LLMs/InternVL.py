from typing import List, Dict, Union, Any
from pathlib import Path
from .Base import OpenAIFormatLLM

class internvl(OpenAIFormatLLM):

    def __init__(self, *args, **kwargs):
        if "api_base" not in kwargs:
            raise ValueError(
                "InternVL requires 'api_base' to be provided (e.g. "
                "api_base='https://your-internvl-endpoint/v1'). "
                "InternVL endpoints vary by deployment and are not "
                "centrally hosted like OpenAI. "
                "Note: the previous default pointed to DeepSeek's API, "
                "which was a copy-paste error — use 'deepseekchat' instead."
            )
        super().__init__(*args, **kwargs)

    def __call__(self, prompt: List[Dict[str, str]]) -> Dict[str, Union[str, int, Any]]:
        return super().call(prompt)
