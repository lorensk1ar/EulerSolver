; TO DO
; generate list of primes up to square root?
; reduce by each prime in list

(define (increment f)
  (cond 
    ((= f 2) 3)
    (else (+ f 2))
   )
)

(define (stop n)
  (sqrt n)
)

(define (reduce n f)
	(cond
    ; if stop, return remainder
    ((> f (stop n)) n)
   
    ; if divisible, reduce by current factor
		((div? n f) (reduce (/ n f) f))
   
    ; if 1, return most recent factor 
    ((= n 1) f)

    ; otherwise increment
    (else (reduce n (increment f)))
  )
)

(reduce 600851475143 2)
