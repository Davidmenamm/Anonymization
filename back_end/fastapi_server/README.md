# Anonymization
Backend for anonymization web app.


# JSON string config example
{
    "techniques" : {
        "mask" : [
            {
                "columns": ["OriginCityName", "DestCityName"],
                "direction": "left",
                "quantity": 5,
                "symbol": "*"
            }
        ],
        "noise" : [
            {
                "columns": ["TaxiOut"],
                "operator": "-",
                "quantity": 5,
                "rounding": 2,        
                "rand": true,
                "seed": 30
            }
        ],
        "swap" : [
            {
                "columns": ["TaxiOut"],
                "type": "independent",
                "seed": 30
            }
        ],
        "generalize" : [
            {
                "columns": ["TaxiOut"],
                "num_range": 1000,
                "str_level": 2,
                "date_type": "year"
            }
        ],
        "pseudonymization" : [
            {
                "unique_index": ["TaxiOut"],
                "private_columns": ["TaxiOut"]
            }
        ]
    }
}


"mask" : TARJETA., CORREO., FECHA_NACIMIENTO.
"noise" : PROMEDIO
"swap" :  SEMESTRE., CIUDAD.
"generalize" : NOMBRE., EDAD., FECHA_REGISTRO.
"pseudonymization" : CODIGO., DEUDAS DIRECCION.


{
    "techniques" : {
        "mask" : [
            {
                "columns": ["name"],
                "direction": "right",
                "quantity": 4,
                "symbol": "*"
            }
        ],
        "noise" : [
            {
                "columns": ["episodes"],
                "operator": "+",
                "quantity": 50,
                "rounding": 2,        
                "rand": false,
                "seed": 30
            }
        ],
        "swap" : [
            {
                "columns": ["members"],
                "type": "independent",
                "seed": 30
            }
        ],
        "generalize" : [
            {
                "columns": ["rating"],
                "num_range": 2,
                "str_level": 2,
                "date_type": "year"
            },
            {
                "columns": ["genre"],
                "num_range": 1000,
                "str_level": 2,
                "date_type": "year"
            },
            {
                "columns": ["date"],
                "num_range": 1000,
                "str_level": 2,
                "date_type": "year"
            }
        ],
        "pseudonymization" : [
            {
                "unique_index": ["anime_id"],
                "private_columns": ["type"]
            }
        ]
    }
}