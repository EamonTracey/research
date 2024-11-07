import argparse
import json

from openai import OpenAI

CODING_SYSTEM = "You are a helpful TaskVine coding assistant. Provide strictly the requested code using the ndcctools.taskvine library."


def zeroshot(client: OpenAI, prompt: dict, model: str,
             responses: int) -> list[dict]:
    completion = client.chat.completions.create(messages=[{
        "role":
        "system",
        "content":
        CODING_SYSTEM
    }, {
        "role":
        "user",
        "content":
        prompt["content"]
    }],
                                                model=model,
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
    responses = args.responses
    output = args.output

    # Load prompts from file.
    with open(prompts, "r") as fp:
        prompts = json.load(fp)

    # Create the OpenAI client.
    client = OpenAI()

    # Perform the zeroshot prompting.
    results = []
    for prompt in prompts:
        result = zeroshot(client, prompt, model, responses)
        results.extend(result)

    # Write to the output file.
    with open(output, "w") as fp:
        json.dump(results, fp, indent=4)
        fp.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Perform zeroshot prompt code generation with an LLM.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "prompts",
        type=str,
        help=
        "Path to the JSON file containing a list of prompts {\"id\": ..., \"content\": ...}."
    )
    parser.add_argument("-m",
                        "--model",
                        type=str,
                        default="gpt-4o",
                        help="The LLM model to use.")
    parser.add_argument("-o",
                        "--output",
                        type=str,
                        default="zeroshot_prompts.json",
                        help="The path to the output file.")
    parser.add_argument(
        "-r",
        "--responses",
        type=int,
        default=1,
        help="Number of responses to generate for each prompt.")
    args = parser.parse_args()
    main(args)
