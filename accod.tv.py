    const _ = require("lodash")

const handleJSON = (jsonString, saveToFile) => {
    let username = jsonString.username.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-zA-Z ]/g, "")
    username = username.trim().split(' ').join('_')
    let filename = jsonString.filename.normalize("NFD").replace(/[\u0300-\u036f]/g, "")
    filename = filename.trim()
   console.log(username,filename)
   delete jsonString['username']
   delete jsonString['filename']
   console.log(jsonString);
   
//    setInterval(()=>{
//        console.log("amaan")
//    },1000)

    // Feel free to use console.log() for debugging purposes
    // console.log(jsonString)

    // Here is an example usage of saveToFile function
    // saveToFile("username", "filename", `{"good":"luck"}`)
}
// module.exports = handleJSON

const json = {"filename": "ILikeProps", "prop": "Hi I'm a prop", "username": "???ta g??"}

let call =_.debounce(handleJSON, [wait=300], [{leading:true,trailing: false}])
call(json)



// function solution(S) {
//     // write your code in JavaScript (Node.js 8.9.4)
//     let newRows = []
//     let rows = S.split(/\r\n|\n/);
//     for (let i =0 ;i<rows.length;i++){
//         rows[i] = rows[i].split(',')
//     }
//     console.log(rows)
//     for (let i = 0;i<rows.length;i++){
//         isValid = true
//         for (let j = 0 ; j < rows[i].length;j++){
//             if (rows[i][j] == 'NULL'){
//                 isValid = false;
//             }
//         }
//         if(isValid) newRows.push(rows[i].join(','));
//     }
//     console.log(newRows.join('\n'))
// }

// solution('header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL')