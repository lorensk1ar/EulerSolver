var limit = 4000000;
var total = 0;

let e = 1;
let f = 1;
let i = 1;

while (f < limit) {
  console.log(i, f);
  tmp = e;
  e = f;
  f = f + tmp;
  i++;


  if (f % 2 == 0) {total += f;}
}

console.log(total)
