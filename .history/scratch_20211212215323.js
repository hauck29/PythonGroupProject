let array = []

function createArray(a) {
  for (let i = 0; i <= 120; i++){
    a.push(i)
  }
}

createArray(array)

function randomArrayShuffle(array) {
  let currentIndex = array.length, temporaryValue, randomIndex;
  while (0 !== currentIndex) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
return array
}

randomArrayShuffle(array)

array.forEach(ele => {
  console.log(`db.session.add(p${ele})`)
})
array.forEach(ele => {
  console.log(`db.session.add(photo${ele})`)
})


2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
2021-12-12 21:49:26.044706
