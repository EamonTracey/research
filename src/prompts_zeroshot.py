import argparse
import json

from openai import OpenAI


def main(args: argparse.Namespace):
    prompts = args.prompts
    model = args.model
    n_responses = args.n_responses

    # Load prompts from file.
    with open(prompts, "r") as fp:
        prompts = json.load(fp)

    # Create the OpenAI client.
    client = OpenAI()
    
    for prompt in prompts:
        q=client.chat.completions.create(messages=[{"role": "user", "content": prompt["prompt"]}], model=model)
        print(q.choices[0].message.content)
        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform zeroshot prompt code generation with an LLM.")
    parser.add_argument("prompts", type=str, help="Path to the JSON file containing a list of prompts {\"id\": ..., \"prompt\": ...}.")
    parser.add_argument("-m", "--model", type=str, default="gpt-4o-mini")
    parser.add_argument("-n", "--n_responses", type=int, default=1, help="Number of responses to generate for each prompt.")
    args = parser.parse_args()
    main(args)
