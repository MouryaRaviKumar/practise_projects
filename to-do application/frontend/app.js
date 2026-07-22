const API_URL = 'http://127.0.0.1:8000';

document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();

    // Form submission
    document.getElementById('task-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const priority = document.getElementById('priority').value;

        await createTask({ title, description, priority });
        e.target.reset();
    });

    // Edit form submission
    document.getElementById('edit-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const id = document.getElementById('edit-id').value;
        const title = document.getElementById('edit-title').value;
        const description = document.getElementById('edit-description').value;
        const priority = document.getElementById('edit-priority').value;
        const status = document.getElementById('edit-status').value;

        await updateTask(id, { title, description, priority, status });
        closeModal();
    });
});

async function fetchTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const data = await response.json();
        renderTasks(data.tasks);
    } catch (error) {
        console.error('Error fetching tasks:', error);
        document.getElementById('task-list').innerHTML = '<div class="loading">Failed to load tasks. Make sure the backend is running.</div>';
    }
}

async function createTask(taskData) {
    try {
        await fetch(`${API_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(taskData),
        });
        fetchTasks();
    } catch (error) {
        console.error('Error creating task:', error);
    }
}

async function updateTask(id, taskData) {
    try {
        await fetch(`${API_URL}/tasks/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(taskData),
        });
        fetchTasks();
    } catch (error) {
        console.error('Error updating task:', error);
    }
}

async function deleteTask(id) {
    if (!confirm('Are you sure you want to delete this task?')) return;
    try {
        await fetch(`${API_URL}/tasks/${id}`, {
            method: 'DELETE',
        });
        fetchTasks();
    } catch (error) {
        console.error('Error deleting task:', error);
    }
}

async function toggleTaskStatus(id, currentStatus) {
    const newStatus = currentStatus === 'completed' ? 'pending' : 'completed';
    await updateTask(id, { status: newStatus });
}

window.openEditModal = function(id, title, description, priority, status) {
    document.getElementById('edit-id').value = id;
    document.getElementById('edit-title').value = title;
    document.getElementById('edit-description').value = description;
    document.getElementById('edit-priority').value = priority;
    document.getElementById('edit-status').value = status;
    
    const modal = document.getElementById('edit-modal');
    modal.classList.add('active');
}

window.closeModal = function() {
    const modal = document.getElementById('edit-modal');
    modal.classList.remove('active');
}

window.deleteTask = deleteTask;
window.toggleTaskStatus = toggleTaskStatus;

function renderTasks(tasks) {
    const taskList = document.getElementById('task-list');
    const taskCount = document.getElementById('task-count');
    
    taskCount.textContent = `${tasks.length} task${tasks.length !== 1 ? 's' : ''}`;
    
    if (tasks.length === 0) {
        taskList.innerHTML = '<div class="loading">No tasks found. Add one above!</div>';
        return;
    }

    taskList.innerHTML = '';
    
    tasks.sort((a, b) => b.id - a.id).forEach(task => {
        const isCompleted = task.status === 'completed';
        const card = document.createElement('div');
        card.className = `task-card priority-${task.priority} ${isCompleted ? 'completed' : ''}`;
        
        // Escape quotes for inline JS execution
        const escapedTitle = task.title.replace(/'/g, "\\'").replace(/"/g, '&quot;');
        const escapedDesc = task.description ? task.description.replace(/'/g, "\\'").replace(/"/g, '&quot;') : '';
        
        card.innerHTML = `
            <div class="task-header">
                <h3>${task.title}</h3>
                <div class="task-actions">
                    <button class="icon-btn complete" onclick="toggleTaskStatus(${task.id}, '${task.status}')" title="${isCompleted ? 'Mark Pending' : 'Mark Completed'}">
                        <i data-lucide="${isCompleted ? 'rotate-ccw' : 'check'}"></i>
                    </button>
                    <button class="icon-btn edit" onclick="openEditModal(${task.id}, '${escapedTitle}', '${escapedDesc}', '${task.priority}', '${task.status}')" title="Edit">
                        <i data-lucide="edit-2"></i>
                    </button>
                    <button class="icon-btn delete" onclick="deleteTask(${task.id})" title="Delete">
                        <i data-lucide="trash-2"></i>
                    </button>
                </div>
            </div>
            ${task.description ? `<p class="task-desc">${task.description}</p>` : ''}
            <div class="task-meta">
                <span class="badge">${task.priority} Priority</span>
                <span class="badge">${task.status}</span>
            </div>
        `;
        
        taskList.appendChild(card);
    });
    
    // Re-initialize lucide icons for newly added elements
    if (window.lucide) {
        lucide.createIcons();
    }
}
