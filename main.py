from openai import OpenAI

# API Key is pulled from 'OPENAI_API_KEY' environment variable
client = OpenAI()

def main():
    chatType = input("Enter 'prompt' or 'roles': ")
    flag = True
    print("Type 'exit' to quit")
    if chatType == 'prompt':
        while(flag):
            prompt = input("Enter a prompt: ")
            if prompt == "exit":
                flag = False
            else:
                query_openai(prompt)
                print("\n")
    elif chatType == 'roles':
        while(flag):
            role = input("Enter a role for the chat bot: ")
            if role == "exit":
                flag = False
            else:
                prompt = input("Enter a prompt: ")
                if prompt == "exit":
                    flag = False
                else:
                    print("\n")
                    query_openai_roles(role,prompt)
                    print("\n")

def query_openai(prompt):
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    print(completion.choices[0].text)

def query_openai_roles(systemRole, prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": systemRole},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()