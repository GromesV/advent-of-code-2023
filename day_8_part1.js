let mapa = ``

let steps = ''
steps = steps.split('')

let positions = steps.map(x => x == 'L' ? 0 : 1)
console.log(steps)
//treba da queue steps

mapa = mapa.split('\n')
let map = {}

mapa.forEach(element => {
    let explosion = element.replaceAll(' ', '').split('=')
    let coords = explosion[1].replace('(', '').replace(')', '').split(',')
    map[explosion[0]] = coords
});

//todo: mislim da je bolje ici od zzz unezad i izbrojati korake da aaa
//moguce je sto se vidi i iz primera da se nekako obrne 'kruzenje' i da 
//poslednji element umesto L postane R
//na taj nacin ovaj while ne mora da dodaje nizove

let nodesToTravel = []
for (let k in map) {
    if (k.at(-1) == 'A')
        nodesToTravel.push(k)
}


function getTotal(curNode) {
    let total = 0
    while (curNode.at(-1) != 'Z' && positions.length > 0) {
        total++
        let pos = positions.shift()
        curNode = map[curNode][pos]
        if (positions.length == 0) {
            positions = positions.concat(steps.map(x => x == 'L' ? 0 : 1))
        }
        console.log('run')
    }
    return total
}

let totals = []
nodesToTravel.forEach(element => {
    totals.push(getTotal(element))
});

// let res = totals.reduce((acc, cur) => acc * cur, 1)
console.log(totals)
//na taj total pustio: https://www.calculatorsoup.com/calculators/math/lcm.php
//ne znam kako to isprogramirati