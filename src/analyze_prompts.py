import argparse
import json


def analyze(prompt: dict):
    print(prompt["response"])


def main(args: argparse.Namespace):
    prompts = args.prompts

    # Load prompts from file.
    with open(prompts, "r") as fp:
        prompts = json.load(fp)

    # Perform the zeroshot prompting.
    for prompt in prompts:
        analyze(prompt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze code generated by an LLM.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "prompts",
        type=str,
        help=
        "Path to the JSON file containing a list of prompts {\"id\": ..., \"content\": ..., \"response: ...\"}."
    )
    args = parser.parse_args()
    main(args)
