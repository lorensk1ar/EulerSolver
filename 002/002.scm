; even?
(define (even? n)
	(= (/ n 2) (floor (/ n 2)))
)

; sum if even fibonacci
(define (sum_even_fibs e f limit)
	(cond 
    ((>= f limit) 0)
		((even? f) (+ f (sum_even_fibs  f (+ f e) limit)))
		(else (sum_even_fibs f (+ f e) limit))
  )
)

; main
(sum_even_fibs 1 1 4000000)
