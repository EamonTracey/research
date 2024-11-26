import argparse
import json
from typing import Union

from openai import OpenAI


def execute_prompt(client: OpenAI, prompt: dict, system: Union[list[str], str],
                   model: str, temperature: float) -> list[dict]:
    messages = []
    if isinstance(system, list):
        for s in system:
            messages.append({"role": "system", "content": s})
    else:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt["content"]})
    completion = client.chat.completions.create(messages=messages,
                                                model=model,
                                                temperature=temperature)

    results = []
    for choice in completion.choices:
        result = prompt
        result["response"] = choice.message.content
        results.append(result)

    return results


def main(args: argparse.Namespace):
    prompts = args.prompts
    model = args.model
    temperature = args.temperature
    output = args.output

    # Load prompts from file.
    with open(prompts, "r") as fp:
        prompts = json.load(fp)
    system = prompts["system"]
    prompts = prompts["prompts"]

    # Create the OpenAI client.
    client = OpenAI()

    # Perform the prompting.
    result = {"system": system, "prompts": []}
    for prompt in prompts:
        prompt = execute_prompt(client, prompt, system, model, temperature)
        result["prompts"].extend(prompt)

    # Write to the output file.
    with open(output, "w") as fp:
        json.dump(result, fp, indent=4)
        fp.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform prompt code generation with an LLM.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "prompts",
        type=str,
        help=
        "Path to the JSON file containing the system and a list of prompts {\"system\": ..., \"prompts\": [{\"id\": ..., \"content\": ...}, ...]}."
    )
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default="gpt-4o",
                        help="The LLM model to use.")
    parser.add_argument(
        "-t",
        "--temperature",
        type=float,
        default=0,
        help="The temperature with which to generate responses (0-1).")
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        default="prompts_output.json",
                        help="The path to the output file.")
    args = parser.parse_args()
    main(args)
