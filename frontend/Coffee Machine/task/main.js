const input = require('sync-input')

console.log('Write how many cups of coffee you will need:')
num = Number(input())
console.log(`For ${num} cups of coffee you will need:
${num * 200} ml of water
${num * 50} ml of milk
${num * 15} g of coffee beans`)
