queries = {
    "column": {
        "head": "select {column} from {schema}.{table} where rownum <= {n}",
        "all": "select {column} from {schema}.{table}",
        "unique": "select distinct {column} from {schema}.{table}",
        "sample": """
                select
                    {column}
                from (
                    select
                        {column}
                    from
                        {schema}.{table}
                    order by
                        dbms_random.value
                    ) x
                where
                    rownum <= {n}
            """
    },
    "table": {
        "select": "select {columns} from {schema}.{table}",
        "head": "select * from {schema}.{table} where rownum <= {n}",
        "all": "select * from {schema}.{table}",
        "unique": "select distinct {columns} from {schema}.{table}",
        "sample": """
                select
                    *
                from (
                    select
                        *
                    from
                        {schema}.{table}
                    order by
                        dbms_random.value
                    ) x
                where
                    rownum <= {n}
            """
    },
    "system": {
        "schema_no_system": """
            select
                a.owner as table_schema
                , c.table_name
                , c.column_name
                , c.data_type
            from
                all_tab_columns c
                join all_tables a
                    on c.table_name = a.table_name
            where
                a.owner not in ('SYS', 'SYSTEM', 'OWBSYS')
        """,
        "schema_with_system": """
            select
                a.owner as table_schema
                , c.table_name
                , c.column_name
                , c.data_type
            from
                all_tab_columns c
                join all_tables a
                    on c.table_name = a.table_name
        """,
        "schema_specified": """
            select
                a.tablespace_name as table_schema
                , a.owner as table_schema
                , c.table_name
                , c.column_name
                , c.data_type
            from
                all_tab_columns c
                join all_tables a
                    on c.table_name = a.table_name
            where
                a.owner in (%s)
        """,
        # See https://stackoverflow.com/questions/1729996/list-of-foreign-keys-and-the-tables-they-reference
        "foreign_keys_for_db": """
            select
                a.column_name
                , c_pk.table_name as foreign_table_name
                , c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
        """,
        "foreign_keys_for_table": """
            select
                a.column_name,
                c_pk.table_name as foreign_table_name,
                c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
                and a.table_name = '{table}'
        """,
        "foreign_keys_for_column": """
            select
                a.column_name,
                c_pk.table_name as foreign_table_name,
                c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
                and a.table_name = '{table}'
                and a.column_name = '{column}'
        """,
        "ref_keys_for_db": """
            select
                a.column_name,
                c_pk.table_name as foreign_table_name,
                c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
        """,
        "ref_keys_for_table": """
            select
                a.column_name,
                c_pk.table_name as foreign_table_name,
                c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
                and a.table_name = '{table}'
        """,
        "ref_keys_for_column": """
            select
                a.column_name,
                c_pk.table_name as foreign_table_name,
                c_pk.index_name as foreign_column_name
            from
                all_cons_columns a
            join all_constraints c
                on a.owner = c.owner
                and a.constraint_name = c.constraint_name
            join all_constraints c_pk
                on c.r_owner = c_pk.owner
                and c.r_constraint_name = c_pk.constraint_name
            where
                c.constraint_type = 'r'
                and a.table_name = '{table}'
                and a.column_name = '{column}'
        """,
   }
}
