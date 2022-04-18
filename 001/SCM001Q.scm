; Gauss summation
(define (gauss_sum n)
  (/ (* n (+ n 1)) 2)
)

; up to but not including limit
(define (lessthan n)
  (- n 0.000000001)
)

; count every kth integer
(define (count limit k)
  (floor (/ (lessthan limit) k))
)

; greatest common divisor
(define (gcd a b)
  (cond 
    ((not(= b 0)) (gcd b (mod a b)))
    (else a)
  )
)

; least common multiple
(define (lcm a b)
  (/ (* a b) (gcd a b))
)

; sum if divisible using Gauss summation
(define (main limit a b)
  (+ 
  (* a (gauss_sum (count limit a)))
  (* b (gauss_sum (count limit b)))
  (* (- 0 (lcm a b)) (gauss_sum (count limit (lcm a b))))
  )
)

; main
(main 1000 3 5)
  




