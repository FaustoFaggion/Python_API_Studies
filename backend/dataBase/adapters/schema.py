import re

class DatabaseSchema:

    tables_schema = [
        {
            "users":            """(
                                email       TEXT            PRIMARY KEY,
                                name        TEXT            NOT NULL,
                                age         INTEGER         NOT NULL,
                                password    TEXT            NOT NULL
                                );"""
        },
        {
            'cylinder_bore_mobil':  """(
                                diam_int    INTEGER         PRIMARY KEY,
                                diam_ext    INTEGER         NOT NULL,
                                max_course  INTEGER         NOT NULL,
                                max_compr   INTEGER         NOT NULL,
                                conex_diam  VARCHAR(5)      NOT NULL,
                                conex_type  VARCHAR(50)     NOT NULL,
                                weight      FLOAT           NOT NULL,
                                material    TEXT            NOT NULL,
                                condition   TEXT            NOT NULL
                            )"""
        },
        {
        'cylinder_rod_mobil':   """(
                                diam        INTEGER         PRIMARY KEY,
                                curso       INTEGER         NOT NULL,
                                ponta_haste INTEGER         NOT NULL,
                                max_compr   INTEGER         NOT NULL,
                                weight      FLOAT           NOT NULL,
                                material    VARCHAR(50)     NOT NULL
                            )"""
        },
        {
        'cylinder':       """(
                                id          SERIAL          PRIMARY KEY,
                                rod_diam    INTEGER         NOT NULL,
                                bore_diam   INTEGER         NOT NULL,
                                type        VARCHAR(50)     NOT NULL,
                                FOREIGN KEY (bore_diam) REFERENCES "cylinder_bore_mobil" (diam_int),
                                FOREIGN KEY (rod_diam) REFERENCES "cylinder_rod_mobil" (diam)
                            )"""
        }
    ]

    table_columns = {}

    def create_table_columns(self):
        for table_dict in self.tables_schema:
            for key, value in table_dict.items():
                column_key = key
                schema = value.strip("()").strip()
                # Split the schema by lines (columns)
                lines = schema.split(",\n")
                # Extract the first word of each line (the column name)
                columns = [re.match(r'^\s*(\w+)', line).group(1) for line in lines if line.strip() and "FOREIGN" not in line and "SERIAL" not in line]
                column_names = f"({', '.join(columns)})"
                self.table_columns[column_key] = column_names
                
        print("table_columns: ", self.table_columns)

    def __init__(self):
        self.create_table_columns
    
    # "cylinder_rod":     """(
    #                         id          INTEGER     PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    #                         diameter    INTEGER     NOT NULL,
    #                         material    TEXT        NOT NULL
    #                     );""",

    # "cylinder_barrel":  """(
    #                         id          INTEGER     PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    #                         diameter    INTEGER     NOT NULL,
    #                         material    TEXT        NOT NULL
    #                     );""",

    # "cylinder":         """(
    #                         id          INTEGER     PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    #                         rod_id      INTEGER     NOT NULL,
    #                         barrel_id   INTEGER     NOT NULL,
    #                         FOREIGN KEY (barrel_id) REFERENCES "cylinder_barrel" (id),
    #                         FOREIGN KEY (rod_id) REFERENCES "cylinder_rod" (id)
    #                     );"""

