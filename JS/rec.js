// recusion 
function printrec(num){
    if(num <= 10){
        console.log(num)
        printrec(num + 1)
    }

}

printrec(1)