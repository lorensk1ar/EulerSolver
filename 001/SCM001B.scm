; a modulo b
(define (modulo a b)
  (if (< a b) 
    a
    (modulo (- a b) b)
  )
)

; a divisible by b?
(define (div? a b)
	(= 0 (modulo a b))
)

; sum if divisible
(define (sum_if n)
	(cond ((= n 1) 0)
		((div? n 3) (+ n (sum_if(- n 1))))
		((div? n 5) (+ n (sum_if(- n 1))))
		(else (sum_if(- n 1)))
  )
)

; main
(sum_if (- 1000 1))

