from openai import OpenAI

# API Key is pulled from 'OPENAI_API_KEY' environment variable
client = OpenAI()

def main():
    print("Type 'exit' to quit")
    flag = True
    while(flag):
        prompt = input("Enter a prompt: ")
        if prompt == "exit":
            flag = False
        else:
            query_openai(prompt)

def query_openai(prompt):
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    print(completion.choices[0].text)

if __name__ == "__main__":
    main()