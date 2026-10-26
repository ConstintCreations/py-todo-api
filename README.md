# RP3 Todo API

This is a simple Todo API made in Python for week 3 of [Resolution's](https://resolution.hackclub.com/) Python Pathway

![Todo API Image](/images/RP3_Todo_API_Image.png)

# Usage

The package is on [TestPyPi](https://test.pypi.org/project/Constint_RP3_Todo_API/)

To install, you can use
```
pip install -i https://test.pypi.org/simple/ Constint_RP3_Todo_API
```

Run with: `todo-api`

# Documentation

## List Tasks (GET /tasks)

Tasks can be listed with "/tasks" and optionally take in a done parameter to show only done tasks or only not done tasks

## Add Tasks (POST /tasks)

Tasks can be added with "/tasks" and take a request body of 

```
{
    "task": "string"
}
```
where "string" is the name of your new task

## Complete Tasks (PATCH /tasks/{task_id}/complete)

Tasks can be completed with "/tasks/{task_id}/complete" where task_id is the integer id at which the task you want to mark as complete is

## Clear Tasks (DELETE /tasks/clear)

Tasks can be cleared (Delete all tasks) with "/tasks/cleared" and optionally take in a done parameter to clear only done tasks or only not done tasks

## Delete Tasks (DELETE /tasks/{task_id})


Tasks can be deleted with "/tasks/{task_id}" where task_id is the integer id at which the task you want to delete is

## Search Tasks (GET /tasks/search)

Tasks can be searched for by task name with "/tasks/seach" and take a request body of 

```
{
    "query": "string"
}
```
where "string" is the actual query for your search
