const API_BASE = 'http://127.0.0.1:8000/api/notes';

document.addEventListener('DOMContentLoaded', () => {
    fetchNotes();

    const form = document.getElementById('note-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('note-title').value;
        const content = document.getElementById('note-content').value;

        if (!title || !content) return;

        await createNote({ title, content });
        form.reset();
        fetchNotes();
    });

    // Modal Events
    document.getElementById('cancel-edit').addEventListener('click', closeEditModal);
    document.getElementById('edit-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const id = document.getElementById('edit-note-id').value;
        const title = document.getElementById('edit-note-title').value;
        const content = document.getElementById('edit-note-content').value;

        await updateNote(id, { title, content });
        closeEditModal();
        fetchNotes();
    });
});

async function fetchNotes() {
    try {
        const response = await fetch(API_BASE);
        const notes = await response.json();
        renderNotes(notes);
    } catch (error) {
        console.error('Error fetching notes:', error);
    }
}

async function createNote(note) {
    try {
        await fetch(API_BASE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(note)
        });
    } catch (error) {
        console.error('Error creating note:', error);
    }
}

async function updateNote(id, note) {
    try {
        await fetch(`${API_BASE}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(note)
        });
    } catch (error) {
        console.error('Error updating note:', error);
    }
}

async function deleteNote(id) {
    if (!confirm('Are you sure you want to delete this note?')) return;
    try {
        await fetch(`${API_BASE}/${id}`, {
            method: 'DELETE'
        });
        fetchNotes();
    } catch (error) {
        console.error('Error deleting note:', error);
    }
}

function renderNotes(notes) {
    const grid = document.getElementById('notes-grid');
    grid.innerHTML = '';
    
    // Sort descending by updated_at
    notes.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at));

    if (notes.length === 0) {
        grid.innerHTML = `<p style="text-align:center; grid-column: 1 / -1; color: var(--text-light);">No notes yet. Start writing! ✨</p>`;
        return;
    }

    notes.forEach(note => {
        const card = document.createElement('div');
        card.className = 'note-card';

        const formattedDate = new Date(note.updated_at).toLocaleDateString('en-US', {
            year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
        });

        // Escaping strings for onclick attribute
        const escapedTitle = escapeHTML(note.title).replace(/'/g, "\\'").replace(/"/g, "&quot;");
        const escapedContent = escapeHTML(note.content).replace(/'/g, "\\'").replace(/"/g, "&quot;");

        card.innerHTML = `
            <div>
                <h3>${escapeHTML(note.title)}</h3>
                <div class="note-meta">Last updated: ${formattedDate}</div>
                <p>${escapeHTML(note.content)}</p>
            </div>
            <div class="note-actions">
                <button class="btn-icon edit" onclick="openEditModal(${note.id}, '${escapedTitle}', '${escapedContent}')">
                    ✏️
                </button>
                <button class="btn-icon delete" onclick="deleteNote(${note.id})">
                    🗑️
                </button>
            </div>
        `;
        grid.appendChild(card);
    });
}

function openEditModal(id, title, content) {
    // Unescape the HTML entities for display in input fields
    const unescapeHTML = (str) => {
        const txt = document.createElement('textarea');
        txt.innerHTML = str;
        return txt.value;
    };

    document.getElementById('edit-note-id').value = id;
    document.getElementById('edit-note-title').value = unescapeHTML(title);
    document.getElementById('edit-note-content').value = unescapeHTML(content);
    document.getElementById('edit-modal').classList.remove('hidden');
}

function closeEditModal() {
    document.getElementById('edit-modal').classList.add('hidden');
    document.getElementById('edit-form').reset();
}

function escapeHTML(str) {
    if (!str) return '';
    return str.replace(/[&<>'"]/g, 
        tag => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        }[tag] || tag)
    );
}
