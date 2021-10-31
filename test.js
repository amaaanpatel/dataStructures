



function test(array){

    // let sortedArray = array.sort(function(a,b){return a -b})
    let sortedArray = array
    console.log(sortedArray)
    let max = 0
    let count = {}
    for (let i=0;i<sortedArray.length;i++){
       if(count[sortedArray[i]]) {
        count[sortedArray[i]] = count[sortedArray[i]] + 1
       } else {
        count[sortedArray[i]] = 1;
       }
    }
    console.log(count)
    for (let key in count){
        console.log(key);
        if( key == count[key] ){
            if(count[key] > max){
                max = count[key]
            }
        }

    }

    console.log(max)

}
test([2,2,3,4])