document.addEventListener('DOMContentLoaded', function() {
    // Seletor do ícone e das tarefas
    const icon = document.getElementById('icon');
    const tasks = document.querySelectorAll('.tarefa');

    // Manipulador do evento de clique no ícone
    icon.addEventListener('click', function() {
        // Alterna a visibilidade das tarefas
        tasks.forEach(function(task) {
            task.style.display = task.style.display === 'none' ? 'block' : 'none';
        });
    });
});

