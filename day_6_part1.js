//this solves both, just changed numbers
let time = [44899691]
let dist = [277113618901768]

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