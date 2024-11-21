import openai
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def debug_code(code_snippet):
    prompt = f"Debug the following code and provide fixes:\n\n{code_snippet}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def format_code(code):
    return highlight(code, PythonLexer(), HtmlFormatter())
