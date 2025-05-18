from crewai import LLM

llm = LLM(
    model='ollama/mistral-nemo',
    base_url='http://localhost:11434',
    num_ctx = 30000,  # Number of context tokens (default: 4096)
)

import litellm
from litellm.llms.ollama.completion.transformation import ollama_pt as _orig_ollama_pt

def safe_ollama_pt(model, messages, **kwargs):
    # ensure msg_i is within bounds and has tool_calls
    for msg in messages:
        msg.setdefault("tool_calls", [])
    return _orig_ollama_pt(model=model, messages=messages, **kwargs)

litellm.llms.ollama.completion.transformation.ollama_pt = safe_ollama_pt