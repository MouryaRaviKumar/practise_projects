# To- do application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Task, TaskCreate, TaskUpdate, TaskResponse, TaskListResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = {}
task_id_counter = 0

@app.get("/")
def health_check():
    return {"message": "To-do application is running!"}

@app.get("/tasks")
def get_tasks():
    task_responses = [TaskResponse(**task.dict()) for task in tasks.values()]
    return TaskListResponse(tasks=task_responses)

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    if task_id not in tasks:
        return {"error": "Task not found!"}
    return TaskResponse(**tasks[task_id].dict())

@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_id_counter
    task_id_counter += 1
    new_task = Task(id=task_id_counter, **task.dict())
    tasks[task_id_counter] = new_task
    return TaskResponse(**new_task.dict())

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    if task_id not in tasks:
        return {"error": "Task not found!"}
    
    task = tasks[task_id]
    for field, value in updated_task.dict(exclude_unset=True).items():
        setattr(task, field, value)
    return TaskResponse(**task.dict())

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        return {"error": "Task not found!"}

    del tasks[task_id]
    return {"message": "Task deleted successfully!"}