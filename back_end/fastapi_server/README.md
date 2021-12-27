# Anonymization
Backend for anonymization web app.


# JSON string config example

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
                "date_type": "year",
                "day_first": true,
                "year_first": false
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