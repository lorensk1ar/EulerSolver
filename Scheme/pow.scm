; base ^ exponent
(define (pow b e)
  (let ((x (floor (/ e 2))))
    (cond
        ((= e 0) 1)
        ((= e 1) b)
        (else (* (pow b x) (pow b (- e x))))
    )
  )
)

; Note that this function already exists as expt
