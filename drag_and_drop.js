const students = document.querySelectorAll('.student')
const tables = document.querySelectorAll('.group')

students.forEach(student => {

    student.addEventListener('dragstart', () => {
        student.classList.add('dragging')
    })

    student.addEventListener('dragend', () => { // for opacity while dragging
        console.log('end')
        student.classList.remove('dragging')
    })
})

tables.forEach(table => {
    table.addEventListener('dragover', e => {
        e.preventDefault()
        // const desk = chooseDesk(table, e.clientY)
        // console.log(desk)
        const desk = chooseDesk(table, e.clientX, e.clientY)
        // console.log(desk)
        const currStudent = document.querySelector('.dragging')
        if(desk == null){
            console.log('insert end')
            // currStudent.parentNode.removeChild(currStudent)
            table.appendChild(currStudent)
        } else {
            console.log('insert before')
            // currStudent.parentNode.removeChild(currStudent)
            const temp = currStudent.nextSibling
            // console.log(temp.querySelector('img').src)
            table.insertBefore(currStudent, desk)
            table.insertBefore(desk, temp)
        }
    })
})

function chooseDesk(table, x, y){
    const desks = [...table.querySelectorAll('.student')]; 

    // if(x > desks[0].getBoundingClientRect().right && y > desks[0].getBoundingClientRect().bottom){
    //     return null
    // }

    const distances = []
    desks.forEach(desk => {
        // console.log(desk.querySelector('img').src)
        // console.log(desk.getBoundingClientRect())
        const desk_center_x = desk.getBoundingClientRect().left + desk.getBoundingClientRect().width/2
        const desk_center_y = desk.getBoundingClientRect().top + desk.getBoundingClientRect().height/2
        const x_offset = x - desk_center_x
        const y_offset = y - desk_center_y
        const distance = Math.sqrt(x_offset ** 2 + y_offset ** 2)
        distances.push(distance)
    })
    // console.log(distances)
    var closest_desk_idx = 0
    // console.log(distances.length)
    for(var i = 1; i < distances.length; ++i){
        if(distances[i] < distances[closest_desk_idx]){
            closest_desk_idx = i
        }
    }
    console.log(table.children)
    console.log(closest_desk_idx)
    return table.children[closest_desk_idx]
}