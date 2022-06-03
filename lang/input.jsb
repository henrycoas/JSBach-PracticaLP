Main |:
    Hanoi
    Alle_Schlussel
:|

Hanoi |:
    src <- {C D E F G}
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <::2> note
        <::3> note
        HanoiRec (n - 1) aux dst src
    :|
:|

Alle_Schlussel |:
    note <- A0
    while note <= C8 |:
        <::1> note
        note <- note + 1
    :|
:|
