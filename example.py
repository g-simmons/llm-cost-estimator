from llm_cost_estimator import estimate_costs

texts = [
    "This is the first prompt.",
    "This is the second prompt.",
    "This is the third prompt."
]
model = "text-davinci-003"
max_tokens = 100

cost = estimate_costs(texts, model, max_tokens, wait=True)

print("Generating...")