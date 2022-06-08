
/**
 * @param arr is a list<int>
 * @returns int
 */
function arrayBalanceIndex(arr) {

  for (var i = 1; i<arr.length-1; i++) {
    var rightSum=0;
    var leftSum=0;
    for (var j = 0; j < i; j++){
      leftSum += arr[j];
    }
    for (var k=arr.length-1; k>i; k--){
      rightSum =+ arr[k];
      }

      console.log(rightSum);
      console.log(leftSum);

      if (leftSum===rightSum) {
        return i;
      }
    }
    return -1;
  }


arrayBalanceIndex([5, 2, 5]);