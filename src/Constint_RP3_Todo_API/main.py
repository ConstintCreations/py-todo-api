from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

app = FastAPI()

TASKS_FILE = "tasks.json"

class TaskBody(BaseModel):
    task: str

class Query(BaseModel):
    query_text: str

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@app.get("/tasks")
async def get_tasks(done: bool | None = None):
    tasks = load_tasks()
    if done != None:
        if done:
            done_tasks = []
            for task in tasks:
                if task["done"] == True:
                    done_tasks.append(task)
            return done_tasks
        else:
            not_done_tasks = []
            for task in tasks:
                if task["done"] == False:
                    not_done_tasks.append(task)
            return not_done_tasks
    return tasks

@app.post("/tasks")
async def add_task(task_body: TaskBody):
    tasks = load_tasks()
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    tasks.append({"id": new_id, "task": task_body.task, "done": False})
    save_tasks(tasks)
    return tasks[-1]

@app.patch("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if (task["id"] == task_id):
            task["done"] = True
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/clear")
async def clear_tasks(done: bool | None = None):
    new_tasks = []
    if done != None:
        tasks = load_tasks()
        if done:
            for task in tasks:
                if task["done"] == False:
                    new_tasks.append(task)
        else:
            for task in tasks:
                if task["done"] == True:
                    new_tasks.append(task)

    save_tasks(new_tasks)
    return new_tasks

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if (task["id"] == task_id):
            tasks.remove(task)
            save_tasks(tasks)
            return f"Task at id {task_id} was deleted"
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks/search")
async def search_tasks(query: Query):
    tasks = load_tasks()
    found_tasks = []
    for task in tasks:
        if query.query_text.lower() in task["task"].lower():
            found_tasks.append(task)
    if len(found_tasks) > 0:
        return found_tasks
    raise HTTPException(status_code=404, detail="No matching tasks found")

def main():
    import uvicorn
    uvicorn.run("Constint_RP3_Todo_API.main:app", host="127.0.0.1", port="8000")

if __name__ == "__main__":
    main()