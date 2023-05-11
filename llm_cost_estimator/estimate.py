from typing import List
import tiktoken

# costs in dollars
MODEL_RATES_PER_TOKEN = {
    "text-davinci-003": 0.02 / 1000,  
    "text-davinci-002": 0.02 / 1000,  
    "text-davinci-001": 0.02 / 1000,  
    "gpt-3.5-turbo": 0.002 / 1000,
    "text-curie-001": 0.002 / 1000,  
    "text-babbage-001": 0.0005 / 1000,  
    "text-ada-001": 0.0004 / 1000,  
}

WORD_TOKEN_RATIO = 0.75 # 1000 tokens is approx 750 words

MODEL_RATES_PER_WORD = {
    k: v * WORD_TOKEN_RATIO for k, v in MODEL_RATES_PER_TOKEN.items()
}


def estimate_gpt_costs(
    texts: List[str],
    model: str,
    max_tokens: int,
    wait=True,
    tokenization_method="tiktoken"
) -> float:
    """
    Estimate cost in dollars of running a gpt3 model on a list of texts. Assumes max_tokens generated tokens plus the prompt length.

    Args:
        texts: list of text prompts
        model: model name, e.g. "text-davinci-003"
        max_tokens: max tokens to generate
        wait: if True, wait for user input to proceed
        tokenization_method: "tiktoken" or "simple"
    
    Returns:
        cost in dollars
    """


    if tokenization_method == "simple":
        if model not in MODEL_RATES_PER_TOKEN:
            if wait:
                print(f"No rate data, cannot calculate a cost. Generate anyway? y/n")
                if not input() == "y":
                    quit()

        num_words = sum([len(text.split()) + (max_tokens / 0.75) for text in texts])

        cost = num_words * MODEL_RATES_PER_WORD[model]
        cost = round(cost, 2)


    else:
        enc = tiktoken.encoding_for_model(model)
        num_tokens = sum([len(enc.encode(text)) + (max_tokens) for text in texts])

        cost = num_tokens * MODEL_RATES_PER_TOKEN[model]
        cost = round(cost, 2)

    if wait:
        print(f"Estimated costs: ${cost} y/n")
        if not input() == "y":
            quit()

    return cost