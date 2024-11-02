

class SqlSyntax:

    def SELECT_column_FROM_table(count = False, *columns, table_name="", query=""):
        
        query_count = "COUNT" if count == True else ""
        query_columns = ", ".join(columns)

        query_syntax = f'SELECT {query_count} {query_columns} FROM {table_name}'
        return query_syntax
    
    def SELECT_DISTINCT_column_FROM_table(table_name, *columns):
        """The SELECT DISTINCT statement is used to return only distinct (different) values."""
        
        query_columns = ", ".join(columns)
        query_syntax = f'SELECT DISTINCT {query_columns} FROM {table_name}'
        return query_syntax
        