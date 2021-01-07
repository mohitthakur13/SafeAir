import intervals as I

iaqi = {
        'good' : I.closed(0, 25),
        'moderate' : I.closed(25, 50),
        'unhealthy' : I.closed(50, 75),
        'hazardous' : I.closed(75, 100)
    }
