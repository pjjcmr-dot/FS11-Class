// function solution(numbers) {
//   let max1 = 0;
//   let max2 = 0;

//   for (let i = 0; i < numbers.length; i++) {
//     if (numbers[i] > max1) {
//       max2 = max1;
//       max1 = numbers[i];
//     } else if (numbers[i] > max2) {
//       max2 = numbers[i];
//     }
//   }

//   console.log(max1 * max2);
// }
// solution([1, 2, 3, 4, 5]);

// function solution(numbers) {
//   let max1 = 0;
//   let max2 = 0;

//   for (let i = 0; i < numbers.length; i++) {
//     if (numbers[i] > max1) {
//       max2 = max1;
//       max1 = numbers[i];
//     } else if (numbers[i] > max2) {
//       max2 = numbers[i];
//     }
//   }
//!   const result = max1 * max2;
//!   console.log(result);
// }

//! solution([1, 2, 3, 4, 5]);
//! solution([0, 31, 24, 10, 1, 9]);

// function solution(numbers) {
//?   let max1 = 1;
//?   let max2 = 1;
//!   for (let i = 1; i < numbers[i]; i++) {
//*FIXME:numbers.length를 사용하지 않을경우
//     if (numbers[i] > max1) {
//       max2 = max1;
//       max1 = numbers[i];
//     } else if (numbers[i] > max2) {
//       max2 = numbers[i];
//     }
//   }
//?   const result = max1 * max2;
//?   return result;
// }

// console.log(solution([1, 2, 3, 4, 5]));
// console.log(solution([0, 31, 24, 10, 1, 9]));

//TODO: 최종 코드 정리
// function solution(numbers) {
//   let max1 = 0;
//   let max2 = 0;

//   for (let i = 0; i < numbers.length; i++) {
//     if (numbers[i] > max1) {
//       max2 = max1;
//       max1 = numbers[i];
//     } else if (numbers[i] > max2) {
//       max2 = numbers[i];
//     }
//   }
//!   return max1 * max2;
// }
//
//!console.log(solution([1, 2, 3, 4, 5]));
//!
//
//
// 매소드 사용
// function solution(numbers) {
//   numbers.sort((a, b) => b - a);
//   return numbers[0] * numbers[1];
// }
// //
// function solution(numbers) {
//   let [a, b] = numbers.sort((a, b) => b - a);
//   return a * b;
// }
// //
// function solution(numbers) {
//   numbers = numbers.sort((a, b) => a - b);
//   return numbers.at(-1) * numbers.at(-2);
// }
// //
// function solution(numbers) {
//   numbers.sort((a, b) => a - b).reverse();
//   return numbers[0] * numbers[1];
// }
// //
// function solution(numbers) {
//   return numbers
//     .sort((a, b) => b - a)
//     .slice(0, 2)
//     .reduce((a, b) => a * b);
// }

// function* gen() {
//   yield 1;
//   yield 3;
// }

// const it = gen();
// console.log(it.next(), it.next().value);
// // 출력: 1 2 3

function solution(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers[0] * numbers[1];
}
// 문제에서 두 개를 곱해 만들 수 있는 최대값을 구하는 것이므로 내림차순을 하여 최대 숫자를 0, 1의 자리에 배치하여 곱셈 계산
console.log(solution([1, 2, 3, 4, 5]));
console.log(solution([0, 31, 24, 10, 1, 9]));
