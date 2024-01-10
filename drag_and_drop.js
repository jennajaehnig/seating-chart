const students = document.querySelectorAll('.student')
const tables = document.querySelectorAll('.group')

students.forEach(student => {

    student.addEventListener('dragstart', () => {
        student.classList.add('dragging')
    })

    student.addEventListener('dragend', () => { // for opacity while dragging
        student.classList.remove('dragging')
    })
})

tables.forEach(table => {
    table.addEventListener('dragover', e => {
        e.preventDefault()
        const desk = chooseDesk(table, e.clientX, e.clientY)
        const currStudent = document.querySelector('.dragging')
        if(desk == null){
            table.appendChild(currStudent)
        } else {
            table.insertBefore(currStudent, desk)
        }
    })
})

function chooseDesk(table, x, y) {
    const studentsAtGroup = [...table.querySelectorAll('.student:not(.dragging)')];

    return studentsAtGroup.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const x_offset = x - box.left - box.width / 2;
        const y_offset = y - box.top - box.height / 2;
        const distance = Math.sqrt(x_offset ** 2 + y_offset ** 2);
        console.log('distance: ' + distance)
        console.log('closest distance: ' + closest.distance)
        if (distance < closest.distance) {
            return { distance, element: child, x_offset, y_offset };
        } else {
            console.log('closest: ')
            console.log(closest)
            return closest;
        }
    }, { distance: Number.POSITIVE_INFINITY }).element;
}