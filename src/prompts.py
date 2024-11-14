import argparse
import json

from openai import OpenAI

def prompt(client: OpenAI, prompt: dict, system: str, model: str, temperature: float,
             responses: int) -> list[dict]:
    completion = client.chat.completions.create(messages=[{
        "role":
        "system",
        "content":
        system
    }, {
        "role":
        "user",
        "content":
        prompt["content"]
    }],
                                                model=model,
                                                temperature=temperature,
                                                n=responses)

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
    responses = args.responses
    output = args.output

    # Load prompts from file.
    with open(prompts, "r") as fp:
        prompts = json.load(fp)
    system = prompts["system"]
    prompts = prompts["prompts"]

    # Create the OpenAI client.
    client = OpenAI()

    # Perform the prompting.
    results = []
    for prompt in prompts:
        result = prompt(client, prompt, system, model, temperature, responses)
        results.extend(result)

    # Write to the output file.
    with open(output, "w") as fp:
        json.dump(results, fp, indent=4)
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
    parser.add_argument(
        "-r",
        "--responses",
        type=int,
        default=1,
        help="Number of responses to generate for each prompt.")
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        default="prompts_output.json",
                        help="The path to the output file.")
    args = parser.parse_args()
    main(args)
