import argparse
import json
from typing import Optional, Union

from openai import OpenAI


def execute_prompt(client: OpenAI,
                   prompt: str,
                   system: Union[list[str], str],
                   model: str,
                   temperature: float,
                   feedback: Optional[list[tuple[str, str]]] = None) -> str:
    # System messages.
    messages = []
    if isinstance(system, list):
        for s in system:
            messages.append({"role": "system", "content": s})
    else:
        messages.append({"role": "system", "content": system})

    # Prompt.
    messages.append({"role": "user", "content": prompt})

    # Feedback messages.
    if feedback is None:
        feedback = []
    for f in feedback:
        messages.append({"role": "assistant", "content": f[0]})
        messages.append({"role": "user", "content": f[1]})

    completion = client.chat.completions.create(messages=messages,
                                                model=model,
                                                temperature=temperature)

    assert len(completion.choices) == 1
    return completion.choices[0].message.content


def main(args: argparse.Namespace):
    system = args.system
    model = args.model
    temperature = args.temperature

    # Load system from file.
    with open(system, "r") as fp:
        system = json.load(fp)
    system = system["system"]

    # Create the OpenAI client.
    client = OpenAI()

    # Perform the prompting.
    while True:
        prompt = input("\033[0;31mPrompt: \033[0m").strip()
        if not prompt:
            break

        response = execute_prompt(client, prompt, system, model, temperature)
        print(response)

        feedback = []
        while True:
            f = input("\033[0;31mFeedback: \033[0m")
            if not f:
                break

            feedback.append((response, f))
            response = execute_prompt(client, prompt, system, model,
                                      temperature, feedback)
            print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform prompt code generation with an LLM.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "system",
        type=str,
        help="Path to JSON containing the system {\"system\": ..., ...}")
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
    args = parser.parse_args()
    main(args)
