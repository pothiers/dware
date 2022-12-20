;; R5RS Scheme
;; https://www.schemers.org/

(import (srfi 69))

(define general-config (make-hash-table eq?))

(hash-table-set! general-config 'project-name "pict_warehouse")
;; ...
