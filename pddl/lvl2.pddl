(define (problem boxUp-lvl1)
    (:domain boxUp)

    (:objects
        point blue red
        row1 row2 row3
        col1 col2 col3
    )
    
    (:init

        (next-row row1 row2)
        (next-row row2 row3)
        (next-col col1 col2)
        (next-col col2 col3)

        (faces-west red)
        (is-small red)
        (iwp red)
        (object-at red row2 col3)

        (faces-north blue)
        (is-large blue)
        (iwp blue)
        (object-at blue row2 col1)

        (object-at point row2 col2)

        (is-empty row1 col1)
        (is-empty row1 col2)
        (is-empty row1 col3)
        (not (is-inside point))
        ; (is-empty row2 col1)
        ; (is-empty row2 col3)

        (is-empty row3 col1)
        (is-empty row3 col2)
        (is-empty row3 col3)
    )
    
    (:goal 
        (and
            ; (object-at red row1 col3)
            ; (object-at blue row2 col2) 
            ; (object-at point row1 col1)
            (object-in point red)
            (object-in red blue)
        )
    )
)