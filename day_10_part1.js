let pipes = {
    "|": ["n", "s"],
    "-": ["e", "w"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    ".": null,
    "S": [],
}


/*
nadjem start
nodjem 4 tacke oko starta clockwise [gore,desno,dole,levo]
to su 4 nova starta, to ide u queue
svaki od tih elemenata mora da ima konekciju
while ima connect trazim dalje
ako nema, break
na kraju imam loop
mozda je dobro za svaki element/simbol da imam i koordinate
na kraju racunam poziciju elementa od starta prema pocetku
startna 4 elementa drzati u objektu
a elementi koji cine loop idu u niz


osim f-je hasConn treba i da znam da li je polje vec potroseno
polje ima
type
consumed
coords
connections (na osnovu pipe-a)
f-ju hasConnectinion

i onda dok god imamo konekciju pushujem na niz

*/

let input = `..F7.
.FJ|.
SJ.L7
|F--J
LJ...`

input = input.split("\n")
input = input.map(x => x.split(""))
console.table(input)



function getConnection(element, coords, input, pipes) {
    let width = input[0].length
    let height = input.length
    let north = coords.x > 0 ? input[coords.x - 1][coords.y] : null
    let east = coords.y < width - 1 ? input[coords.x][coords.y + 1] : null
    let south = coords.x < height - 1 ? input[coords.x + 1][coords.y] : null
    let west = coords.y > 0 ? input[coords.x][coords.y - 1] : null

    let connections = []

    if (pipes[element] == undefined) {
        throw new Error(`wtf ${element}`)
    }


    if (north && north != '.' && pipes[element].includes('n') && pipes[north].includes('s'))
        connections.push({ x: coords.x - 1, y: coords.y })
    if (east && east != '.' && pipes[element].includes('e') && pipes[east].includes('w'))
        connections.push({ x: coords.x, y: coords.y + 1 })
    if (south && south != '.' && pipes[element].includes('s') && pipes[south].includes('n'))
        connections.push({ x: coords.x + 1, y: coords.y })
    if (west && west != '.' && pipes[element].includes('w') && pipes[west].includes('e'))
        connections.push({ x: coords.x, y: coords.y - 1 })

    return connections
}

function getFirstFour(coords, input,) {
    let width = input[0].length
    let height = input.length
    let north = coords.x > 0 ? input[coords.x - 1][coords.y] : null
    let east = coords.y < width - 1 ? input[coords.x][coords.y + 1] : null
    let south = coords.x < height - 1 ? input[coords.x + 1][coords.y] : null
    let west = coords.y > 0 ? input[coords.x][coords.y - 1] : null
    let tmp = []
    if (north)
        tmp.push({ x: coords.x - 1, y: coords.y, symbol: north })
    if (east)
        tmp.push({ x: coords.x, y: coords.y + 1, symbol: east })
    if (south)
        tmp.push({ x: coords.x + 1, y: coords.y, symbol: south })
    if (west)
        tmp.push({ x: coords.x, y: coords.y - 1, symbol: west })
    return tmp
}


let startingFour
let consumed = {}
let walked = {}

for (let i = 0; i < input.length; i++) {
    const row = input[i];
    for (let j = 0; j < row.length; j++) {
        const element = row[j];
        let coords = { x: i, y: j }
        if (element == 'S')
            startingFour = getFirstFour(coords, input)
        if (!consumed[i])
            consumed[i] = {}
        consumed[i][j] = false
    }
}

console.log(JSON.stringify(startingFour))

for (let s = 0; s < startingFour.length; s++) {
    const startPoint = startingFour[s];
    walked[startPoint.symbol] = []

    consumed[startPoint.x][startPoint.y] = true

    let coords = { x: startPoint.x, y: startPoint.y }
    //this is dumb, should attach it to coords obj
    let symbol = startPoint.symbol

    let connections
    let hasContinue = true

    console.log(coords.x, coords.y, symbol)
    while (hasContinue && symbol != '.') {
        hasContinue = false
        connections = getConnection(symbol, coords, input, pipes)
        for (let conn of connections) {
            if (conn.x != coords.x || conn.y != coords.y) {
                if (!consumed[conn.x][conn.y]) {
                    hasContinue = true
                    coords = { x: conn.x, y: conn.y }
                    symbol = input[conn.x][conn.y]
                    if (symbol == '.')
                        console.log('wwwtttfff')
                    console.log(conn.x, conn.y, input[conn.x][conn.y])
                    consumed[conn.x][conn.y] = true
                    walked[startPoint.symbol].push({ x: conn.x, y: conn.y })
                }
            }
        }
    }
}
for (let k in walked) {
    let path = walked[k]
    if (path.length > 1)
        console.log(path.length / 2 + 1)
}
// console.log(JSON.stringify(walked))
