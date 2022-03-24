const arr=[1000,500,100,50,20,10,2,1]
const minn = a => {
    let coins =0;
    let i=0
    while (i < a.length) {
        if (a >=arr[i]) {
            a= a - arr[i]
            coins += 1
        }else{
            i++;
        };
    };
   console.log(coins);
}
minn(120);
// op=[1,2,34,5,6,78,55]
// // op={1:10,
// //     13:90}
// // for (const i in op) {
// //     console.log(op[i]);
// // }
// o=0
// while(o<op.length) {
//     console.log(op[o]);
//     o++;
// }