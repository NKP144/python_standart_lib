from clickhouse_driver import Client
from datetime import date
from datetime import datetime

client = Client(host='localhost',
                database='test_database')
# client = Client(host='10.10.13.26',
#                 password='yg6LYvbbBGnJ',
#                 user='default',
#                 database='tutorial',
#                 compression='lz4')


print(client.execute('SHOW DATABASES'))
# print(client.execute('SELECT * FROM system.numbers LIMIT 5'))
#
# string = "SELECT %(date)s, %(a)s + %(b)s" % {'date': date.today(), 'a': 1, 'b': 2}
# print(string)
# print(client.execute('SELECT %(date)s, %(a)s + %(b)s', {'date': date.today(), 'a': 1, 'b': 2}))
# print(client.execute("SELECT 'test' like '%%es%%', %(myvar)s", {'myvar': 1}))

# progress = client.execute_with_progress("SELECT Timestamp, Lat, Lon, Speed, Course, "
#                                         "Sat, HandlerAngle, SignalQuality, RFID "
#                                         "from routes where TrackerId='12345678.10043' order by Timestamp DESC")

# progress = client.execute_with_progress("SELECT * from routes where TrackerId='12345678.10043' order by Timestamp DESC")
#
# timeout = 20
# started_at = datetime.now()
# print(f"started_at {started_at}")
#
# for num_rows, total_rows in progress:
#     print(f"num_rows = {num_rows}, total_rows = {total_rows}")
#     if total_rows:
#         done = float(num_rows) / total_rows
#     else:
#         done = total_rows
#     print(f"done = {done}")
#
#     now = datetime.now()
#     print(f"now {now}")
#
#     elapsed = (now - started_at).total_seconds()
#     print(f"elapsed = {elapsed}")
#
#     if elapsed > timeout and done < 0.5:
#         client.cancel()
#     else:
#         rv = progress.get_result()
#         print(rv)


# settings = {'max_block_size': 100000}
# rows_gen = client.execute_iter("SELECT Timestamp, Lat, Lon, "
#                                "SignalQuality, TrackerId "
#                                "from routes where TrackerId='12345678.10043' order by Timestamp DESC LIMIT 100",
#                                settings=settings)
# for row in rows_gen:
#     print(row)
#
# rows_gen = client.execute_iter("SELECT Timestamp, Lat, Lon, "
#                                "SignalQuality, TrackerId "
#                                "from routes where TrackerId='830000002.10043' order by Timestamp DESC LIMIT 100",
#                                settings=settings)
# for row in rows_gen:
#     print(row)

# client.execute('INSERT INTO text (x) VALUES (%(a)s), (%(b)s)', {'a': 1, 'b': 2})
client.execute('INSERT INTO text (x) VALUES', [{'x': '1'}, {'x': '2'}, {'x': '3'}, {'x': '100'}])
client.execute('INSERT INTO text (x) VALUES', [['200']])
