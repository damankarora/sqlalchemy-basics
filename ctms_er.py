from sqlalchemy import *
from generate import generateHTML

def ctms_er(db_string):
    engine = create_engine(db_string)
    with engine.connect() as conn:

        result = conn.execute(text("SELECT * FROM studies LIMIT 1"))
        print(result.all())
        metadata_obj = MetaData(engine, schema='ctgov')

        # Loading up all the existing tables.
        metadata_obj.reflect(engine, resolve_fks=True)

        mapping_dict = {}

        # Loading a single table.
        # outcome_measurements = Table('outcome_measurements', metadata_obj, autoload=True)

        print("========== List of tables ==============")
        for t in metadata_obj.sorted_tables:     
            print("*********************************************************")   
            print("Table name: ")
            print(t.name)

            for constraint in t.constraints:
                print(type(constraint) == ForeignKeyConstraint)
                if(type(constraint) == ForeignKeyConstraint):
                    print("Foreign constraint found..")
                    # print(constraint.column_keys, " From", constraint.referred_table)

                    depends_on.append({"column": constraint.column_keys[0]+"x"+constraint.elements[0].column.name, "table": constraint.referred_table.name})


            print("** Primary key columns:")
            depends_on = []
            for p_key in t.primary_key:
                print(p_key)

            # Another way to get foreign key columns
            
            # print("** Foreign key columns: ")
            # for f_key in t.foreign_keys:
            #     print(f_key.column.table.name, " for colum: ")
            #     print(f_key)
            #     depends_on.append({"table": f_key.column.table.name, "column": f_key.column.name})

            mapping_dict[t.name] = depends_on

        print(mapping_dict)
        generateHTML(mapping_dict)