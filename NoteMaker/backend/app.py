from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import createNote, updateNote, noteResponse, Note
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

notes = {}
note_id_counter = 0

@app.get("/api/notes")
def get_notes():
    return list(notes.values())

@app.post("/api/notes")
def create_notes(note: createNote):
    global note_id_counter
    note_id_counter += 1
    new_note = Note(id=note_id_counter, **note.dict())
    notes[note_id_counter] = new_note
    return noteResponse(**new_note.dict())

@app.get("/api/notes/{note_id}")
def get_note_by_id(note_id: int):
    if note_id not in notes:
        return {"error": "Note not found!"}
    return noteResponse(**notes[note_id].dict())

@app.put("/api/notes/{note_id}")
def update_note(note_id: int, updated_note: updateNote):
    if note_id not in notes:
        return {"error": "Note not found!"}
    
    note = notes[note_id]
    for field, value in updated_note.dict(exclude_unset=True).items():
        setattr(note, field, value)
    note.updated_at = datetime.utcnow()
    return noteResponse(**note.dict())

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        return {"error": "Note not found!"}

    del notes[note_id]
    return {"message": "Note deleted successfully!"}



