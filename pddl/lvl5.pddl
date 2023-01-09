(define (problem boxUp-lvl1)
    (:domain boxUp)

    (:objects
        point blue red 
        largeBlack smallBlack
        row1 row2 row3 row4
        col1 col2 col3 col4
    )
    
    (:init

        (next-row row1 row2)
        (next-row row2 row3)
        (next-row row3 row4)
        (next-col col1 col2)
        (next-col col2 col3)
        (next-col col3 col4)

        (faces-east red)
        (is-small red)
        (iwp red)
        (object-at red row2 col3)

        (faces-south blue)
        (is-large blue)
        (iwp blue)
        (object-at blue row1 col4)

        (faces-north largeBlack)
        (is-large largeBlack)
        (iwp largeBlack)
        (object-at largeBlack row4 col1)

        (faces-west smallBlack)
        (is-small smallBlack)
        (iwp smallBlack)
        (object-at smallBlack row3 col2)

        (object-at point row1 col3)
        (not (is-inside point))

        (is-empty row1 col1)
        (is-empty row1 col2)
        ; (is-empty row1 col3)
        ; (is-empty row1 col4)
        (is-empty row2 col1)
        ; (is-empty row2 col3)
        (is-empty row2 col4)

        (is-empty row3 col1)
        ; (is-empty row3 col2)
        ; (is-empty row3 col3)
        (is-empty row3 col4)
        ; (is-empty row4 col1)
        (is-empty row4 col2)
        (is-empty row4 col3)
        (is-empty row4 col4)
    )
    
    (:goal 
        (and
            ; (object-at red row1 col3)
            ; (object-at red row3 col3)
            ; (object-at blue row2 col2) 
            ; (object-at largeBlack row3 col3) 
            ; (object-at point row1 col1)
            ; (object-in red largeBlack)
            (object-in red blue)
            (object-in point red)
        )
    )
)