const students = document.querySelectorAll('.student')
const tables = document.querySelectorAll('.group')
var curr_desk_idx = 0

students.forEach(student => {

    student.addEventListener('dragstart', e => {
        student.classList.add('dragging')
        curr_desk_idx = chooseDesk(student.parentNode, e.clientX, e.clientY)
    })

    student.addEventListener('dragend', () => { // for opacity while dragging
        student.classList.remove('dragging')
    })
})

tables.forEach(table => {
    table.addEventListener('dragover', e => {
        e.preventDefault()
        const desk_idx = chooseDesk(table, e.clientX, e.clientY)
        const desk = table.children[desk_idx]
        const currStudent = document.querySelector('.dragging')
        if(curr_desk_idx < desk_idx){
            desk.insertAdjacentElement("afterend", currStudent)
        } else if(curr_desk_idx > desk_idx){
            desk.insertAdjacentElement("beforebegin", currStudent)
        }
        curr_desk_idx = desk_idx
    })
})

function chooseDesk(table, x, y){
    const desks = [...table.querySelectorAll('.student')]; 

    const distances = []
    desks.forEach(desk => {
        const desk_center_x = desk.getBoundingClientRect().left + desk.getBoundingClientRect().width/2
        const desk_center_y = desk.getBoundingClientRect().top + desk.getBoundingClientRect().height/2
        const x_offset = x - desk_center_x
        const y_offset = y - desk_center_y
        const distance = Math.sqrt(x_offset ** 2 + y_offset ** 2)
        distances.push(distance)
    })
    var closest_desk_idx = 0
    for(var i = 1; i < distances.length; ++i){
        if(distances[i] < distances[closest_desk_idx]){
            closest_desk_idx = i
        }
    }
    return closest_desk_idx
}