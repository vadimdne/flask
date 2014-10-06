TASKS = [
    {
        "owner": "vadim",
        "title": "To complete python backend",
        "isopen": "True",
    },
    {
        "owner": "vadim",
        "title": "Implement HTML markup",
        "isopen": "True",
    },
    {
        "owner": "vadim",
        "title": "Connect to Postgre Database",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Teach python course",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Plant a tree",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Build a house",
        "isopen": "True",
    },
]

if __name__ == "__main__":
    response = ""
    for task in TASKS:
        if task["owner"] == "vadim":
        #    print task
            response = response + task["title"] + '\n'
    print response

