
/**
 * @param arrayA is a list<int>
 * @param arrayB is a list<int>
 * @returns list<int>
 */
 export function interleaveArrays(arrayA, arrayB) {
    var outputArray = []
    if (arrayA.length>arrayB.length){
      var longer = arrayA
    }
    else{
      longer = arrayB
    }
  
    for (let i = 0; i<longer.length; i++){
      if(i >= arrayB.length){
        outputArray.push(arrayA[i])
      }
      else if(i>= arrayA.length){
        outputArray.push(arrayB[i])
      }
      else{
        outputArray.push(arrayA[i])
        outputArray.push(arrayB[i])
      }
    }
    return outputArray
  }

  arrayA = [2,4,6,8]
  arrayB = [1,3,9]

  console.log(interleaveArrays(arrayA, arrayB))