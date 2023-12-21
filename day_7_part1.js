let cardStrenght = 'A,K,Q,J,T,9,8,7,6,5,4,3,2'
cardStrenght = cardStrenght.split(',')

let handStrenght = 'Five of a kind,Four of a kind,Full house,Three of a kind,Two pair,One pair,High card'
handStrenght = handStrenght.split(',')


function getCount(hand) {
    return hand.reduce((acc, cur) => {
        if (!acc[cur])
            acc[cur] = 1
        else
            acc[cur]++
        return acc
    }, {})

}

function getHandType(count) {
    //this can be switch TODO
    let keys = Object.keys(count)
    if (keys.length == 1)
        return 'Five of a kind'
    else if (keys.length == 2) {
        for (let k of keys) {
            if (count[k] == 4)
                return 'Four of a kind'
        }
        return 'Full house'
    }
    else if (keys.length == 3) {
        for (let k of keys) {
            if (count[k] == 3)
                return 'Three of a kind'
        }
        return 'Two pair'
    }
    else if (keys.length == 4) {
        return 'One pair'
    }
    else return 'High card'
}

function compareHands(a, b) {
    let fst = a.hand.split('')
    let snd = b.hand.split('')
    let [fstTp, sndTp] = [getHandType(getCount(fst)), getHandType(getCount(snd))]
    if (handStrenght.indexOf(fstTp) > handStrenght.indexOf(sndTp))
        return -1
    else if (handStrenght.indexOf(fstTp) < handStrenght.indexOf(sndTp))
        return +1
    else {
        for (let i = 0; i < fst.length; i++) {
            const fstEl = fst[i];
            const sndEl = snd[i];
            if (cardStrenght.indexOf(fstEl) > cardStrenght.indexOf(sndEl))
                return -1
            else if (cardStrenght.indexOf(fstEl) < cardStrenght.indexOf(sndEl))
                return +1
        }
    }
    return 0
}

let testData = `secret`

testData = testData.split('\n')
data = testData.map(x => {
    let tmp = x.split(' ')
    return { 'hand': tmp[0], 'bid': parseInt(tmp[1]) }
})
result = data.toSorted(compareHands).reduce((acc, cur, index) => {
    acc += cur.bid * (index + 1)
    return acc
}, 0)

console.table(result)