let input = ``

input = input.split('\n')
input = input.map(x => x.split(' ').map(y => parseInt(y)))



let total = 0
for (let vals of input) {
    let stack = [vals]
    while (!stack.at(-1).every(x => x == 0)) {
        let differences = []
        for (let i = 0; i < stack.at(-1).length; i++) {
            const cur = stack.at(-1)[i];
            if (i > 0)
                differences.push(cur - stack.at(-1)[i - 1])
        }
        stack.push(differences)
    }
    let curVal = 0
    console.log("==================================================")
    for (let i = stack.length - 2; i >= 0; i--) {
        const st = stack[i];
        curVal = st[0] - curVal

    }
    total += curVal
}
console.log(total)



