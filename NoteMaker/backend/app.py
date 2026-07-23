from fastapi import FastAPI

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

