import json
import MySQLdb as mdb
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.conf import settings

def get_connection():
    defaultdb = settings.DATABASES['default']
    con = mdb.connect(defaultdb['HOST'], 
                      defaultdb['USER'],
                      defaultdb['PASSWORD'],
                      defaultdb['NAME'])
    return con

def _fix_in_clause(sql, *values):
    assert sql.count('%s') == len(values), (sql, values)
    placeholders = []
    new_values = []
    for value in values:
        if isinstance(value, (list, tuple)):
            placeholders.append(', '.join(['%s'] * len(value)))
            new_values.extend(value)
        else:
            placeholders.append('%s')
            new_values.append(value)
    sql = sql % tuple(placeholders)
    values = tuple(new_values)
    return (sql, values)

def _query(sql, single_row_mode, *args):
    '''
    Executes the query and returns a list of objects
    '''
    query, values = _fix_in_clause(sql, *args)
    conn = get_connection()
    with conn:
        cur = conn.cursor(mdb.cursors.DictCursor)
        cur.execute(query, values)
        if single_row_mode:
            return cur.fetchone()
        else:
            rows = cur.fetchall()
            return list(rows)

def query(sql, *args):
    '''Examples 
    query("Select .. where a=%s and b in (%s)", [1, (1, 2, 3)]))
    query("Select .. where a=%s and b in (%s)", [1, [1, 2, 3]]))
    query("Select .. where a=%s and b in (%s)", [1, ('a', 'b', 'c']]))    
    '''
    return _query(sql, False, *args)


def query_for_object(sql, *args):
    return _query(sql, True, *args)

def query_as_json(sql, *args):
    objects = query(sql, *args)
    return json.dumps(objects, encoding="ISO-8859-1")
