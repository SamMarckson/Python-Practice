// SOURCE: https://www.codewars.com/kata/559a28007caad2ac4e000083/solutions/javascript

function perimeter(n) {
    let i = 1;
    let fiboArray = [0, 1];
    let allSidesSum = 1;
    while(i < n+1){
        let sum = fiboArray[i] + fiboArray[i - 1];
        fiboArray.push(sum);
        allSidesSum += sum;
        sum = 0;
        i++;
    }
    return 4*allSidesSum;
}

console.log(perimeter(30));

