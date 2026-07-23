from fastapi import FastAPI
from models import createNote, updateNote, noteResponse
app = FastAPI()

notes = []
note_id_counter = 0

@app.get("/api/notes")
def get_notes():
    return notes

@app.post("/api/notes")
def create_notes(note: createNote):
    global note_id_counter
    note_id_counter += 1
    new_note = note(id=note_id_counter, **note.dict())
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
    return noteResponse(**note.dict())

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        return {"error": "Note not found!"}

    del notes[note_id]
    return {"message": "Note deleted successfully!"}



