; modulo
(define (mod n d)
  (round (* d (- (/ n d) (floor (/ n d)))))
)

; divisible by?
(define (div? n d)
  (= (/ n d) (floor (/ n d)))
)

; already exists as expt
(define (pow b e)
  (let ((x (floor (/ e 2))))
    (cond
        ((= e 0) 1)
        ((= e 1) b)
        (else (* (pow b x) (pow b (- e x))))
    )
  )
)
