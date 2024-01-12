const students = document.querySelectorAll('.student')
const tables = document.querySelectorAll('.group')

students.forEach(student => {

    student.addEventListener('dragstart', () => {
        student.classList.add('dragging')
        // student.parentNode.removeChild(student)
    })

    student.addEventListener('dragend', () => { // for opacity while dragging
        // console.log('end')
        student.classList.remove('dragging')
    })
})

tables.forEach(table => {
    table.addEventListener('dragover', e => {
        e.preventDefault()
        // const desk = chooseDesk(table, e.clientY)
        // console.log(desk)
        const e_idx = find_desk_idx(table, e)
        // console.log(e_idx)
        const desk_idx = chooseDesk(table, e.clientX, e.clientY)
        console.log(desk_idx)
        // console.log(table.children[0].querySelector('img').src)
        // console.log(table.children[desk_idx].nextElementSibling.querySelector('img').src)
        const desk = table.children[desk_idx]
        // console.log(desk)
        const currStudent = document.querySelector('.dragging')
        // if(desk == null){
        //     console.log('insert end')
        //     // currStudent.parentNode.removeChild(currStudent)
        //     table.appendChild(currStudent)
        // } else {
        //     console.log('insert before')
        //     // currStudent.parentNode.removeChild(currStudent)
        //     // const temp = currStudent.nextSibling
        //     // console.log(currStudent)
        //     // console.log(temp)
        //     // console.log(desk)
        //     // console.log(temp.querySelector('img').src)
        //     table.insertBefore(currStudent, desk)
        //     // table.insertBefore(desk, temp)
        // }
        var replacing_desk_prev = -1
        var replacing_desk_next = -1
        if(desk_idx != 0){
            replacing_desk_prev = table.children[desk_idx].previousElementSibling
        }
        if(desk_idx != table.childElementCount - 1){
            replacing_desk_next = table.children[desk_idx].nextElementSibling
        }
        if(desk_idx == 0 && replacing_desk_prev != -1){
            console.log('before 0')
            table.children[0] = currStudent
            table.children[1] = replacing_desk_prev
            table.children[2] = replacing_desk_next
            table.children[3] = replacing_desk_next.nextElementSibling.nextElementSibling
            // table.insertBefore(currStudent, table.children[0])
        } else if(desk_idx == 1){
            console.log('before 1')
            table.children[0] = replacing_desk_prev
            table.children[1] = currStudent
            table.children[2] = replacing_desk_next
            table.children[3] = replacing_desk_next.nextElementSibling
            // table.insertBefore(currStudent, table.children[1])
        } else if(desk_idx == 2){
            console.log('before 2')
            table.children[0] = replacing_desk_prev.previousElementSibling
            table.children[1] = replacing_desk_prev
            table.children[2] = currStudent
            table.children[3] = replacing_desk_next
            // table.insertBefore(currStudent, table.children[2])
        } else if(desk_idx == 3){
            console.log('before 3')
            table.children[0] = replacing_desk_prev.previousElementSibling.previousElementSibling
            table.children[1] = replacing_desk_prev.previousElementSibling
            table.children[2] = replacing_desk_prev
            table.children[3] = currStudent
            // table.insertBefore(currStudent, table.children[3])
        } 
        // else {
        //     console.log('at end')
        //     table.appendChild(currStudent)
        // }
    })
})

function chooseDesk(table, x, y){
    const desks = [...table.querySelectorAll('.student')]; 
    // const desks = [...table.querySelectorAll('.student:not(.dragging)')]; 

    // if(x > desks[0].getBoundingClientRect().right && y > desks[0].getBoundingClientRect().bottom){
    //     return null
    // }
    const box = table.getBoundingClientRect()
    // console.log(box)
    const left_bound = box.left
    const right_bound = box.right
    const middle_x = box.left + box.width/2
    const middle_y = box.top + box.height/2
    if(x < middle_x && y < middle_y){ // desk 0
        return 0
    } else if(x > middle_x && y < middle_y){ // desk 1
        return 1
    } else if(x < middle_x && y > middle_y){ // desk 2
        return 2
    } else if(x > middle_x && y > middle_y){ // desk 3
        return 3
    }
    return null

    // const distances = []
    // desks.forEach(desk => {
    //     // console.log(desk.querySelector('img').src)
    //     // console.log(desk.getBoundingClientRect())
    //     const desk_center_x = desk.getBoundingClientRect().left + desk.getBoundingClientRect().width/2
    //     const desk_center_y = desk.getBoundingClientRect().top + desk.getBoundingClientRect().height/2
    //     const x_offset = x - desk_center_x
    //     const y_offset = y - desk_center_y
    //     const distance = Math.sqrt(x_offset ** 2 + y_offset ** 2)
    //     distances.push(distance)
    // })
    // // console.log(distances)
    // var closest_desk_idx = 0
    // // console.log(distances.length)
    // for(var i = 1; i < distances.length; ++i){
    //     if(distances[i] < distances[closest_desk_idx]){
    //         closest_desk_idx = i
    //     }
    // }
    // // console.log(table.children)
    // console.log('closest_desk_idx:' + closest_desk_idx)
    // // return table.children[closest_desk_idx]
    // return closest_desk_idx
}

function find_desk_idx(table, e){
    for(var i = 0; i < table.childElementCount; ++i){
        if(table.children[i].querySelector('img') === e.target){
            // console.log('i: ' + i)
            return i;
        }
    }
}