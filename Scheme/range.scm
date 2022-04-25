; start stop step
; EXAMPLE:
; (numbers 0 10 2) --> (0 2 4 6 8 10)
; (numbers 10 0 -1) --> (10 9 8 7 6 5 4 3 2 1 0)

(define (numbers start stop step)
  (if (= start stop)
     (list stop) 
     (cons start (numbers (+ start step) stop step))
  )
)

