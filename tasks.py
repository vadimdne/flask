TASKS = [
    {
        "owner": "vadim",
        "title": "To complete python backend",
        "date": "15-10-2014",
        "isopen": "True",
    },
    {
        "owner": "vadim",
        "title": "Implement HTML markup",
        "date": "13-10-2014",
        "isopen": "True",
    },
    {
        "owner": "vadim",
        "title": "Connect to Postgre Database",
        "date": "14-10-2014",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Teach python course",
        "date": "15-10-2014",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Plant a tree",
        "date": "13-10-2014",
        "isopen": "True",
    },
    {
        "owner": "roman",
        "title": "Build a house",
        "date": "14-10-2014",
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

