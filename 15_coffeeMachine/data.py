recursos:dict[str, int] = {
    'agua': 1000,
    'cafe': 100,
    'leche': 500,
    'dinero': 0 #TODO: convertir a diccionario de monedas
    }

sabores:list[dict] = [
    {
        'espresso': {
            'ingredientes': {
                'agua': 50,
                'cafe': 18
            },
            'costo': 200
        },

        'latte':{
            'ingredientes': {
                'agua': 200,
                'cafe': 24,
                'leche': 150
            },
            'costo': 1000
        },

        'capuccino':{
            'ingredientes':{
                'agua': 250,
                'cafe': 24,
                'leche': 100
            },
            'costo': 500
        }
    }
]