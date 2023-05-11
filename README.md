# LLM Cost Estimator

Simple tool to estimate costs for batch text generation with LLMs.

Currently OpenAI LLMs are supported. PRs welcome to add support for other providers.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed
- The `tiktoken` library installed (`pip install tiktoken`)

## Installation

1. Clone and install this repository:

```bash
git clone https://github.com/g-simmons/llm-cost-estimator.git
cd llm-cost-estimator
pip install -e .
```

## Usage

1. Import the necessary modules:

```python
from llm_cost_estimator import estimate_costs
```

2. Use the `estimate_costs` function to estimate the cost:

The function takes the following parameters:

- `texts` (List[str]): A list of text prompts.
- `model` (str): The model name, e.g., "text-davinci-003".
- `max_tokens` (int): The maximum number of tokens to generate.
- `wait` (bool): If `True`, the program will wait for user input before proceeding. Default is `True`.
- `tokenization_method` (str): The tokenization method to use, either "tiktoken" or "simple". Default is "tiktoken".

The function returns the estimated cost in dollars.

## Example Usage

```python
texts = [
    "This is the first prompt.",
    "This is the second prompt.",
    "This is the third prompt."
]
model = "text-davinci-003"
max_tokens = 100

cost = estimate_costs(texts, model, max_tokens, wait=False)
print(f"Estimated cost: ${cost}")
```

This example estimates the cost of running the "text-davinci-003" model on the given list of texts, generating a maximum of 100 tokens. The estimated cost is then printed.


## Wait for user input before proceeding

Note: The `wait` parameter allows the program to wait for user confirmation before proceeding. If you want the program to continue without waiting, set `wait=False` when calling the function.

```python
texts = [
    "This is the first prompt.",
    "This is the second prompt.",
    "This is the third prompt."
]
model = "text-davinci-003"
max_tokens = 100

cost = estimate_costs(texts, model, max_tokens, wait=True)

print(f"Generating ...")
```

Output:
```
Estimated costs: $0.01 y/n
n
```

```
Estimated costs: $0.01 y/n
y
Generating...
```
