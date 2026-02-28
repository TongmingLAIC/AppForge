from typing import Any, Dict, List, Union

from .Base import OpenAIFormatLLM


class custom_openai_compatible(OpenAIFormatLLM):
    """
    Minimal template for integrating a new text-only LLM backend.

    Usage:
        from LLMs.Template import custom_openai_compatible
        model = custom_openai_compatible(api_key_path="your_api_key_file")
    """

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            api_base="https://api.openai.com/v1",
            model="gpt-4o-mini",
        )

    def __call__(self, prompt: List[Dict[str, str]]) -> Dict[str, Union[str, int, Any]]:
        return super().call(prompt)
