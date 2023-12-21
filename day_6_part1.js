let time = [44, 89, 96, 91]
let dist = [277, 1136, 1890, 1768]

let nos = []
for (let tt in time) {
    t = time[tt]
    no = 0
    record = dist[tt]
    for (let i = 1; i < t + 1; i++) {
        let remain = t - i
        let res = i * remain
        if (res > record)
            no++
    }
    nos.push(no)
}
console.log(nos)

let total = nos.reduce((p, c) => p * c, 1)
console.log(total)